import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    """
    Converts an MP3 audio file to WAV format.
    
    Args:
        mp3_path (str): Path to the input MP3 file.
        wav_path (str): Path to save the WAV file.
        
    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
        print(f"Converted {mp3_path} to {wav_path}")
        return True
    except Exception as e:
        print(f"Error converting MP3 to WAV: {e}")
        return False

def transcribe_audio(wav_path):
    """
    Transcribes audio to text using Google Speech Recognition.
    
    Args:
        wav_path (str): Path to the WAV audio file.
        
    Returns:
        str: Transcribed text or empty string if transcription fails.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="en-US")
        print(f"Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""