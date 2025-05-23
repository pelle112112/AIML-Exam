import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import os
import pickle
import time

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

st.title("Resume Label Classifier")

# --- Model Selector ---
model_option = st.selectbox("Select Model", [
    "BERT Classifier",
    "Random Forest",
    "Logistic Regression",
    "Decision Tree"
])

# --- Load Models ---
@st.cache_resource
def load_bert_model_and_tokenizer():
    base_path = os.path.join(os.path.dirname(__file__), "..", "models")
    tokenizer = BertTokenizer.from_pretrained(base_path)
    model = BertForSequenceClassification.from_pretrained(base_path)
    model.eval()
    return tokenizer, model

@st.cache_resource
def load_vectorizer():
    path = os.path.join(os.path.dirname(__file__), "..", "models", "classificationModels", "vectorizer.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)

@st.cache_resource
def load_sklearn_model(name):
    path = os.path.join(os.path.dirname(__file__), "..", "models", "classificationModels", f"{name}.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)

# --- Text input ---
text = st.text_area("Paste a resume below:")

if st.button("Classify"):
    if not text.strip():
        st.warning("Please paste a resume first.")
    else:
        st.subheader("Predicted Label Scores:")

        start_time = time.time()

        if model_option == "BERT Classifier":
            tokenizer, model = load_bert_model_and_tokenizer()
            with torch.no_grad():
                inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
                outputs = model(**inputs)
                logits = outputs.logits
                probs = torch.sigmoid(logits).squeeze().tolist()
            for name, score in zip(label_names, probs):
                st.write(f"{name}: {score:.4f}")

        else:
            model_map = {
                "Random Forest": "random_forest_best",
                "Logistic Regression": "logistic_regression",
                "Decision Tree": "decision_tree"
            }
            vectorizer = load_vectorizer()
            clf = load_sklearn_model(model_map[model_option])

            vec = vectorizer.transform([text])
            if hasattr(clf, "predict_proba"):
                probs = clf.predict_proba(vec)
                for name, prob in zip(label_names, probs):
                    score = prob[0][1] if prob.shape[1] > 1 else prob[0][0]
                    st.write(f"{name}: {score:.4f}")
            else:
                preds = clf.predict(vec)[0]
                for name, val in zip(label_names, preds):
                    st.write(f"{name}: {float(val):.4f}")

        end_time = time.time()  # End timer
        elapsed_time = end_time - start_time
        st.info(f"Prediction completed in {elapsed_time:.2f} seconds.")
