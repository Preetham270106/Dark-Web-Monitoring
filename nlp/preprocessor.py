from nlp.text_cleaner import clean_text
from nlp.tokenizer import tokenize_text

def preprocess_text(text):
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    return " ".join(tokens)