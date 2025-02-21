import streamlit as st
from langdetect import detect
from deep_translator import GoogleTranslator

# Streamlit UI
st.title("Auto-Detect Language and Translate")

# User input
user_text = st.text_area("Enter text to detect and translate:")

# Target language selection
target_lang = st.selectbox(
    "Select target language:",
    ["en", "te","es", "fr", "de", "hi", "zh", "ar"],  # Add more language codes as needed
)

if st.button("Translate"):
    if user_text:
        try:
            # Detect language
            detected_lang = detect(user_text)
            st.write(f"Detected Language: {detected_lang}")

            # Translate
            translated_text = GoogleTranslator(source=detected_lang, target=target_lang).translate(user_text)
            st.success(f"Translated Text ({target_lang}): {translated_text}")

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to translate.")
