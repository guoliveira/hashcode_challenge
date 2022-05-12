# WIP: Hashcode Challenge

In order to follow [these objectives](DataEngineer_Challenge.pdf) some priori analysis/tasks were made:

**- Source/Dataset:**
1. In the site provided for the [world-cities](https://simplemaps.com/data/world-cities) dataset it was analysed all the datasets and its metadata. This allowed to check the number of entries, the attributes and the format;
2. It was Downloaded one CSV file to make a simple check of contents.

**- Geohash:**
1. Using the Wikipedia link provided it was analysed what is a Geohash;
2. It was Googled how to convert lat and lon in geohash code using python.

**- Project planification:**
1. Define steps for the project
2. Define deadlines for each step

## Project steps: 
- [ ] Development of a functional Python script to allow minimum requirements;
- [ ] Development of an Airflow DAG to run all the steps required and presented in previous bullet;
- [ ] Improvement of quality code and project; 
- [ ] Simple presentation of work done.


### Minimum requirements

In order to get the minimum requirements for the challenge a functional Python script was developed. 

**This script has the following main tasks/function:**
1. Download of the dataset and conversion into Pandas dataframe;
2. Filter Portuguese cities using column "Country";
3. Creation of the extra Geohash code column;
4. Conversion of the dataframe into a JSON file;
5. Upload the previous file into Aws S3 using boto3 library.

The working version of the script is present in this Python file.


### Orchestration of the data pipeline

With the goal of ensure a working flow and a visual graph it was decided to build a Airflow DAG.
This DAG has all the functions of the script mentioned above. 

The program Airflow was set to run inside Docker in a local manner. 
However, since it was created a Docker container all the Dag, python script and settings can run in other machine.
