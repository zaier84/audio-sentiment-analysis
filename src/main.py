import os
import argparse
from text_to_audio import text_to_audio
from audio_to_text import convert_mp3_to_wav, transcribe_audio
from sentiment_analysis import analyze_sentiment

def main():
    parser = argparse.ArgumentParser(description="Sentiment Analysis from Audio")
    parser.add_argument("--input_audio", default="audio_files/positive_sentiment.mp3", help="Path to input audio file")
    parser.add_argument("--output_dir", default="audio_files", help="Directory to save output audio")
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Define file paths
    input_audio_path = args.input_audio
    wav_temp_path = os.path.join(args.output_dir, "temp_audio.wav")
    output_audio_path = os.path.join(args.output_dir, "sentiment_output.mp3")

    # Step 1: Convert MP3 to WAV
    if not convert_mp3_to_wav(input_audio_path, wav_temp_path):
        print("Exiting due to conversion failure.")
        return

    # Step 2: Transcribe audio to text
    transcribed_text = transcribe_audio(wav_temp_path)

    # Step 3: Analyze sentiment
    sentiment = analyze_sentiment(transcribed_text)

    # Step 4: Generate output message and save as audio
    output_message = f"Your sentence is {sentiment.lower()}."
    print(f"Output message: {output_message}")
    text_to_audio(output_message, output_audio_path)

    # Clean up temporary WAV file
    if os.path.exists(wav_temp_path):
        os.remove(wav_temp_path)
        print(f"Removed temporary file: {wav_temp_path}")

if __name__ == "__main__":
    main()