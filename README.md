# AIML-Exam

### By Pelle Hald Vedsmand and Nicolai Rosendahl

Contains 2 parts.

#### - ML-part training models.
Trained on https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset

1. We train a neural network for the first screening. We categorize the resume and see if the category matches. (Multi label)

3. We semantic compare the resume against the job requirements in a second screening giving more complex comparisations of actual skills.

#### - AI-part using pretrained LLMs in a RAG setup




### How to setup and run the project

You need a python version >= 3.11

```pip install -r requirements.txt```

#### Downloading of the models:

```python setupScripts/downloadRFModel.py```

```python setupScripts/downloadBertModel.py.py```

#### Launching the streamlit application
```cd Webapp```

```python -m streamlit run start.py```
