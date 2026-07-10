rules = [

    # -----------------------------
    # Basic Symptoms
    # -----------------------------

    {
        "id": 1,
        "conditions": ["fever"],
        "conclusion": "High Temperature"
    },

    {
        "id": 2,
        "conditions": ["cough"],
        "conclusion": "Respiratory Infection"
    },

    {
        "id": 3,
        "conditions": ["fatigue"],
        "conclusion": "Weakness"
    },

    {
        "id": 4,
        "conditions": ["headache"],
        "conclusion": "Head Pain"
    },

    {
        "id": 5,
        "conditions": ["sore_throat"],
        "conclusion": "Throat Infection"
    },

    {
        "id": 6,
        "conditions": ["runny_nose"],
        "conclusion": "Nasal Infection"
    },

    {
        "id": 7,
        "conditions": ["breathing_problem"],
        "conclusion": "Breathing Issue"
    },

    {
        "id": 8,
        "conditions": ["body_pain"],
        "conclusion": "Muscle Pain"
    },

    {
        "id": 9,
        "conditions": ["chills"],
        "conclusion": "Possible Viral Infection"
    },

    {
        "id": 10,
        "conditions": ["loss_of_taste", "loss_of_smell"],
        "conclusion": "COVID Symptoms"
    },

    # -----------------------------
    # Common Cold
    # -----------------------------

    {
        "id": 11,
        "conditions": ["Respiratory Infection", "Throat Infection"],
        "conclusion": "Common Cold"
    },

    {
        "id": 12,
        "conditions": ["Common Cold", "Nasal Infection"],
        "conclusion": "Rest and Hydration"
    },

    # -----------------------------
    # Flu
    # -----------------------------

    {
        "id": 13,
        "conditions": ["High Temperature", "Respiratory Infection"],
        "conclusion": "Flu"
    },

    {
        "id": 14,
        "conditions": ["Flu", "Weakness"],
        "conclusion": "Consult Doctor"
    },

    {
        "id": 15,
        "conditions": ["Consult Doctor"],
        "conclusion": "Take Proper Rest"
    },

    # -----------------------------
    # Allergy
    # -----------------------------

    {
        "id": 16,
        "conditions": ["sneezing", "itchy_eyes"],
        "conclusion": "Allergy"
    },

    {
        "id": 17,
        "conditions": ["Allergy", "Breathing Issue"],
        "conclusion": "Asthma"
    },

    {
        "id": 18,
        "conditions": ["Asthma"],
        "conclusion": "Emergency"
    },

    # -----------------------------
    # COVID
    # -----------------------------

    {
        "id": 19,
        "conditions": ["High Temperature", "Head Pain", "Throat Infection"],
        "conclusion": "COVID-19"
    },

    {
        "id": 20,
        "conditions": ["COVID Symptoms", "COVID-19"],
        "conclusion": "PCR Test Recommended"
    },

    {
        "id": 21,
        "conditions": ["PCR Test Recommended"],
        "conclusion": "Home Isolation"
    },

    # -----------------------------
    # Food Poisoning
    # -----------------------------

    {
        "id": 22,
        "conditions": ["vomiting", "nausea"],
        "conclusion": "Food Poisoning"
    },

    {
        "id": 23,
        "conditions": ["Food Poisoning", "diarrhea"],
        "conclusion": "Dehydration Risk"
    },

    {
        "id": 24,
        "conditions": ["Dehydration Risk"],
        "conclusion": "Drink ORS"
    },

    # -----------------------------
    # Blood Pressure
    # -----------------------------

    {
        "id": 25,
        "conditions": ["high_bp", "dizziness"],
        "conclusion": "Hypertension"
    },

    {
        "id": 26,
        "conditions": ["Hypertension"],
        "conclusion": "Monitor Blood Pressure"
    },

    # -----------------------------
    # Skin
    # -----------------------------

    {
        "id": 27,
        "conditions": ["skin_rash"],
        "conclusion": "Skin Allergy"
    },

    {
        "id": 28,
        "conditions": ["Skin Allergy", "itchy_eyes"],
        "conclusion": "Consult Dermatologist"
    },

    # -----------------------------
    # Stomach
    # -----------------------------

    {
        "id": 29,
        "conditions": ["stomach_pain"],
        "conclusion": "Gastritis"
    },

    {
        "id": 30,
        "conditions": ["Gastritis", "nausea"],
        "conclusion": "Digestive Disorder"
    }

]