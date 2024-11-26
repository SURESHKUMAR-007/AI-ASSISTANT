import easyocr
from gtts import gTTS
from io import BytesIO
import streamlit as st
from PIL import Image
import numpy as np

def text_to_speech_conversion(image):
    """Extract text from an image and convert it to speech using EasyOCR."""
    # Convert PIL Image to numpy array
    image_np = np.array(image)

    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'])
    
    # Convert image to text
    text = reader.readtext(image_np, detail=0)  # Extract only text (no bounding boxes)
    extracted_text = " ".join(text)  # Combine list of text into a single string

    # Display extracted text
    st.write("Extracted Text:", extracted_text)

    # Convert text to speech
    if extracted_text.strip():
        tts = gTTS(extracted_text)
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.write("No text found in the image.")

# Streamlit interface
st.title("Image to Text-to-Speech Converter")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    text_to_speech_conversion(image)