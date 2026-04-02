import streamlit as st
import joblib

# Page config
st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# Load model
model = joblib.load("student_model.pkl")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 Student Score Predictor</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p style='text-align: center;'>Predict your exam score based on study hours</p>", unsafe_allow_html=True)

st.write("---")

# Input section
st.subheader("📥 Enter Details")

hours = st.slider("📚 Study Hours", 0.0, 24.0, 1.0)

st.write("---")

# Prediction
if st.button("🚀 Predict Score"):
    prediction = model.predict([[hours]])
    
    st.success(f"🎯 Predicted Score: {prediction[0]:.2f}")
    
    # Feedback message
    if prediction[0] > 80:
        st.info("🔥 Excellent! Keep it up!")
    elif prediction[0] > 50:
        st.info("👍 Good job! improve the hours you study")
    else:
        st.warning("⚠️ You need more study time!")

st.write("---")

# Footer
st.markdown("<p style='text-align: center;'>Made by You 🚀</p>", unsafe_allow_html=True)