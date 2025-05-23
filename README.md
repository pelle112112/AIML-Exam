# AIML-Exam

### By Pelle Hald Vedsmand and Nicolai Rosendahl

## Deliverables

- [Synopsis containing comparative analysis]()
- [Documentation of ML models (notebooks)]()
- [Setup and running the project](README.md)

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

After installing the model use the following command to exit the chat.

```
/bye
```
 
##### Step 3.

Navigate to open webUI, press get started and create an admin account when prompted. 

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

Your knowledge should now look something like this:

![image](documentation/Local_AI_model/knowledge_complete.png)

##### Step 5.

Your local AI is now setup and ready to use through the frontend application, on page "Ask your local AI for help".

Keep in mind for future usage it is needed to have ollama serve the models to Open WebUI and to have the docker container running.

### How to setup and run the project

You need a python version >= 3.11

#### Installing required dependencies
To install the required dependencies, it is highly recommended to use a virtual environment to not get any conflicting versions.

Put the following command into the terminal from the root of the project:

`pip install -r requirements.txt`

#### Downloading of the models:
The following scripts will download the BERT and RF models which are required for the first part of the screening process.

Put the following commands one at a time into the terminal from the root of the project:

`python setupScripts/downloadRFModel.py`

`python setupScripts/downloadBertModel.py`

#### Launching the streamlit application
Once everything is set up you should be able to run the application. 

Firstly navigate to the Webapp folder with the following command:

`cd Webapp`

Then type the following command to run the streamlit application:

`python -m streamlit run start.py`

### Documentation of the Machine Learning

The thoughts and reflections will be in the following files, where we trained different models for the first screening process of resumes (Multi labeling):

- dataCleaning.ipynb
- BertTraining.ipynb
- ClassificationModels.ipynb
- dataExploration.ipynb
