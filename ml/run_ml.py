import sys
import os
sys.path.append(os.getcwd())

from data.data_loader import load_processed_data
from data.data_saver import save_processed_data
from ml.vectorizer import create_vectorizer
from ml.label_encoder import encode_labels
from ml.classifier import train_classifier
from ml.predictor import predict_category

df = load_processed_data()

texts = df["clean_text"]
labels = df["true_category"]

vectorizer = create_vectorizer()
X = vectorizer.fit_transform(texts)

y, encoder = encode_labels(labels)
model = train_classifier(X, y)

df["predicted_category"] = predict_category(
    model, vectorizer, encoder, texts
)

save_processed_data(df)

print("ML crime classification completed")