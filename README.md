# AIML-Exam

### By Pelle Hald Vedsmand and Nicolai Rosendahl

Contains 2 parts.

#### - ML-part training models.
Trained on https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset

1. We train a neural network for the first screening. We categorize the resume and see if the category matches. (Multi label)

3. We semantic compare the resume against the job requirements in a second screening giving more complex comparisations of actual skills.

#### - AI-part using pretrained LLMs in a RAG setup

#### Setting up the local AI.

The application uses Open WebUI's API to communicate with a locally installed AI. Below is a step to step guideline on installation and configuration of the local AI with and without NVIDIA GPU SUPPORT.

##### Step 1.
Spin up a docker container on an image that has Open WebUI with ollama support. 

```
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

or with NVIDIA GPU support

```
docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:cuda
```

##### Step 2.
Make sure you have ollama installed and start ollama. (This step can be skipped if you have the ollama app installed and running)

```
ollama serve
```

Open a new terminal and install the required model.

```
ollama run gemma3:4b
```
 
##### Step 3.

Navigate to open webUI and create an admin account when prompted. 

```
http://localhost:3000/
```

Go to settings, open Account settings and retrieve your API key (Which is required to use the AI through the frontend app)

![image](documentation/Local_AI_model/API_key_retrievel.png)

##### Step 4.

Navigate to workspace and into knowledge.

![image](documentation/Local_AI_model/workspace_knowledge.png)

Add a new knowledge named

```Resume Matcher```

Add a description I.E

```Assisting in rating resumes```

Click 'Create Knowledge'

![image](documentation/Local_AI_model/create_knowledge.png)

Click add content and choose Upload directory.

Upload all the content of [the companyDocs/json folder](/companyDocs/json/) 