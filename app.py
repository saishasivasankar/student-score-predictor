import streamlit as st
import joblib

# Page config
st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# Load model
model = joblib.load("student_model.pkl")

# Title (NO HTML)
st.title("🎓 Student Score Predictor")

# Subtitle
st.caption("Predict your exam score based on study hours")

st.divider()

# Input section
st.subheader("📥 Enter Details")

hours = st.slider("📚 Study Hours", 0.0, 24.0, 1.0)

st.divider()

# Prediction
if st.button("🚀 Predict Score"):
    prediction = model.predict([[hours]])
    
    st.success(f"🎯 Predicted Score: {prediction[0]:.2f}")
    
    if prediction[0] > 80:
        st.info("🔥 Excellent! Keep it up!")
    elif prediction[0] > 50:
        st.info("👍 Good job! Improve your study hours")
    else:
        st.warning("⚠️ You need more study time!")

st.divider()

# Footer
st.caption("Made by You 🚀")