"""
Agriculture-focused chatbot for BharatAgri AI.
Rule-based agricultural knowledge system with multilingual support.
"""
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.database import get_db, ChatHistory, User
from app.routes.auth import get_current_user
from app.data.india_data import CROP_CONDITIONS, STATES_DATA, SOIL_CHARACTERISTICS, CROP_AVG_YIELDS

router = APIRouter(prefix="/api/chatbot", tags=["Chatbot"])


class ChatMessage(BaseModel):
    message: str
    language: str = "en"
    context: dict = None


KNOWLEDGE_BASE = {
    "npk": {
        "en": "**NPK** stands for Nitrogen (N), Phosphorus (P), and Potassium (K) — the three primary nutrients essential for plant growth.\n\n• **Nitrogen (N):** Promotes leaf and stem growth, gives plants their green color\n• **Phosphorus (P):** Supports root development, flowering, and fruiting\n• **Potassium (K):** Strengthens plant immunity, improves water regulation\n\nYou can find your soil's NPK values from your **Soil Health Card** issued by the government, or by getting a soil test done at your nearest agricultural lab.",
        "hi": "**NPK** का मतलब है नाइट्रोजन (N), फॉस्फोरस (P), और पोटेशियम (K) — पौधों की वृद्धि के लिए तीन प्रमुख पोषक तत्व।\n\n• **नाइट्रोजन (N):** पत्तियों और तने की वृद्धि को बढ़ावा देता है\n• **फॉस्फोरस (P):** जड़ विकास, फूल और फल को सहायता देता है\n• **पोटेशियम (K):** पौधे की प्रतिरक्षा को मजबूत करता है\n\nआप अपनी मिट्टी के NPK मान **मृदा स्वास्थ्य कार्ड** से प्राप्त कर सकते हैं।",
        "gu": "**NPK** એટલે નાઇટ્રોજન (N), ફોસ્ફરસ (P), અને પોટેશિયમ (K) — છોડના વિકાસ માટે ત્રણ મુખ્ય પોષક તત્વો.\n\n• **નાઇટ્રોજન (N):** પાંદડા અને દાંડીના વિકાસને પ્રોત્સાહન આપે છે\n• **ફોસ્ફરસ (P):** મૂળ વિકાસ, ફૂલ અને ફળને સહાય કરે છે\n• **પોટેશિયમ (K):** છોડની રોગપ્રતિકારક શક્તિ મજબૂત કરે છે\n\nતમારી માટીના NPK મૂલ્યો **માટી આરોગ્ય કાર્ડ** માંથી મેળવો."
    },
    "soil_health_card": {
        "en": "**Soil Health Card (SHC)** is a government scheme that provides farmers with information about the nutrient status of their soil.\n\n📋 **How to get one:**\n1. Visit your nearest Krishi Vigyan Kendra (KVK) or agriculture office\n2. Submit a soil sample\n3. Results include: N, P, K levels, pH, organic carbon, and micronutrients\n4. Cards are issued free of cost\n\n🌐 Apply online at: soilhealth.dac.gov.in",
        "hi": "**मृदा स्वास्थ्य कार्ड (SHC)** एक सरकारी योजना है जो किसानों को मिट्टी की पोषक स्थिति की जानकारी देती है।\n\n📋 **कैसे प्राप्त करें:**\n1. अपने निकटतम कृषि विज्ञान केंद्र (KVK) पर जाएं\n2. मिट्टी का नमूना जमा करें\n3. परिणाम: N, P, K स्तर, pH, कार्बनिक कार्बन\n4. कार्ड मुफ्त में जारी किए जाते हैं",
        "gu": "**માટી આરોગ્ય કાર્ડ (SHC)** એ ખેડૂતોને તેમની માટીની પોષક સ્થિતિ વિશે માહિતી આપતી સરકારી યોજના છે.\n\n📋 **કેવી રીતે મેળવવું:**\n1. તમારા નજીકના કૃષિ વિજ્ઞાન કેન્દ્ર (KVK)ની મુલાકાત લો\n2. માટીનો નમૂનો જમા કરો\n3. પરિણામ: N, P, K સ્તર, pH, કાર્બનિક કાર્બન\n4. કાર્ડ મફતમાં આપવામાં આવે છે\n\n🌐 ઓનલાઈન અરજી: soilhealth.dac.gov.in"
    },
    "ph": {
        "en": "**Soil pH** measures how acidic or alkaline your soil is, on a scale of 0-14.\n\n• **Below 7:** Acidic soil — common in areas with heavy rainfall\n• **Exactly 7:** Neutral — ideal for most crops\n• **Above 7:** Alkaline soil — common in dry regions\n\nMost crops grow best in pH range of **6.0 to 7.5**. You can test pH using:\n- Soil Health Card\n- pH testing strips (available at agricultural shops)\n- Lab testing",
        "hi": "**मिट्टी का pH** मापता है कि आपकी मिट्टी कितनी अम्लीय या क्षारीय है (0-14 के पैमाने पर)।\n\n• **7 से नीचे:** अम्लीय मिट्टी\n• **7:** उदासीन — अधिकांश फसलों के लिए आदर्श\n• **7 से ऊपर:** क्षारीय मिट्टी\n\nअधिकांश फसलें **6.0 से 7.5** pH में सबसे अच्छी बढ़ती हैं।",
        "gu": "**માટીનો pH** માપે છે કે તમારી માટી કેટલી એસિડિક કે આલ્કલાઇન છે (0-14 ના સ્કેલ પર).\n\n• **7 થી નીચે:** એસિડિક માટી\n• **7:** તટસ્થ — મોટાભાગના પાક માટે આદર્શ\n• **7 થી ઉપર:** આલ્કલાઇન માટી\n\nમોટાભાગના પાક **6.0 થી 7.5** pH માં શ્રેષ્ઠ ઉગે છે."
    },
    "improve_soil": {
        "en": "**Ways to improve soil fertility:**\n\n🌱 **For Low Nitrogen:**\n- Use organic compost or vermicompost\n- Grow legumes (pulses) as cover crops\n- Apply urea fertilizer as a supplement\n\n🌱 **For Low Phosphorus:**\n- Add bone meal or single super phosphate (SSP)\n- Apply DAP (Diammonium Phosphate)\n\n🌱 **For Low Potassium:**\n- Use potash fertilizer (MOP)\n- Add wood ash to soil\n\n🌱 **For pH Correction:**\n- Acidic soil → Add lime (calcium carbonate)\n- Alkaline soil → Add gypsum or sulfur",
        "hi": "**मिट्टी की उर्वरता सुधारने के तरीके:**\n\n🌱 **कम नाइट्रोजन:** जैविक खाद या केंचुआ खाद का उपयोग करें\n🌱 **कम फॉस्फोरस:** हड्डी का चूर्ण या DAP डालें\n🌱 **कम पोटेशियम:** पोटाश उर्वरक (MOP) का उपयोग करें\n🌱 **pH सुधार:** अम्लीय मिट्टी → चूना, क्षारीय मिट्टी → जिप्सम",
        "gu": "**માટીની ફળદ્રુપતા સુધારવાના ઉપાયો:**\n\n🌱 **ઓછો નાઇટ્રોજન:** જૈવિક ખાતર અથવા અળસિયાનું ખાતર વાપરો\n🌱 **ઓછો ફોસ્ફરસ:** હાડકાનો ભૂકો અથવા DAP નાખો\n🌱 **ઓછું પોટેશિયમ:** પોટાશ ખાતર (MOP) વાપરો\n🌱 **pH સુધારણા:** એસિડિક માટી → ચૂનો, આલ્કલાઇન માટી → જિપ્સમ"
    },
    "government_schemes": {
        "en": "**Key Government Schemes for Farmers:**\n\n1. 🏛️ **PM-KISAN:** ₹6,000/year direct benefit transfer\n2. 🌾 **PM Fasal Bima Yojana:** Crop insurance at low premiums\n3. 🚰 **PM Krishi Sinchayee Yojana:** Irrigation support\n4. 💰 **Kisan Credit Card (KCC):** Low-interest crop loans\n5. 🌱 **National Mission on Sustainable Agriculture:** Climate adaptation\n6. 📋 **Soil Health Card Scheme:** Free soil testing\n7. 🏪 **e-NAM:** Electronic national agriculture market\n\nVisit your nearest agriculture office or https://agriculture.gov.in for details.",
        "hi": "**किसानों के लिए प्रमुख सरकारी योजनाएं:**\n\n1. 🏛️ **PM-KISAN:** ₹6,000/वर्ष प्रत्यक्ष लाभ\n2. 🌾 **PM फसल बीमा योजना:** कम प्रीमियम पर फसल बीमा\n3. 💰 **किसान क्रेडिट कार्ड:** कम ब्याज दर पर ऋण\n4. 📋 **मृदा स्वास्थ्य कार्ड:** मुफ्त मिट्टी परीक्षण",
        "gu": "**ખેડૂતો માટે મુખ્ય સરકારી યોજનાઓ:**\n\n1. 🏛️ **PM-KISAN:** ₹6,000/વર્ષ સીધું લાભ ટ્રાન્સફર\n2. 🌾 **PM ફસલ બીમા યોજના:** ઓછા પ્રીમિયમ પર પાક વીમો\n3. 🚰 **PM કૃષિ સિંચાઈ યોજના:** સિંચાઈ સહાય\n4. 💰 **કિસાન ક્રેડિટ કાર્ડ (KCC):** ઓછા વ્યાજના પાક લોન\n5. 📋 **માટી આરોગ્ય કાર્ડ:** મફત માટી પરીક્ષણ\n6. 🏪 **e-NAM:** ઇલેક્ટ્રોનિક રાષ્ટ્રીય કૃષિ બજાર\n\nવિગતો માટે agriculture.gov.in ની મુલાકાત લો."
    },
    "crop_info": {
        "en": "I can provide information about any crop! Here are some major crops:\n\n🌾 **Kharif (Monsoon):** Rice, Maize, Cotton, Sugarcane, Groundnut, Bajra\n❄️ **Rabi (Winter):** Wheat, Mustard, Gram, Barley, Lentil\n☀️ **Zaid (Summer):** Watermelon, Cucumber, Potato (some regions)\n\nAsk me about a specific crop and I'll tell you the ideal conditions!",
        "hi": "मैं किसी भी फसल के बारे में जानकारी दे सकता हूं!\n\n🌾 **खरीफ:** धान, मक्का, कपास, गन्ना, मूंगफली\n❄️ **रबी:** गेहूं, सरसों, चना, जौ, मसूर\n\nकिसी विशिष्ट फसल के बारे में पूछें!",
        "gu": "હું કોઈપણ પાક વિશે માહિતી આપી શકું!\n\n🌾 **ખરીફ (ચોમાસું):** ડાંગર, મકાઈ, કપાસ, શેરડી, મગફળી, બાજરી\n❄️ **રબી (શિયાળો):** ઘઉં, સરસવ, ચણા, જવ, મસૂર\n☀️ **ઝૈદ (ઉનાળો):** તરબૂચ, કાકડી\n\nકોઈ ચોક્કસ પાક વિશે પૂછો!"
    }
}


def _find_crop_info(query):
    """Look for crop name in query and return details."""
    query_lower = query.lower()
    for crop, conditions in CROP_CONDITIONS.items():
        if crop.lower() in query_lower:
            avg_yield = CROP_AVG_YIELDS.get(crop, "N/A")
            info = f"**{crop} — Growing Guide:**\n\n"
            info += f"🌡️ **Temperature:** {conditions['temp'][0]}-{conditions['temp'][1]}°C\n"
            info += f"💧 **Rainfall:** {conditions['rainfall'][0]}-{conditions['rainfall'][1]}mm\n"
            info += f"🧪 **pH Range:** {conditions['ph'][0]}-{conditions['ph'][1]}\n"
            info += f"🌱 **Best Season:** {', '.join(conditions['season'])}\n"
            info += f"🏔️ **Suitable Soil:** {', '.join(conditions['soil'])}\n"
            info += f"📊 **Avg Yield:** {avg_yield} tons/hectare\n\n"
            info += f"**NPK Requirements:**\n"
            info += f"- Nitrogen: {conditions['n'][0]}-{conditions['n'][1]} kg/ha\n"
            info += f"- Phosphorus: {conditions['p'][0]}-{conditions['p'][1]} kg/ha\n"
            info += f"- Potassium: {conditions['k'][0]}-{conditions['k'][1]} kg/ha"
            return info
    return None


def _find_state_info(query):
    """Check for state name in query and return info."""
    query_lower = query.lower()
    for state, info in STATES_DATA.items():
        if state.lower() in query_lower:
            climate = info["climate"]
            result = f"**{state} — Agricultural Profile:**\n\n"
            result += f"🌾 **Major Crops:** {', '.join(info['major_crops'])}\n"
            result += f"🏔️ **Soil Types:** {', '.join(info['soil_types'])}\n"
            result += f"🌡️ **Temperature:** {climate['temp_min']}-{climate['temp_max']}°C\n"
            result += f"💧 **Rainfall:** {climate['rainfall_min']}-{climate['rainfall_max']}mm\n"
            result += f"💦 **Humidity:** {climate['humidity_min']}-{climate['humidity_max']}%\n\n"
            result += f"**Districts:** {', '.join(info['districts'][:8])}..."
            return result
    return None


def get_chatbot_response(message: str, language: str = "en", context: dict = None):
    """Get chatbot response based on message content."""
    msg_lower = message.lower()

    # Check for keyword matches
    if any(kw in msg_lower for kw in ["npk", "nitrogen", "phosphorus", "potassium", "n p k"]):
        return KNOWLEDGE_BASE["npk"].get(language, KNOWLEDGE_BASE["npk"]["en"])

    if any(kw in msg_lower for kw in ["soil health card", "shc", "soil card", "soil test"]):
        return KNOWLEDGE_BASE["soil_health_card"].get(language, KNOWLEDGE_BASE["soil_health_card"]["en"])

    if any(kw in msg_lower for kw in ["ph", "acidic", "alkaline", "acidity"]):
        return KNOWLEDGE_BASE["ph"].get(language, KNOWLEDGE_BASE["ph"]["en"])

    if any(kw in msg_lower for kw in ["improve soil", "soil fertility", "fertilizer", "soil improvement", "improve my soil"]):
        return KNOWLEDGE_BASE["improve_soil"].get(language, KNOWLEDGE_BASE["improve_soil"]["en"])

    if any(kw in msg_lower for kw in ["scheme", "government", "subsidy", "pm kisan", "yojana", "loan"]):
        return KNOWLEDGE_BASE["government_schemes"].get(language, KNOWLEDGE_BASE["government_schemes"]["en"])

    if any(kw in msg_lower for kw in ["recommend", "why", "suggested", "why this crop"]):
        if context:
            return f"Based on your inputs — soil type: {context.get('soil_type', 'N/A')}, state: {context.get('state', 'N/A')}, the recommendation considers your specific soil nutrients, climate conditions, and historical yield patterns in your region. The AI model evaluated all suitable crops and ranked them by compatibility."
        return "To explain a recommendation, please first run a crop prediction from the Advisory page. The system considers your soil nutrients, climate conditions, and state-specific data."

    # Check for crop-specific query
    crop_info = _find_crop_info(message)
    if crop_info:
        return crop_info

    # Check for state-specific query
    state_info = _find_state_info(message)
    if state_info:
        return state_info

    if any(kw in msg_lower for kw in ["crop", "season", "kharif", "rabi", "zaid"]):
        return KNOWLEDGE_BASE["crop_info"].get(language, KNOWLEDGE_BASE["crop_info"]["en"])

    if any(kw in msg_lower for kw in ["hello", "hi", "hey", "namaste", "help", "kem cho", "kemcho"]):
        greetings = {
            "en": "🙏 **Namaste!** I am BharatAgri AI Assistant.\n\nI can help you with:\n- 🌱 **Crop information** — Ask about any crop\n- 🧪 **Soil guidance** — NPK, pH, soil health\n- 📊 **Recommendations** — Why a crop was suggested\n- 🏛️ **Government schemes** — Subsidies and support\n- 🗺️ **State info** — Regional agricultural data\n\nJust ask me anything about farming!",
            "hi": "🙏 **नमस्ते!** मैं भारतएग्री AI सहायक हूं।\n\nमैं आपकी इन विषयों में मदद कर सकता हूं:\n- 🌱 फसल जानकारी\n- 🧪 मिट्टी मार्गदर्शन\n- 📊 सिफारिशें\n- 🏛️ सरकारी योजनाएं\n\nखेती के बारे में कुछ भी पूछें!",
            "gu": "🙏 **કેમ છો!** હું ભારતએગ્રી AI સહાયક છું.\n\nહું તમને આ વિષયોમાં મદદ કરી શકું:\n- 🌱 **પાક માહિતી** — કોઈપણ પાક વિશે પૂછો\n- 🧪 **માટી માર્ગદર્શન** — NPK, pH, માટી આરોગ્ય\n- 📊 **ભલામણો** — પાક કેમ સૂચવ્યો\n- 🏛️ **સરકારી યોજનાઓ** — સબસિડી અને સહાય\n- 🗺️ **રાજ્ય માહિતી** — પ્રાદેશિક કૃષિ ડેટા\n\nખેતી વિશે કંઈપણ પૂછો!"
        }
        return greetings.get(language, greetings["en"])

    # Default response
    defaults = {
        "en": "I understand you're asking about farming. Here are some things I can help with:\n\n- Ask **\"What is NPK?\"** to learn about soil nutrients\n- Ask about any **crop name** (e.g., \"Tell me about Rice\")\n- Ask about any **state** (e.g., \"Maharashtra agriculture\")\n- Ask **\"How to improve soil?\"**\n- Ask about **\"Government schemes\"**\n\nTry asking a specific question!",
        "hi": "मैं समझता हूं कि आप खेती के बारे में पूछ रहे हैं। मैं इनमें मदद कर सकता हूं:\n\n- **\"NPK क्या है?\"** पूछें\n- किसी **फसल** के बारे में पूछें\n- **\"मिट्टी कैसे सुधारें?\"** पूछें\n- **\"सरकारी योजनाएं\"** के बारे में पूछें",
        "gu": "હું સમજું છું કે તમે ખેતી વિશે પૂછી રહ્યા છો. હું આમાં મદદ કરી શકું:\n\n- **\"NPK શું છે?\"** પૂછો\n- કોઈ **પાક** વિશે પૂછો (દા.ત. \"ડાંગર વિશે જણાવો\")\n- **\"માટી કેવી રીતે સુધારવી?\"** પૂછો\n- **\"સરકારી યોજનાઓ\"** વિશે પૂછો"
    }
    return defaults.get(language, defaults["en"])


@router.post("/message")
def chat(
    data: ChatMessage,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    response = get_chatbot_response(data.message, data.language, data.context)

    # Save to history
    chat_record = ChatHistory(
        user_id=current_user.id,
        message=data.message,
        response=response,
        language=data.language
    )
    db.add(chat_record)
    db.commit()

    return {"response": response}


@router.get("/history")
def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    history = db.query(ChatHistory).filter(
        ChatHistory.user_id == current_user.id
    ).order_by(ChatHistory.created_at.desc()).limit(50).all()

    return [
        {
            "id": h.id,
            "message": h.message,
            "response": h.response,
            "language": h.language,
            "created_at": h.created_at.isoformat()
        }
        for h in history
    ]
