import nltk
import random
import string

# Download required nltk data (run once)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Load data
def load_corpus(file_path="chatbot_corpus.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = f.read().lower()
        return nltk.sent_tokenize(raw)
    except FileNotFoundError:
        # fallback text if file is missing
        return [
            "Hello! How can I help you?",
            "I'm here to chat with you.",
            "Tell me more about that.",
            "Goodbye! It was nice talking to you."
        ]

# Initialize corpus
corpus = load_corpus()

# Simple response generator
def chatbot_response(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    # For now, just return a random sentence from corpus
    return random.choice(corpus)







