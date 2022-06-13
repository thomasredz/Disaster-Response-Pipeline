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
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md
```



# Results <a name="result"></a>
The main findings with the answers of the questions can be found [here](https://medium.com/@thomasredz/so-you-wanna-list-a-property-on-the-airbnb-market-maybe-this-can-help-ffcbda1b4da0).

# License <a name="license"></a>
Must give credit to Udacity-Data Science Nanodegree for the knowledge and the techniques for the manipulation of the data. 
You can find the Licensing for the data and other descriptive information at the [Kaggle](https://www.kaggle.com/datasets/airbnb/seattle) link available here. 
Feel free to use the code here as you would like!

[Link Repository Github](https://github.com/thomasredz/airbnb-seattle)
