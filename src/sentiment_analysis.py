from transformers import pipeline

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text using a transformer model.
    
    Args:
        text (str): Text to analyze.
        
    Returns:
        str: Sentiment label ("POSITIVE" or "NEGATIVE").
    """
    if not text:
        print("No transcribed text available. Defaulting sentiment to negative.")
        return "NEGATIVE"
    
    sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_pipeline(text)[0]
    sentiment = result['label']
    print(f"Sentiment: {sentiment}")
    return sentiment