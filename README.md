# Hashcode Challenge

## Index
- [Introduction](https://github.com/guoliveira/hashcode_challenge#introduction)
- [Priori steps](https://github.com/guoliveira/hashcode_challenge#priori-steps)
  -  [Source/Dataset](https://github.com/guoliveira/hashcode_challenge#--sourcedataset)
  -  [Geohash](https://github.com/guoliveira/hashcode_challenge#--geohash)
  -  [Planification](https://github.com/guoliveira/hashcode_challenge#--project-planification)
- [Project planification](https://github.com/guoliveira/hashcode_challenge#project-planification)
  - [Project steps](https://github.com/guoliveira/hashcode_challenge#project-steps)
  - [Deadlines](https://github.com/guoliveira/hashcode_challenge#deadlines)
- [Presentation](https://github.com/guoliveira/hashcode_challenge/blob/main/README.md#presentation)

## Introduction

For the Data Engineer process to OLX Group it was required a challenge.
This challenge had [several objectives](DataEngineer_Challenge.pdf) with the scope of performing an Extract Transform and Load (ETL) process with Python.

It was decided to first focus on the ETL process doing the Python Script required and then it was decided to do an "extra-mile" by setting the process to run on a Airflow DAG.

All the devolepment steps are documented in this github Repo.

## Priori steps

Before going straight to the development some priori analysis/tasks were made:

### - Source/Dataset:
1. In the site provided for the [world-cities](https://simplemaps.com/data/world-cities) dataset it was analysed all the datasets and its metadata. This allowed to check the number of entries, the attributes and the format;
2. It was downloaded one file to make a simple check of contents.

### - Geohash:
1. Using the [Wikipedia link](https://en.wikipedia.org/wiki/Geohash) provided it was analysed what is a geohash code;
2. It was used Google to know how to convert lat and lon values in geohash code using Python.

### - Project planification:
1. Define steps for the project
2. Define deadlines for each step



## Project planification

### Project steps: 

- [x] [Development of a functional Python script to allow minimum requirements;](/code/README.md) (finished at 16/05/2022 due AWS constraints)
- [x] [Development of an Airflow DAG to run all the steps required and presented in previous point;](airflow/README.md) (finished at 16/05/2022)
- [x] Improvement of quality code and project description; (finished at 17/05/2022)
- [x] Simple presentation of work done.

### Deadlines: 
- Finish a working version of the Python Script by testing with sucess - 13/05/2022
- Develop and test with sucess a DAG that perform the ETL process -  17/05/2022
- Improve quality code and description code - 18/05/2022
- Do a presentation of the developed work - 19/05/2022
- Final check and challenge deliver - 19/05/2022 

## Presentation

In order to show what was done I did this video:


https://user-images.githubusercontent.com/12693788/168809221-cd865270-0f2d-4514-a8fe-1fe4c994b626.mp4

