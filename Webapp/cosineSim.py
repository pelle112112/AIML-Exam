import streamlit as st
from sentence_transformers import SentenceTransformer, util
import torch
import os
import json


st.title("Resume vs Job Role Matching (Cosine Similarity)")


# We load the model and cache it to reduce loading time on subsequent runs
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
model = load_model()

# Loading of the job requirements from JSON files and caching the results to again reduce loading time
@st.cache_resource
def load_job_descriptions():
    job_folder = os.path.join(os.path.dirname(__file__), "..", "companyDocs", "json")
    job_descriptions = {}

    allowed_roles = {
        "Software Developer": "software_developer.json",
        "Database Administrator": "database-administrator.json",
        "Systems Administrator": "systems_administrator.json",
        "Project Manager": "project_manager.json",
        "Web Developer": "web_developer.json",
        "Network Administrator": "network_administrator.json",
        "Security Analyst": "security-analyst.json",
        "Python Developer": "python-developer.json",
        "Java Developer": "java-developer.json",
        "Front End Developer": "front-end-developer.json",
    }

    actual_files = {f.lower(): f for f in os.listdir(job_folder)}  # lowercase mapping

    for role_name, expected_file in allowed_roles.items():
        lower_file = expected_file.lower()
        actual_file = actual_files.get(lower_file)
        if actual_file:
            filepath = os.path.join(job_folder, actual_file)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                parts = [
                    data.get("job_description", ""),
                    " ".join(data.get("tasks", [])),
                    " ".join(data.get("technical_skills", [])),
                    " ".join(data.get("personal_skills", [])),
                ]
                full_description = " ".join(part.strip() for part in parts if part.strip())
                if full_description:
                    job_descriptions[role_name] = full_description
        else:
            st.warning(f"Job file not found for role: {role_name} (expected: {expected_file})")

    return job_descriptions


job_descriptions = load_job_descriptions()
st.text(f"Loaded job descriptions: {len(job_descriptions)}")


# This function computes the embeddings for the job descriptions into a BERT-like format
@st.cache_resource
def get_job_embeddings(descriptions):
    return {role: model.encode(desc, convert_to_tensor=True) for role, desc in descriptions.items()}

job_embeddings = get_job_embeddings(job_descriptions)

# --- User input ---
resume_text = st.text_area("Paste your resume here:")

if st.button("Match Resume to Job Roles"):
    if not resume_text.strip():
        st.warning("Please paste a resume.")
    else:
        with st.spinner("Computing similarities..."):
            # We compute the embedding for the resume texts aswell
            resume_emb = model.encode(resume_text, convert_to_tensor=True)

            # Compute cosine similarity between the resume and each job description. Score is between 0 and 1, the higher the better
            scores = {}
            for role, job_emb in job_embeddings.items():
                score = util.cos_sim(resume_emb, job_emb).item()
                scores[role] = round(score, 3)

            # Sort the scores in descending order, so the best matches are at the top
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

            st.subheader("Match Results:")
            for role, score in sorted_scores:
                st.write(f"**{role}**: {score:.3f}")

# --- Optional Debug Info ---
with st.expander("Loaded Job Descriptions"):
    for role, desc in job_descriptions.items():
        st.markdown(f"***{role}***:\n\n {desc}\n")
