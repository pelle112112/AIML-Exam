import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os


label_names = [
    "Software Developer",
    "Database Administrator",
    "Systems Administrator",
    "Project Manager",
    "Web Developer",
    "Network Administrator",
    "Security Analyst",
    "Python Developer",
    "Java Developer",
    "Front-End Developer"
]



model_path = "models"  # or "pelle112112/ResumeLabelBert" if loading from Hugging Face
tokenizer = BertTokenizer.from_pretrained(os.path.join(os.path.dirname(__file__), "..", "models"))
model = BertForSequenceClassification.from_pretrained(os.path.join(os.path.dirname(__file__), "..", "models"))
model.eval()

st.title("Resume Label Classifier")


text = st.text_area("Paste a resume below:")

if st.button("Classify"):
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.sigmoid(logits).squeeze().tolist()


    st.subheader("Predicted Label Scores:")
    for name, score in zip(label_names, probs):
        st.write(f"{name}: {score:.4f}")
