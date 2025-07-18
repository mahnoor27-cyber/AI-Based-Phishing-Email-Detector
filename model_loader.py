import joblib

def load_model_and_vectorizer():
    model = joblib.load("models/phishing_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer
