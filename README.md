# AI-Based-Phishing-Email-Detector

A lightweight machine learning-based web app that detects whether an email is phishing or legitimate, built using Python, scikit-learn, Streamlit, and ELI5 for model explanation.Uses eli5 to explain why the model made a prediction, showing which words had the most influence.
## Features
- Predicts whether an email is phishing or legitimate
- Trained using logistic regression on a labeled dataset
- Displays feature importance using `eli5`
- Cleans input text with basic NLP preprocessing
- Web-based interface with Streamlit
## Project Structure
├── app.py # Streamlit frontend
├── train_model.py # Model training script
├── utils/
│ ├── text_cleaner.py# Text cleaning and tokenization
│ ├── model_loader.py
│ └── eli5_explainer.py # ELI5 explanation logic
├── models/
│ ├── model.pkl # Trained ML model
│ └── vectorizer.pkl # TF-IDF vectorizer
├── emails.csv # Dataset (emails with labels)
├── requirements.txt # Python dependencies
└── README.md # This file
## Dataset
- CSV Format: `emails.csv`
- Columns:
  - `text`: The raw email content
  - `label`: 1 for phishing, 0 for legitimate
## Setup Instructions
### 1. Clone the Repository
git clone https://github.com/mahnoor27-cyber/AI-Based-Phishing-Email-Detector
cd phishing-email-detector
## Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate    # For Windows
## Install Dependencies
pip install -r requirements.txt
## Train the Model
python train_model.py
## Run the Streamlit App
streamlit run app.py
