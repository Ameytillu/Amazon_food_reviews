import streamlit as st
import joblib
import numpy as np

# Load model and vectorizer from the correct path
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# App title
st.title("Food Review Sentiment Predictor 🍔🍽️")
st.write("Enter a food review and get its predicted sentiment.")

# Input box
user_input = st.text_area("📝 Enter your review here")

# Predict button
if st.button("Predict Sentiment"):
    if user_input.strip() != "":
        # Vectorize input
        input_vector = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(input_vector)
        prediction_proba = model.predict_proba(input_vector)

        # Convert prediction to readable label
        label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
        predicted_label = label_map[np.argmax(prediction_proba)]

        # Show result
        st.success(f"🧠 Predicted Sentiment: **{predicted_label}**")
    else:
        st.warning("Please enter a review to analyze.")

