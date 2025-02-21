import streamlit as st
from deep_translator import GoogleTranslator

def translate_text(text, dest_language):
    translator = GoogleTranslator(target=dest_language)
    return translator.translate(text)

def main():
    st.title("Language Translator From English")

    text = st.text_area("Enter text to translate:")
    languages = GoogleTranslator().get_supported_languages()
    target_language = st.selectbox("Select target language:", languages)

    if st.button("Translate"):
        if text.strip():
            translated_text = translate_text(text, target_language)
            st.success(f"Translated Text: {translated_text}")
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()
