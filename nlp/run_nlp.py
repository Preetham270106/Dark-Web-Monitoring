import sys
import os
sys.path.append(os.getcwd())

from nlp.preprocessor import preprocess_text
from data.data_loader import load_raw_data
from data.data_saver import save_processed_data

raw_df = load_raw_data()

raw_df["clean_text"] = raw_df["raw_text"].apply(preprocess_text)

processed_df = raw_df[
    ["source_url", "timestamp", "clean_text", "true_category"]
]

save_processed_data(processed_df)

print("NLP preprocessing completed")