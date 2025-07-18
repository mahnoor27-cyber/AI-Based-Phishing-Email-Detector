import pandas as pd
import re
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import nltk
nltk.download('stopwords')

# Load and prepare data
df = pd.read_csv("emails.csv", encoding='ISO-8859-1')
df = df[['v1', 'v2']]  # Keep only relevant columns
df.rename(columns={'v1': 'label', 'v2': 'body'}, inplace=True)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})
df.dropna(inplace=True)

# Clean text
stop_words = set(stopwords.words("english"))
def clean_email(text):
    text = re.sub(r"http\\S+", "", text.lower())  # remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    tokens = text.split()  # basic tokenization
    return " ".join([word for word in tokens if word not in stop_words])

df['cleaned_body'] = df['body'].apply(clean_email)

# Vectorization
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df['cleaned_body'])
y = df['label']

# Model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
