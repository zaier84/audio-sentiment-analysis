# Intelligent Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

This project analyzes the sentiment of audio input by converting speech to text, determining the sentiment using a transformer model, and generating an audio output with the result.

## Features

- **Speech-to-Text Conversion**: Transcribes MP3 audio to text using Google Speech Recognition.
- **Sentiment Analysis**: Uses a DistilBERT model to classify text as positive or negative.
- **Text-to-Speech Output**: Generates an audio file announcing the sentiment result using gTTS.
- **Modular Structure**: Organized into reusable Python modules for easy maintenance.

## Prerequisites

- Python 3.7 to 3.11
- FFmpeg installed for audio processing
- Internet connection for speech recognition and model download

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/IntelligentSentimentAnalysis.git
   cd IntelligentSentimentAnalysis
   ```

2. **Set up a virtual environment**:

   - In CMD:
     ```bash
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - In PowerShell (if scripts are restricted, first run as Administrator):
     ```powershell
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cpu
   ```

4. **Install FFmpeg**:
   - Download from [FFmpeg](https://ffmpeg.org/download.html) and add to PATH, or use Chocolatey:
     ```bash
     choco install ffmpeg
     ```
   - Verify with:
     ```bash
     ffmpeg -version
     ```

## Usage

1. **Prepare input audio**:

   - Place an MP3 file (e.g., `positive_sentiment.mp3`) in the `audio_files` directory.
   - Example content: "I am absolutely thrilled and overjoyed by the exceptional service I experienced."

2. **Run the script**:

   ```bash
   python src/main.py --input_audio audio_files/positive_sentiment.mp3 --output_dir audio_files
   ```

3. **Output**:
   - The script converts the MP3 to WAV, transcribes it, analyzes the sentiment, and saves an audio file (`sentiment_output.mp3`) in `audio_files`.
   - Example output:
     ```
     Converted audio_files/positive_sentiment.mp3 to audio_files/temp_audio.wav
     Transcribed Text: I am absolutely thrilled and overjoyed by the exceptional service I experienced.
     Sentiment: POSITIVE
     Output message: Your sentence is positive.
     Audio saved to audio_files/sentiment_output.mp3
     Removed temporary file: audio_files/temp_audio.wav
     ```

## Project Structure

```
IntelligentSentimentAnalysis/
├── src/
│   ├── text_to_audio.py      # Text-to-speech conversion
│   ├── audio_to_text.py      # MP3 to WAV and speech-to-text
│   ├── sentiment_analysis.py  # Sentiment analysis with DistilBERT
│   └── main.py               # Main workflow script
├── audio_files/              # Input/output audio files
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file
```

## Notes

- Ensure input MP3 files contain clear English speech for accurate transcription.
- Google Speech Recognition requires an internet connection.
- The DistilBERT model is downloaded automatically on first use.
- If transcription fails, the sentiment defaults to "NEGATIVE."
- Audio files in `audio_files/` are ignored by Git to avoid committing large files.
- Use Python 3.7–3.11 for compatibility with PyTorch 2.6.0.

## Troubleshooting

- **PowerShell script error**:
  - Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` in PowerShell as Administrator.
- **ModuleNotFoundError: No module named 'gtts' or 'torch'**:
  - Run `pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cpu`.
- **FFmpeg not found**:
  - Verify FFmpeg is installed and in your system PATH.
- **Speech recognition errors**:
  - Check audio quality and internet connectivity.
- **PyTorch errors**:
  - Ensure `torch==2.6.0` is installed with the CPU index.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact

For issues or questions, please open an issue on the [GitHub repository](https://github.com/zaier84/audio-sentiment-analysis).
