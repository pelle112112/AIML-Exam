import streamlit as st
from openwebui_api import chat_with_model

st.title("Ask your AI assistant for a match score")

job_title = st.selectbox(
    "Select a job title:",
    options=[
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
)
text = st.text_area("Paste a resume below:")

if st.button("Get match score"):
    match job_title:
        case "Software Developer":
            job_title = "Software_developer"
        case "Database Administrator":
            job_title = "Database_administrator"
        case "Systems Administrator":
            job_title = "Systems_administrator"
        case "Project Manager":
            job_title = "Project_manager"
        case "Web Developer":
            job_title = "Web_developer"
        case "Network Administrator":
            job_title = "Network_administrator"
        case "Security Analyst":
            job_title = "Security-analyst"
        case "Python Developer":
            job_title = "Python-developer"
        case "Java Developer":
            job_title = "Java-developer"
        case "Front-End Developer":
            job_title = "Front-end-developer"
        case _:
            st.error("Invalid job title selected.")
            st.stop()

    jsonResponse = chat_with_model(
        job_title=job_title,
        resume=text
    )
    
    st.subheader("Match Score:")
    try:
        ai_response = jsonResponse["choices"][0]["message"]["content"]
        st.write(ai_response)
    except Exception as e:
        st.error(f"Failed to parse response: {e}")
        st.json(jsonResponse)
