1.README.md

AI-Powered Assistive Tool for Visually Impaired Individuals
streamlit run app.py


Instructions to Run

1. Save the code in the appropriate files as per the structure.


2. Install the necessary dependencies:

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run app.py


4. Open the provided URL (e.g., http://localhost:8501) in your browser.

2.Project Structure

assistive_ai/
├── app.py                   # Main Streamlit file
├── scene_understanding.py   # Image captioning logic
├── text_to_speech.py        # OCR and TTS functionality
├── object_detection.py      # Object and obstacle detection
├── requirements.txt         # Dependencies


3.Requirements Libraries

streamlit
transformers
torch
Pillow
opencv-python
pytesseract
gTTS
ultralytics

