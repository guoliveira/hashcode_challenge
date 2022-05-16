### Orchestration of the data pipeline using Airflow

## Introduction

With the goal of ensure an automated working flow and a visual graph it was decided to build an Airflow DAG.
This DAG has all the functionalities of the script developed in the first step. 

The program Airflow was set to run inside Docker container in a local manner. 
However, since it was created a Docker container the DAG, Python code and settings (requirements) can be extrapolated for other laptop or virtual machine.

## Reproducibility

# Pre requisites

To be able to run the solution provided it is necessary to have:
- [Docker Desktop installed](https://www.docker.com/products/docker-desktop/)
- Access to internet. 
- AWS access key and secret key for the AWS account you want to load the data.

# Docker steps

To run Airflow with Docker and Docker-Compose the following steps were made and can be reproduced:
1. 


## Data workflow design

As mentioned before, the process is an ETL flow therefore the high level architecture is as following:




## Final Airflow DAG

The Python file with the final DAG to automate the challenge requirements is presented in 




[Back to main](https://github.com/guoliveira/hashcode_challenge)
