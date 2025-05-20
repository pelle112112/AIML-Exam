from transformers import BertForSequenceClassification, BertTokenizer
from huggingface_hub import hf_hub_download
import os
import shutil


def download_random_forest_model():
    model_repo = "pelle112112/RFResumeScreening"
    filename = "random_forest_best.pkl"
    target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models', 'classificationModels'))

    os.makedirs(target_dir, exist_ok=True)

    print(f"Downloading Random Forest model from: {model_repo}")
    file_path = hf_hub_download(repo_id=model_repo, filename=filename)

    print(f"Copying model to: {target_dir}")
    shutil.copy(file_path, os.path.join(target_dir, filename))
    print("✅ Random Forest model download and save completed.\n")


def main():
    download_random_forest_model()


if __name__ == "__main__":
    main()