from sklearn.preprocessing import LabelEncoder

def encode_labels(labels):
    encoder = LabelEncoder()
    encoded = encoder.fit_transform(labels)
    return encoded, encoder