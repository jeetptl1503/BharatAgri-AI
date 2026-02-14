"""
India state-wise agricultural reference data.
Contains soil types, climate ranges, districts, and crop suitability for major Indian states.
"""

STATES_DATA = {
    "Andhra Pradesh": {
        "districts": ["Anantapur", "Chittoor", "East Godavari", "Guntur", "Krishna",
                       "Kurnool", "Nellore", "Prakasam", "Srikakulam", "Visakhapatnam",
                       "West Godavari", "YSR Kadapa"],
        "soil_types": ["Black", "Red", "Alluvial", "Laterite"],
        "climate": {"temp_min": 22, "temp_max": 38, "rainfall_min": 600, "rainfall_max": 1200,
                    "humidity_min": 55, "humidity_max": 85},
        "major_crops": ["Rice", "Cotton", "Sugarcane", "Groundnut", "Tobacco", "Chilli"]
    },
    "Assam": {
        "districts": ["Barpeta", "Darrang", "Dibrugarh", "Goalpara", "Jorhat",
                       "Kamrup", "Karbi Anglong", "Lakhimpur", "Nagaon", "Sivasagar",
                       "Sonitpur", "Tinsukia"],
        "soil_types": ["Alluvial", "Laterite", "Red"],
        "climate": {"temp_min": 12, "temp_max": 35, "rainfall_min": 1500, "rainfall_max": 3000,
                    "humidity_min": 70, "humidity_max": 95},
        "major_crops": ["Rice", "Tea", "Jute", "Sugarcane", "Potato", "Banana"]
    },
    "Bihar": {
        "districts": ["Bhagalpur", "Darbhanga", "Gaya", "Muzaffarpur", "Patna",
                       "Purnia", "Saharsa", "Saran", "Vaishali", "Nalanda",
                       "Begusarai", "Munger"],
        "soil_types": ["Alluvial", "Sandy", "Clay"],
        "climate": {"temp_min": 10, "temp_max": 42, "rainfall_min": 1000, "rainfall_max": 1600,
                    "humidity_min": 40, "humidity_max": 85},
        "major_crops": ["Rice", "Wheat", "Maize", "Lentil", "Sugarcane", "Potato"]
    },
    "Gujarat": {
        "districts": ["Ahmedabad", "Amreli", "Banaskantha", "Bharuch", "Bhavnagar",
                       "Junagadh", "Kutch", "Mehsana", "Rajkot", "Surat",
                       "Vadodara", "Valsad"],
        "soil_types": ["Black", "Alluvial", "Sandy", "Saline"],
        "climate": {"temp_min": 15, "temp_max": 43, "rainfall_min": 300, "rainfall_max": 1500,
                    "humidity_min": 30, "humidity_max": 80},
        "major_crops": ["Cotton", "Groundnut", "Wheat", "Rice", "Tobacco", "Bajra"]
    },
    "Haryana": {
        "districts": ["Ambala", "Bhiwani", "Faridabad", "Gurugram", "Hisar",
                       "Jhajjar", "Karnal", "Kurukshetra", "Panipat", "Rohtak",
                       "Sirsa", "Sonipat"],
        "soil_types": ["Alluvial", "Sandy", "Clay"],
        "climate": {"temp_min": 5, "temp_max": 45, "rainfall_min": 300, "rainfall_max": 800,
                    "humidity_min": 30, "humidity_max": 75},
        "major_crops": ["Wheat", "Rice", "Sugarcane", "Cotton", "Mustard", "Bajra"]
    },
    "Karnataka": {
        "districts": ["Bangalore Rural", "Bangalore Urban", "Belgaum", "Bellary",
                       "Bidar", "Dakshina Kannada", "Dharwad", "Gulbarga",
                       "Hassan", "Mandya", "Mysore", "Shimoga"],
        "soil_types": ["Red", "Black", "Laterite", "Alluvial"],
        "climate": {"temp_min": 18, "temp_max": 38, "rainfall_min": 500, "rainfall_max": 3500,
                    "humidity_min": 45, "humidity_max": 85},
        "major_crops": ["Rice", "Ragi", "Jowar", "Cotton", "Sugarcane", "Coffee"]
    },
    "Kerala": {
        "districts": ["Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod",
                       "Kollam", "Kottayam", "Kozhikode", "Malappuram", "Palakkad",
                       "Thiruvananthapuram", "Thrissur"],
        "soil_types": ["Laterite", "Alluvial", "Red", "Sandy"],
        "climate": {"temp_min": 22, "temp_max": 36, "rainfall_min": 1500, "rainfall_max": 4000,
                    "humidity_min": 70, "humidity_max": 95},
        "major_crops": ["Rice", "Coconut", "Rubber", "Tea", "Coffee", "Banana"]
    },
    "Madhya Pradesh": {
        "districts": ["Bhopal", "Gwalior", "Indore", "Jabalpur", "Rewa",
                       "Sagar", "Satna", "Ujjain", "Vidisha", "Hoshangabad",
                       "Chhindwara", "Dewas"],
        "soil_types": ["Black", "Red", "Alluvial", "Laterite"],
        "climate": {"temp_min": 10, "temp_max": 45, "rainfall_min": 800, "rainfall_max": 1600,
                    "humidity_min": 30, "humidity_max": 80},
        "major_crops": ["Wheat", "Soybean", "Rice", "Gram", "Cotton", "Sugarcane"]
    },
    "Maharashtra": {
        "districts": ["Ahmednagar", "Aurangabad", "Kolhapur", "Mumbai", "Nagpur",
                       "Nashik", "Pune", "Ratnagiri", "Sangli", "Satara",
                       "Solapur", "Thane"],
        "soil_types": ["Black", "Red", "Laterite", "Alluvial"],
        "climate": {"temp_min": 15, "temp_max": 42, "rainfall_min": 500, "rainfall_max": 3000,
                    "humidity_min": 35, "humidity_max": 85},
        "major_crops": ["Rice", "Sugarcane", "Cotton", "Soybean", "Jowar", "Groundnut"]
    },
    "Odisha": {
        "districts": ["Balasore", "Cuttack", "Ganjam", "Kalahandi", "Kendrapara",
                       "Khurda", "Koraput", "Mayurbhanj", "Puri", "Sambalpur",
                       "Sundargarh", "Bhadrak"],
        "soil_types": ["Alluvial", "Red", "Laterite", "Black"],
        "climate": {"temp_min": 15, "temp_max": 40, "rainfall_min": 1200, "rainfall_max": 1800,
                    "humidity_min": 55, "humidity_max": 90},
        "major_crops": ["Rice", "Groundnut", "Sugarcane", "Jute", "Sesame", "Turmeric"]
    },
    "Punjab": {
        "districts": ["Amritsar", "Bathinda", "Faridkot", "Ferozepur", "Gurdaspur",
                       "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana", "Moga",
                       "Patiala", "Sangrur"],
        "soil_types": ["Alluvial", "Sandy", "Clay"],
        "climate": {"temp_min": 2, "temp_max": 45, "rainfall_min": 400, "rainfall_max": 900,
                    "humidity_min": 30, "humidity_max": 75},
        "major_crops": ["Wheat", "Rice", "Cotton", "Sugarcane", "Maize", "Potato"]
    },
    "Rajasthan": {
        "districts": ["Ajmer", "Alwar", "Barmer", "Bikaner", "Jaipur",
                       "Jodhpur", "Kota", "Nagaur", "Udaipur", "Sikar",
                       "Chittorgarh", "Bhilwara"],
        "soil_types": ["Sandy", "Alluvial", "Red", "Saline"],
        "climate": {"temp_min": 5, "temp_max": 48, "rainfall_min": 100, "rainfall_max": 800,
                    "humidity_min": 15, "humidity_max": 60},
        "major_crops": ["Wheat", "Bajra", "Mustard", "Gram", "Barley", "Maize"]
    },
    "Tamil Nadu": {
        "districts": ["Chennai", "Coimbatore", "Cuddalore", "Dindigul", "Erode",
                       "Kancheepuram", "Madurai", "Nagapattinam", "Salem", "Thanjavur",
                       "Tiruchirappalli", "Tirunelveli"],
        "soil_types": ["Red", "Black", "Alluvial", "Laterite", "Sandy"],
        "climate": {"temp_min": 20, "temp_max": 40, "rainfall_min": 600, "rainfall_max": 1500,
                    "humidity_min": 55, "humidity_max": 85},
        "major_crops": ["Rice", "Sugarcane", "Cotton", "Groundnut", "Banana", "Coconut"]
    },
    "Telangana": {
        "districts": ["Adilabad", "Hyderabad", "Karimnagar", "Khammam", "Mahabubnagar",
                       "Medak", "Nalgonda", "Nizamabad", "Rangareddy", "Warangal",
                       "Sangareddy", "Siddipet"],
        "soil_types": ["Black", "Red", "Alluvial", "Laterite"],
        "climate": {"temp_min": 18, "temp_max": 42, "rainfall_min": 700, "rainfall_max": 1200,
                    "humidity_min": 40, "humidity_max": 80},
        "major_crops": ["Rice", "Cotton", "Maize", "Sugarcane", "Turmeric", "Chilli"]
    },
    "Uttar Pradesh": {
        "districts": ["Agra", "Allahabad", "Bareilly", "Gorakhpur", "Jhansi",
                       "Kanpur", "Lucknow", "Mathura", "Meerut", "Varanasi",
                       "Moradabad", "Saharanpur"],
        "soil_types": ["Alluvial", "Sandy", "Clay", "Black"],
        "climate": {"temp_min": 5, "temp_max": 45, "rainfall_min": 600, "rainfall_max": 1200,
                    "humidity_min": 30, "humidity_max": 80},
        "major_crops": ["Wheat", "Rice", "Sugarcane", "Potato", "Mustard", "Gram"]
    },
    "West Bengal": {
        "districts": ["Bankura", "Bardhaman", "Birbhum", "Darjeeling", "Hooghly",
                       "Howrah", "Jalpaiguri", "Kolkata", "Malda", "Midnapore",
                       "Murshidabad", "Nadia"],
        "soil_types": ["Alluvial", "Red", "Laterite", "Sandy"],
        "climate": {"temp_min": 10, "temp_max": 40, "rainfall_min": 1200, "rainfall_max": 2500,
                    "humidity_min": 55, "humidity_max": 90},
        "major_crops": ["Rice", "Jute", "Tea", "Potato", "Wheat", "Mustard"]
    }
}

SOIL_TYPES = ["Alluvial", "Black", "Red", "Laterite", "Sandy", "Clay", "Saline"]

SOIL_CHARACTERISTICS = {
    "Alluvial": {"n_range": (200, 350), "p_range": (15, 40), "k_range": (150, 300), "ph_range": (6.5, 8.0), "description": "Found in river plains, very fertile, good water retention"},
    "Black": {"n_range": (150, 280), "p_range": (10, 30), "k_range": (200, 350), "ph_range": (7.0, 8.5), "description": "Rich in iron, lime, calcium, good moisture retention"},
    "Red": {"n_range": (100, 220), "p_range": (8, 25), "k_range": (100, 250), "ph_range": (5.5, 7.0), "description": "Rich in iron oxides, poor in nitrogen and phosphorus"},
    "Laterite": {"n_range": (80, 180), "p_range": (5, 20), "k_range": (80, 200), "ph_range": (5.0, 6.5), "description": "Acidic, rich in iron and aluminium, low fertility"},
    "Sandy": {"n_range": (50, 150), "p_range": (5, 15), "k_range": (50, 150), "ph_range": (5.5, 7.5), "description": "Low water retention, well-drained, low nutrient content"},
    "Clay": {"n_range": (180, 320), "p_range": (12, 35), "k_range": (180, 300), "ph_range": (6.0, 8.0), "description": "Heavy, high water retention, rich in nutrients"},
    "Saline": {"n_range": (60, 140), "p_range": (5, 15), "k_range": (80, 200), "ph_range": (8.0, 9.5), "description": "High salt content, found in arid regions, limited crop suitability"}
}

SEASONS = ["Kharif", "Rabi", "Zaid"]

ALL_CROPS = [
    "Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Jute",
    "Groundnut", "Soybean", "Mustard", "Gram", "Lentil",
    "Potato", "Banana", "Coconut", "Coffee", "Tea",
    "Tobacco", "Chilli", "Turmeric", "Bajra", "Jowar",
    "Ragi", "Barley", "Sesame", "Rubber"
]

# Optimal growing conditions for each crop
CROP_CONDITIONS = {
    "Rice": {"n": (60, 120), "p": (20, 60), "k": (20, 60), "temp": (22, 35), "humidity": (70, 95), "ph": (5.5, 7.0), "rainfall": (1000, 2500), "season": ["Kharif"], "soil": ["Alluvial", "Clay", "Black"]},
    "Wheat": {"n": (80, 140), "p": (30, 70), "k": (20, 50), "temp": (10, 25), "humidity": (30, 65), "ph": (6.0, 7.5), "rainfall": (400, 800), "season": ["Rabi"], "soil": ["Alluvial", "Clay", "Black"]},
    "Maize": {"n": (60, 120), "p": (30, 70), "k": (20, 50), "temp": (18, 32), "humidity": (50, 80), "ph": (5.5, 7.5), "rainfall": (500, 1200), "season": ["Kharif", "Rabi"], "soil": ["Alluvial", "Red", "Black"]},
    "Sugarcane": {"n": (80, 150), "p": (20, 60), "k": (30, 70), "temp": (25, 38), "humidity": (60, 90), "ph": (6.0, 8.0), "rainfall": (800, 2000), "season": ["Kharif"], "soil": ["Alluvial", "Black", "Clay"]},
    "Cotton": {"n": (40, 100), "p": (20, 50), "k": (15, 45), "temp": (25, 40), "humidity": (40, 70), "ph": (6.0, 8.0), "rainfall": (500, 1200), "season": ["Kharif"], "soil": ["Black", "Alluvial", "Red"]},
    "Jute": {"n": (60, 120), "p": (20, 50), "k": (20, 50), "temp": (25, 37), "humidity": (70, 95), "ph": (5.5, 7.0), "rainfall": (1200, 2500), "season": ["Kharif"], "soil": ["Alluvial", "Clay"]},
    "Groundnut": {"n": (20, 60), "p": (30, 70), "k": (20, 50), "temp": (22, 35), "humidity": (50, 75), "ph": (5.5, 7.0), "rainfall": (400, 900), "season": ["Kharif", "Rabi"], "soil": ["Sandy", "Red", "Alluvial"]},
    "Soybean": {"n": (20, 80), "p": (30, 70), "k": (20, 60), "temp": (20, 35), "humidity": (50, 80), "ph": (5.5, 7.0), "rainfall": (600, 1200), "season": ["Kharif"], "soil": ["Black", "Alluvial", "Red"]},
    "Mustard": {"n": (40, 100), "p": (20, 50), "k": (15, 40), "temp": (10, 25), "humidity": (30, 60), "ph": (6.0, 7.5), "rainfall": (300, 600), "season": ["Rabi"], "soil": ["Alluvial", "Sandy", "Clay"]},
    "Gram": {"n": (15, 50), "p": (30, 70), "k": (15, 40), "temp": (15, 30), "humidity": (30, 60), "ph": (6.0, 8.0), "rainfall": (300, 700), "season": ["Rabi"], "soil": ["Black", "Alluvial", "Sandy"]},
    "Lentil": {"n": (15, 50), "p": (20, 55), "k": (15, 40), "temp": (12, 28), "humidity": (35, 65), "ph": (6.0, 7.5), "rainfall": (300, 600), "season": ["Rabi"], "soil": ["Alluvial", "Clay", "Black"]},
    "Potato": {"n": (80, 150), "p": (40, 80), "k": (40, 80), "temp": (12, 24), "humidity": (60, 80), "ph": (5.0, 6.5), "rainfall": (500, 1000), "season": ["Rabi", "Zaid"], "soil": ["Alluvial", "Sandy", "Red"]},
    "Banana": {"n": (80, 140), "p": (20, 60), "k": (40, 80), "temp": (25, 35), "humidity": (70, 90), "ph": (6.0, 7.5), "rainfall": (800, 2000), "season": ["Kharif", "Zaid"], "soil": ["Alluvial", "Clay", "Red"]},
    "Coconut": {"n": (30, 80), "p": (15, 45), "k": (50, 100), "temp": (25, 35), "humidity": (70, 95), "ph": (5.5, 7.0), "rainfall": (1000, 3000), "season": ["Kharif"], "soil": ["Laterite", "Alluvial", "Sandy"]},
    "Coffee": {"n": (40, 100), "p": (15, 40), "k": (30, 70), "temp": (18, 28), "humidity": (70, 90), "ph": (5.0, 6.5), "rainfall": (1200, 2500), "season": ["Kharif"], "soil": ["Laterite", "Red"]},
    "Tea": {"n": (40, 100), "p": (10, 35), "k": (20, 60), "temp": (15, 28), "humidity": (75, 95), "ph": (4.5, 6.0), "rainfall": (1500, 3500), "season": ["Kharif"], "soil": ["Laterite", "Red", "Alluvial"]},
    "Tobacco": {"n": (40, 100), "p": (20, 50), "k": (30, 70), "temp": (20, 35), "humidity": (50, 75), "ph": (5.5, 7.5), "rainfall": (500, 1200), "season": ["Kharif", "Rabi"], "soil": ["Black", "Red", "Alluvial"]},
    "Chilli": {"n": (60, 120), "p": (30, 60), "k": (25, 55), "temp": (20, 35), "humidity": (55, 80), "ph": (6.0, 7.5), "rainfall": (500, 1200), "season": ["Kharif", "Rabi"], "soil": ["Black", "Red", "Alluvial"]},
    "Turmeric": {"n": (60, 120), "p": (20, 50), "k": (40, 80), "temp": (22, 35), "humidity": (65, 90), "ph": (5.5, 7.0), "rainfall": (800, 1800), "season": ["Kharif"], "soil": ["Alluvial", "Red", "Clay"]},
    "Bajra": {"n": (30, 80), "p": (15, 40), "k": (15, 40), "temp": (25, 40), "humidity": (25, 55), "ph": (6.5, 8.0), "rainfall": (200, 600), "season": ["Kharif"], "soil": ["Sandy", "Alluvial", "Red"]},
    "Jowar": {"n": (30, 80), "p": (15, 45), "k": (15, 40), "temp": (25, 38), "humidity": (30, 65), "ph": (6.0, 8.0), "rainfall": (300, 800), "season": ["Kharif", "Rabi"], "soil": ["Black", "Red", "Alluvial"]},
    "Ragi": {"n": (30, 70), "p": (15, 40), "k": (15, 40), "temp": (20, 32), "humidity": (50, 80), "ph": (5.0, 7.0), "rainfall": (500, 1200), "season": ["Kharif"], "soil": ["Red", "Laterite", "Sandy"]},
    "Barley": {"n": (40, 90), "p": (20, 50), "k": (15, 40), "temp": (8, 22), "humidity": (30, 60), "ph": (6.5, 8.0), "rainfall": (300, 600), "season": ["Rabi"], "soil": ["Alluvial", "Sandy", "Clay"]},
    "Sesame": {"n": (20, 60), "p": (15, 40), "k": (15, 40), "temp": (25, 38), "humidity": (40, 70), "ph": (5.5, 7.5), "rainfall": (400, 900), "season": ["Kharif"], "soil": ["Sandy", "Red", "Alluvial"]},
    "Rubber": {"n": (30, 80), "p": (10, 35), "k": (20, 60), "temp": (25, 35), "humidity": (75, 95), "ph": (4.5, 6.5), "rainfall": (2000, 4000), "season": ["Kharif"], "soil": ["Laterite", "Red"]}
}

# Average yields by crop (tons/hectare) — national averages
CROP_AVG_YIELDS = {
    "Rice": 2.7, "Wheat": 3.5, "Maize": 3.0, "Sugarcane": 70.0, "Cotton": 1.8,
    "Jute": 2.5, "Groundnut": 1.5, "Soybean": 1.2, "Mustard": 1.3, "Gram": 1.0,
    "Lentil": 0.8, "Potato": 23.0, "Banana": 35.0, "Coconut": 10.0, "Coffee": 1.0,
    "Tea": 2.0, "Tobacco": 1.7, "Chilli": 2.0, "Turmeric": 5.5, "Bajra": 1.2,
    "Jowar": 0.9, "Ragi": 1.6, "Barley": 2.8, "Sesame": 0.4, "Rubber": 1.5
}
