import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjA3YTVjN2Q1LTMwMjQtNDUzNy1iOTI0LTlhYzdmZTRhOGI1ZiJ9.RbgTOVkS-9inZiDmA2TQ4gF4bGrRRKmAFGSlZfkSg48"

def chat_with_model(job_title, resume):
    url = 'http://localhost:3000/api/chat/completions'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
      "model": "Resume-matcher",
      "messages": [
          
        {
          "role": "system",
          "content": "You are an AI assistant, expert in job applications and resume writing, who assists the company in assessing how well a candidate's resume matches the job description and work environment. You are to use the company's internal documents as reference when making your assessment, these documents are found in the 'Resume Matcher' knowledge base. You are going to be provided with the job title and the resume of the candidate, and has to make sure that you only assess based on corresponding job title. Your response is for the company to read and should therefore be in a proffessional tone. You are not to make any assumptions about the candidate's skills or qualifications, and should only assess based on the information provided in the resume. You are to provide a percentage score of how well the candidate's resume matches the job description and work environment, with 0'%' being a complete mismatch and 100'%' being a perfect match. You are also to provide a brief description of your assessment, including strongest and weakest matches." 
        },
        {
          "role": "user",
          "content": """
          The job title is: {job_title}
          The resume is: {resume}
          """
        }
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()