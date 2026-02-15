/**
 * BharatAgri AI — Internationalization (i18n)
 * Supports 7 languages: English, Hindi, Punjabi, Marathi, Telugu, Tamil, Bengali
 */
const translations = {
    en: {
        // Nav
        home: "Home", advisory: "Advisory", dashboard: "Dashboard", chatbot: "Chatbot",
        login: "Login", signup: "Sign Up", logout: "Logout", profile: "Profile",
        // Hero
        hero_badge: "🇮🇳 AI-Powered Agriculture Platform",
        hero_title: "Intelligent Crop & Yield Advisory for Indian Farmers",
        hero_subtitle: "Get region-specific crop recommendations, yield predictions, and risk analysis powered by AI — tailored to your state, soil, and climate conditions.",
        get_started: "Get Started", learn_more: "Learn More",
        // Features
        feat_crop_title: "Smart Crop Recommendation",
        feat_crop_desc: "AI suggests the best crops for your specific soil nutrients, climate, and region.",
        feat_yield_title: "Yield Prediction",
        feat_yield_desc: "Predict expected harvest output with state-level accuracy using ML models.",
        feat_risk_title: "Risk Analysis",
        feat_risk_desc: "Understand potential risks from climate deviation, soil gaps, and seasonal factors.",
        feat_multi_title: "Multilingual Support",
        feat_multi_desc: "Available in 7 Indian languages to serve farmers across the nation.",
        feat_chat_title: "AI Chatbot",
        feat_chat_desc: "Ask questions about crops, soil health, government schemes, and farming tips.",
        feat_data_title: "State-wise Data",
        feat_data_desc: "Covers 16 states with district-level soil and climate intelligence.",
        // Stats
        stat_states: "States Covered", stat_crops: "Crops Analyzed", stat_models: "AI Models",
        // Advisory
        advisory_title: "Crop & Yield Advisory",
        advisory_sub: "Enter your soil and location details to get personalized crop recommendations.",
        select_state: "Select State", select_district: "Select District", select_soil: "Select Soil Type",
        select_season: "Select Season",
        nitrogen: "Nitrogen (N)", phosphorus: "Phosphorus (P)", potassium: "Potassium (K)",
        temperature: "Temperature (°C)", humidity: "Humidity (%)", ph_level: "pH Level",
        rainfall: "Rainfall (mm)", area: "Area (hectares)",
        analyze: "🔍 Analyze & Recommend", analyzing: "Analyzing...",
        // Help texts
        help_n: "Amount of Nitrogen in soil (kg/ha). According to your health card",
        help_p: "Amount of phosphorus in soil (kg/ha). Essential for root growth.",
        help_k: "Amount of potassium in soil (kg/ha). Helps plant immunity.",
        help_ph: "Soil pH (0-14). Most crops need 6.0-7.5. Check Soil Health Card.",
        help_temp: "Average temperature in your area during the growing season.",
        help_humidity: "Average relative humidity (%). Higher in coastal areas.",
        help_rainfall: "Annual rainfall in mm. Auto-filled based on your state selection.",
        help_area: "Farm area in hectares (1 hectare = 2.47 acres).",
        what_is_this: "What is this?",
        // Results
        crop_recommendations: "Crop Recommendations",
        yield_prediction: "Yield Prediction",
        risk_analysis: "Risk Analysis",
        feature_importance: "Feature Importance",
        predicted_yield: "Predicted Yield",
        state_average: "State Average",
        explanation: "AI Explanation",
        // Climate simulation
        climate_sim: "🌡️ Climate Simulation",
        climate_sim_desc: "Adjust sliders to simulate climate change effects on recommendations.",
        rainfall_change: "Rainfall Change",
        temp_change: "Temperature Change",
        recalculate: "Recalculate",
        // Dashboard
        dashboard_title: "Your Dashboard",
        dashboard_sub: "Track your prediction history and compare yields.",
        recent_predictions: "Recent Predictions",
        yield_comparison: "Yield Comparison",
        no_history: "No predictions yet. Go to Advisory to get your first recommendation!",
        date: "Date", type: "Type", state: "State", result: "Result",
        // Chatbot
        chat_title: "Agricultural Assistant",
        chat_sub: "Ask me anything about farming, crops, soil health, or government schemes.",
        chat_placeholder: "Type your question here...",
        send: "Send",
        // Auth
        login_title: "Welcome Back",
        login_sub: "Sign in to access your personalized dashboard.",
        register_title: "Create Account",
        register_sub: "Join BharatAgri AI for smart farming insights.",
        email: "Email Address", password: "Password", name: "Full Name",
        dont_have_account: "Don't have an account?", already_have_account: "Already have an account?",
        // Loading
        loading: "Analyzing your data...",
        // Profile
        profile_title: "Your Profile",
        save_changes: "Save Changes",
        preferred_language: "Preferred Language",
    },
    hi: {
        home: "होम", advisory: "सलाह", dashboard: "डैशबोर्ड", chatbot: "चैटबॉट",
        login: "लॉगिन", signup: "साइन अप", logout: "लॉगआउट", profile: "प्रोफ़ाइल",
        hero_badge: "🇮🇳 AI-संचालित कृषि मंच",
        hero_title: "भारतीय किसानों के लिए बुद्धिमान फसल और उपज सलाह",
        hero_subtitle: "AI द्वारा संचालित क्षेत्र-विशिष्ट फसल सिफारिशें, उपज पूर्वानुमान और जोखिम विश्लेषण प्राप्त करें।",
        get_started: "शुरू करें", learn_more: "और जानें",
        feat_crop_title: "स्मार्ट फसल सिफारिश", feat_crop_desc: "AI आपकी मिट्टी, जलवायु और क्षेत्र के लिए सर्वोत्तम फसलों का सुझाव देता है।",
        feat_yield_title: "उपज पूर्वानुमान", feat_yield_desc: "ML मॉडल का उपयोग करके अपेक्षित फसल उत्पादन की भविष्यवाणी करें।",
        feat_risk_title: "जोखिम विश्लेषण", feat_risk_desc: "जलवायु विचलन और मिट्टी की कमियों से संभावित जोखिमों को समझें।",
        feat_multi_title: "बहुभाषी सहायता", feat_multi_desc: "देश भर के किसानों के लिए 7 भारतीय भाषाओं में उपलब्ध।",
        feat_chat_title: "AI चैटबॉट", feat_chat_desc: "फसलों, मिट्टी, सरकारी योजनाओं के बारे में प्रश्न पूछें।",
        feat_data_title: "राज्यवार डेटा", feat_data_desc: "जिला-स्तरीय मिट्टी और जलवायु जानकारी के साथ 16 राज्य।",
        stat_states: "राज्य", stat_crops: "फसलें", stat_models: "AI मॉडल",
        advisory_title: "फसल और उपज सलाह",
        advisory_sub: "व्यक्तिगत फसल सिफारिशें प्राप्त करने के लिए अपनी मिट्टी और स्थान का विवरण दर्ज करें।",
        select_state: "राज्य चुनें", select_district: "जिला चुनें", select_soil: "मिट्टी का प्रकार", select_season: "मौसम चुनें",
        nitrogen: "नाइट्रोजन (N)", phosphorus: "फॉस्फोरस (P)", potassium: "पोटेशियम (K)",
        temperature: "तापमान (°C)", humidity: "आर्द्रता (%)", ph_level: "pH स्तर",
        rainfall: "वर्षा (मिमी)", area: "क्षेत्र (हेक्टेयर)",
        analyze: "🔍 विश्लेषण करें", analyzing: "विश्लेषण हो रहा है...",
        what_is_this: "यह क्या है?",
        crop_recommendations: "फसल सिफारिशें", yield_prediction: "उपज पूर्वानुमान",
        risk_analysis: "जोखिम विश्लेषण", feature_importance: "सुविधा महत्व",
        predicted_yield: "अनुमानित उपज", state_average: "राज्य औसत", explanation: "AI व्याख्या",
        climate_sim: "🌡️ जलवायु सिमुलेशन",
        dashboard_title: "आपका डैशबोर्ड", recent_predictions: "हाल की भविष्यवाणियां",
        chat_title: "कृषि सहायक", chat_placeholder: "अपना प्रश्न यहाँ टाइप करें...", send: "भेजें",
        login_title: "स्वागत है", register_title: "खाता बनाएं",
        email: "ईमेल", password: "पासवर्ड", name: "पूरा नाम",
        loading: "आपके डेटा का विश्लेषण किया जा रहा है...",
        profile_title: "आपकी प्रोफ़ाइल", save_changes: "परिवर्तन सहेजें",
    },
    pa: {
        home: "ਘਰ", advisory: "ਸਲਾਹ", dashboard: "ਡੈਸ਼ਬੋਰਡ", chatbot: "ਚੈਟਬੋਟ",
        login: "ਲੌਗਇਨ", signup: "ਸਾਈਨ ਅੱਪ", logout: "ਲੌਗਆਊਟ",
        hero_title: "ਭਾਰਤੀ ਕਿਸਾਨਾਂ ਲਈ ਬੁੱਧੀਮਾਨ ਫ਼ਸਲ ਤੇ ਝਾੜ ਸਲਾਹ",
        get_started: "ਸ਼ੁਰੂ ਕਰੋ", analyze: "🔍 ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ",
        select_state: "ਰਾਜ ਚੁਣੋ", select_district: "ਜ਼ਿਲ੍ਹਾ ਚੁਣੋ",
        chat_placeholder: "ਆਪਣਾ ਸਵਾਲ ਇੱਥੇ ਟਾਈਪ ਕਰੋ...", send: "ਭੇਜੋ",
        loading: "ਤੁਹਾਡੇ ਡੇਟਾ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
    },
    mr: {
        home: "मुख्यपृष्ठ", advisory: "सल्ला", dashboard: "डॅशबोर्ड", chatbot: "चॅटबॉट",
        login: "लॉगिन", signup: "साइन अप", logout: "लॉगआउट",
        hero_title: "भारतीय शेतकऱ्यांसाठी बुद्धिमान पीक आणि उत्पादन सल्ला",
        get_started: "सुरू करा", analyze: "🔍 विश्लेषण करा",
        select_state: "राज्य निवडा", select_district: "जिल्हा निवडा",
        chat_placeholder: "तुमचा प्रश्न इथे टाइप करा...", send: "पाठवा",
        loading: "तुमच्या डेटाचे विश्लेषण केले जात आहे...",
    },
    te: {
        home: "హోమ్", advisory: "సలహా", dashboard: "డాష్‌బోర్డ్", chatbot: "చాట్‌బాట్",
        login: "లాగిన్", signup: "సైన్ అప్", logout: "లాగౌట్",
        hero_title: "భారతీయ రైతులకు తెలివైన పంట మరియు దిగుబడి సలహా",
        get_started: "ప్రారంభించండి", analyze: "🔍 విశ్లేషించండి",
        select_state: "రాష్ట్రం ఎంచుకోండి", select_district: "జిల్లా ఎంచుకోండి",
        chat_placeholder: "మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...", send: "పంపండి",
        loading: "మీ డేటా విశ్లేషించబడుతోంది...",
    },
    ta: {
        home: "முகப்பு", advisory: "ஆலோசனை", dashboard: "டாஷ்போர்டு", chatbot: "சாட்போட்",
        login: "உள்நுழை", signup: "பதிவு", logout: "வெளியேறு",
        hero_title: "இந்திய விவசாயிகளுக்கான அறிவார்ந்த பயிர் மற்றும் விளைச்சல் ஆலோசனை",
        get_started: "தொடங்குங்கள்", analyze: "🔍 பகுப்பாய்வு செய்",
        select_state: "மாநிலம் தேர்வு", select_district: "மாவட்டம் தேர்வு",
        chat_placeholder: "உங்கள் கேள்வியை இங்கே தட்டச்சு செய்யுங்கள்...", send: "அனுப்பு",
        loading: "உங்கள் தரவு பகுப்பாய்வு செய்யப்படுகிறது...",
    },
    bn: {
        home: "হোম", advisory: "পরামর্শ", dashboard: "ড্যাশবোর্ড", chatbot: "চ্যাটবট",
        login: "লগইন", signup: "সাইন আপ", logout: "লগআউট",
        hero_title: "ভারতীয় কৃষকদের জন্য বুদ্ধিমান ফসল ও ফলন পরামর্শ",
        get_started: "শুরু করুন", analyze: "🔍 বিশ্লেষণ করুন",
        select_state: "রাজ্য নির্বাচন", select_district: "জেলা নির্বাচন",
        chat_placeholder: "আপনার প্রশ্ন এখানে টাইপ করুন...", send: "পাঠান",
        loading: "আপনার ডেটা বিশ্লেষণ করা হচ্ছে...",
    },
    gu: {
        home: "હોમ", advisory: "સલાહ", dashboard: "ડેશબોર્ડ", chatbot: "ચેટબોટ",
        login: "લૉગિન", signup: "સાઇન અપ", logout: "લૉગઆઉટ", profile: "પ્રોફાઇલ",
        hero_badge: "🇮🇳 AI-સંચાલિત કૃષિ મંચ",
        hero_title: "ભારતીય ખેડૂતો માટે બુદ્ધિશાળી પાક અને ઉપજ સલાહ",
        hero_subtitle: "AI દ્વારા સંચાલિત પ્રદેશ-વિશિષ્ટ પાક ભલામણો, ઉપજ આગાહી અને જોખમ વિશ્લેષણ મેળવો.",
        get_started: "શરૂ કરો", learn_more: "વધુ જાણો",
        feat_crop_title: "સ્માર્ટ પાક ભલામણ", feat_crop_desc: "AI તમારી માટી, આબોહવા અને પ્રદેશ માટે શ્રેષ્ઠ પાકોનું સૂચન કરે છે.",
        feat_yield_title: "ઉપજ આગાહી", feat_yield_desc: "ML મોડેલનો ઉપયોગ કરીને અપેક્ષિત પાક ઉત્પાદનની આગાહી કરો.",
        feat_risk_title: "જોખમ વિશ્લેષણ", feat_risk_desc: "આબોહવા વિચલન અને માટીની ખામીઓથી સંભવિત જોખમોને સમજો.",
        feat_multi_title: "બહુભાષી સહાય", feat_multi_desc: "દેશભરના ખેડૂતો માટે ભારતીય ભાષાઓમાં ઉપલબ્ધ.",
        feat_chat_title: "AI ચેટબોટ", feat_chat_desc: "પાક, માટી, સરકારી યોજનાઓ વિશે પ્રશ્નો પૂછો.",
        feat_data_title: "રાજ્યવાર ડેટા", feat_data_desc: "જિલ્લા-સ્તરની માટી અને આબોહવા માહિતી સાથે 16 રાજ્યો.",
        stat_states: "રાજ્યો", stat_crops: "પાક", stat_models: "AI મોડેલ",
        advisory_title: "પાક અને ઉપજ સલાહ",
        advisory_sub: "વ્યક્તિગત પાક ભલામણો મેળવવા માટે તમારી માટી અને સ્થાનની વિગતો દાખલ કરો.",
        select_state: "રાજ્ય પસંદ કરો", select_district: "જિલ્લો પસંદ કરો",
        select_soil: "માટીનો પ્રકાર", select_season: "ઋતુ પસંદ કરો",
        nitrogen: "નાઇટ્રોજન (N)", phosphorus: "ફોસ્ફરસ (P)", potassium: "પોટેશિયમ (K)",
        temperature: "તાપમાન (°C)", humidity: "ભેજ (%)", ph_level: "pH સ્તર",
        rainfall: "વરસાદ (મિમી)", area: "વિસ્તાર (હેક્ટર)",
        analyze: "🔍 વિશ્લેષણ કરો", analyzing: "વિશ્લેષણ થઈ રહ્યું છે...",
        what_is_this: "આ શું છે?",
        crop_recommendations: "પાક ભલામણો", yield_prediction: "ઉપજ આગાહી",
        risk_analysis: "જોખમ વિશ્લેષણ", feature_importance: "ફીચર મહત્વ",
        predicted_yield: "અનુમાનિત ઉપજ", state_average: "રાજ્ય સરેરાશ", explanation: "AI સમજૂતી",
        climate_sim: "🌡️ આબોહવા સિમ્યુલેશન",
        dashboard_title: "તમારું ડેશબોર્ડ", recent_predictions: "તાજેતરની આગાહીઓ",
        chat_title: "કૃષિ સહાયક", chat_placeholder: "તમારો પ્રશ્ન અહીં ટાઈપ કરો...", send: "મોકલો",
        login_title: "સ્વાગત છે", register_title: "ખાતું બનાવો",
        email: "ઈમેલ", password: "પાસવર્ડ", name: "પૂરું નામ",
        loading: "તમારા ડેટાનું વિશ્લેષણ કરવામાં આવી રહ્યું છે...",
        profile_title: "તમારી પ્રોફાઇલ", save_changes: "ફેરફારો સાચવો",
    }
};

let currentLang = 'en';

function t(key) {
    const lang = translations[currentLang] || translations.en;
    return lang[key] || translations.en[key] || key;
}

function changeLanguage(lang) {
    currentLang = lang;
    document.getElementById('langSelect').value = lang;
    // Switch body font class for proper Indic script rendering
    document.body.className = document.body.className.replace(/lang-\w+/g, '');
    document.body.classList.add('lang-' + lang);
    document.documentElement.lang = lang;
    // Re-render current page
    if (typeof renderCurrentPage === 'function') {
        renderCurrentPage();
    }
    // Update nav links text
    updateNavText();
}

function updateNavText() {
    const links = document.querySelectorAll('.nav-link');
    const pages = ['home', 'recommend', 'dashboard', 'chatbot'];
    const keys = ['home', 'advisory', 'dashboard', 'chatbot'];
    links.forEach((link, i) => {
        if (keys[i]) link.textContent = t(keys[i]);
    });
}
