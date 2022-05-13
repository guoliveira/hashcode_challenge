# WIP: Hashcode Challenge

## Index
- [Introduction](https://github.com/guoliveira/hashcode_challenge#introduction)
- [Priori steps](https://github.com/guoliveira/hashcode_challenge#priori-steps)
  -  Source/Dataset
  -  Geohash
  -  Project planification
- [Project planification](https://github.com/guoliveira/hashcode_challenge#project-planification)


## Introduction

#TODO



## Priori steps

In order to follow [these objectives](DataEngineer_Challenge.pdf) some priori analysis/tasks were made:

### - Source/Dataset:
1. In the site provided for the [world-cities](https://simplemaps.com/data/world-cities) dataset it was analysed all the datasets and its metadata. This allowed to check the number of entries, the attributes and the format;
2. It was downloaded one file to make a simple check of contents.

### - Geohash:
1. Using the Wikipedia link provided it was analysed what is a geohash code;
2. It was used Google to know how to convert lat and lon values in geohash code using Python.

### - Project planification:
1. Define steps for the project
2. Define deadlines for each step



## Project planification

### Project steps: 

- [ ] [Development of a functional Python script to allow minimum requirements;](/code/README.md)
- [ ] Development of an Airflow DAG to run all the steps required and presented in previous point;
- [ ] Improvement of quality code and project description; 
- [ ] Simple presentation of work done.

### Deadlines: 
- Finish a working version of the Python Script by testing with sucess - 13/05/2022
- Develop and test with sucess a DAG that perform the ETL process -  17/05/2022
- Improve quality code and description code - 18/05/2022
- Do a presentation of the developed work - 19/05/2022
- Final check and challenge deliver - 19/05/2022 


### Orchestration of the data pipeline

With the goal of ensure a working flow and a visual graph it was decided to build a Airflow DAG.
This DAG has all the functions of the script mentioned above. 

The program Airflow was set to run inside Docker in a local manner. 
However, since it was created a Docker container all the Dag, python script and settings can run in other machine.
