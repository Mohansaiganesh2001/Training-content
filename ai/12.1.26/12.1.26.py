import pandas as pd

# Sample data
data = {
    "employee_id": [101, 102, 103, 104, 105],
    "department": ["HR", "IT", "", "Marketing", None],
    "feedback": [
        None,
        "Needs improvement in coding",
        "",
        "Creative ideas",
        "Met all sales targets"
    ],
    "rating": [4.5, None, 4.8, None, 4.7],
    "manager_comments": [
        "N/A",
        "Focus on deadlines",
        "Not sure",
        "Good job",
        ""
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display
print(df)

# Step 1 Replace textual missing values

df['feedback'] = df['feedback'].replace([None, '', 'N/A'], 'No feedback provided')

df['department'] = df['department'].replace([None, ''], 'Unknown')

df['manager_comments'] = df['manager_comments'].replace(['N/A', 'Not sure', ''], 'No manager comments')

# Setp2: Fill numeric missing values
df['rating'].fillna(df['rating'].mean(), inplace=True)

print(df)

# Language Detection
from langdetect import detect

data = {
    "ticket_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    "message": [
        "Cannot login to my account",                 # English
        "Payment failed but money deducted",          # English
        "App crashes on startup",                      # English
        "Need to reset my password",                  # English
        "Feature request: Dark mode",                 # English
        "My order hasn't arrived yet",                # English
        "Cannot change my email address",            # English
        "No puedo iniciar sesión en mi cuenta",       # Spanish
        "Impossible de se connecter à mon compte",    # French
        "मेरा अकाउंट लॉगिन नहीं हो रहा है"           # Hindi
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

def detect_language(str):
    try:
        return detect(str)
    except:
        return 'unknown'

df['language'] = df['message'].apply(detect_language)

print(df)

df_en = df[df['language'] == 'en'].copy()

print(df_en)