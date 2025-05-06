import streamlit as st
from googletrans import Translator
import pyttsx3
import tempfile
import os

st.title("Multilingual Text Converter with Voice")

# Input text
text_input = st.text_area("Enter text to convert")

# Language options
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh-cn",
    "Arabic": "ar",
    "Russian": "ru"
}

target_language = st.selectbox("Choose target language", list(languages.keys()))
voice_gender = st.radio("Choose voice gender", ["Male", "Female"])

if st.button("Translate and Speak"):
    if not text_input.strip():
        st.warning("Please enter text first.")
    else:
        try:
            # Translate text
            translator = Translator()
            translated = translator.translate(text_input, dest=languages[target_language])
            translated_text = translated.text
            st.success(f"Translated Text ({target_language}):")
            st.write(translated_text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
            translated_text = ""

        if translated_text:
            try:
                # Set up TTS
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')

                # Try to select appropriate gendered voice
                selected_voice = None
                for voice in voices:
                    if voice_gender == "Male" and ("david" in voice.name.lower() or "male" in voice.name.lower()):
                        selected_voice = voice
                        break
                    elif voice_gender == "Female" and ("zira" in voice.name.lower() or "female" in voice.name.lower()):
                        selected_voice = voice
                        break

                if selected_voice:
                    engine.setProperty('voice', selected_voice.id)
                else:
                    st.warning("Selected voice gender not found. Using default voice.")

                # Save audio to temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tf:
                    temp_path = tf.name
                    engine.save_to_file(translated_text, temp_path)
                    engine.runAndWait()

                # Play audio
                st.audio(temp_path, format="audio/wav")

                # Download button
                with open(temp_path, "rb") as file:
                    st.download_button(
                        label="Download Audio",
                        data=file,
                        file_name="translated_audio.wav",
                        mime="audio/wav"
                    )

                # Clean up
                engine.stop()
                os.remove(temp_path)

            except Exception as e:
                st.error(f"Text-to-speech failed: {e}")
