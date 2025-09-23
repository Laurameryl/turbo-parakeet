import nltk
import random
import stringimport nltk


# Download required nltk data (run once)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Load data
def load_corpus(file_path="data/chatbot_corpus.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read().lower()
    return nltk.sent_tokenize(raw)

corpus = load_corpus()

# Simple response generator
def chatbot_response(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    # For now, just return a random sentence from corpus
    return random.choice(corpus)

