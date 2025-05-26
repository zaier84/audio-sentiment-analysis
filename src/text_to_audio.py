import os
from gtts import gTTS

def text_to_audio(text, filename, lang='en'):
    """
    Converts text to speech and saves it as an MP3 file.
    
    Args:
        text (str): The text to convert.
        filename (str): Path to save the audio file.
        lang (str): Language code (default 'en' for English).
    """
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    print(f"Audio saved to {filename}")