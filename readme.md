### Table of Contents

1. [ Installation ](#installation)
2. [ Motivation ](#motivation)
3. [ File description ](#file_desc)
4. [ Results ](#result)
5. [ License ](#license)

# Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. 
The code should run with no issues using Python versions 3.*.

# Motivation <a name="motivation"></a>

During a natural disaster, people send a lot of messages asking for help, food or just to inform about what is happening in a certain moment and location.

In this project we are going to analyze a dataset from [Figure Height](https://appen.com/), containing messages sent during a natual disaster.

After a little bit of data exploration, we are going to build a model which aim to classify the message in a category that fit the type of help needed.

The last step will be to build a web app in order to classify a new message inputted by the user.

# File Description <a name="file_desc"></a>

```
.
├── disaster_response_pipeline_project
│   ├── app
│    |   ├── templates
│    │   │   │   ├── go.html
│    │   │   │   └── master.html
│    │   │   ├── run.py
│   ├── models
│   │   ├── train_classifier.py
│   └── readme.md
├── data
│       ├── DisasterResponse.db
│       └── disaster_categories.csv
│       └── process_data.py
├── ETL Pipeline Preparation.ipynb
├── ML Pipeline Preparation.ipynb
└── readme.md

```

# How to launch the app?:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python disaster_response_pipeline_project/models/train_classifier.py data/DisasterResponse.db disaster_response_pipeline_project/models/classifier.pkl`

2. Run the following command in the project's root directory to run your web app.
    `python disaster_response_pipeline_project/app/run.py`

3. Go to http://0.0.0.0:3001/


# Results <a name="result"></a>
The trained model has an accuracy of 94%, and we were successufully able to launch the app and analyze new messages.

# License <a name="license"></a>
Must give credit to Udacity-Data Science Nanodegree for the knowledge and the techniques for the manipulation of the data.

You can find the Licensing for the data and other descriptive information at the [Figure Height](https://appen.com/) link available here. 
Feel free to use the code here as you would like!

[Link Repository Github](https://github.com/thomasredz/Disaster-Response-Pipeline)
