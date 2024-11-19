import pytesseract
from gtts import gTTS
from io import BytesIO
import streamlit as st
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"  # Update path if needed

def text_to_speech_conversion(image):
    """Extract text from an image and convert it to speech."""
    text = pytesseract.image_to_string(image)
    st.write("Extracted Text:", text)

    if text.strip():
        tts = gTTS(text)
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.write("No text found in the image.")
