import streamlit as st
from scene_understanding import generate_scene_description
from text_to_speech import text_to_speech_conversion
from object_detection import detect_objects
from PIL import Image

# Set up the Streamlit app
st.title("AI-Powered Assistive Tool for Visually Impaired Individuals")
st.sidebar.header("Features")
feature = st.sidebar.radio(
    "Select a Feature:",
    ["Scene Understanding", "Text-to-Speech", "Object Detection"]
)

uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if feature == "Scene Understanding":
        st.subheader("Real-Time Scene Understanding")
        description = generate_scene_description(image)
        st.write("Scene Description:", description)

    elif feature == "Text-to-Speech":
        st.subheader("Text-to-Speech Conversion for Visual Content")
        text_to_speech_conversion(image)

    elif feature == "Object Detection":
        st.subheader("Object and Obstacle Detection")
        annotated_image, objects = detect_objects(image)
        st.image(annotated_image, caption="Annotated Image", use_column_width=True)
        st.write("Detected Objects:", objects)
