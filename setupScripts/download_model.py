from transformers import BertForSequenceClassification, BertTokenizer
import os

def main():
    # Define model path
    model_name = "pelle112112/ResumeLabelBert"
    save_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))

    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Load model and tokenizer
    print(f"Downloading model and tokenizer from: {model_name}")
    model = BertForSequenceClassification.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # Save them to /models
    print(f"Saving model and tokenizer to: {save_directory}")
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)
    print("Download and save completed.")

if __name__ == "__main__":
    main()
