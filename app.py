import streamlit as st
import joblib
import eli5
import streamlit.components.v1 as components
from utils.text_cleaner import clean_text
from utils.model_loader import load_model_and_vectorizer
from utils.eli5_explainer import explain_with_eli5

st.set_page_config(page_title="Phishing Email Detector", layout="wide")
st.title("📧 Phishing Email Detector")
st.markdown("Enter an email message below to check if it's **phishing** or **legitimate**.")

# Load model and vectorizer
model, vectorizer = load_model_and_vectorizer()

# Input from user
email_input = st.text_area("Paste the email content here:", height=300)

if st.button("Analyze"):
    if not email_input.strip():
        st.warning("Please enter some email content to analyze.")
    else:
        cleaned_text = clean_text(email_input)
        vectorized_input = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_input)[0]
        prediction_proba = model.predict_proba(vectorized_input)[0]

        st.subheader("🔍 Prediction:")
        if prediction == 1:
            st.error("⚠️ This email is likely **Phishing**.")
        else:
            st.success("✅ This email is likely **Legitimate**.")

        st.subheader("📊 Prediction Confidence:")
        st.write(f"Legitimate: {prediction_proba[0]*100:.2f}%")
        st.write(f"Phishing: {prediction_proba[1]*100:.2f}%")

        st.subheader("🤖 Why This Prediction?")
        with st.spinner("Generating explanation with ELI5..."):
            html_explanation = explain_with_eli5(model, cleaned_text, vectorizer)
            components.html(html_explanation, height=400, scrolling=True)
