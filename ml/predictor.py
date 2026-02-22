def predict_category(model, vectorizer, encoder, texts):
    vectors = vectorizer.transform(texts)
    predictions = model.predict(vectors)
    return encoder.inverse_transform(predictions)