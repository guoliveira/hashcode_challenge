# Minimum requirements of the challenge

In order to get the minimum requirements for the challenge a functional Python script was developed. 

**This script has the following main tasks/function:**
1. Download of the zipfile;
2. Conversion of the csv file into Pandas dataframe;
3. Filter Portuguese cities using column "country";
4. Selection of the needed columns for the project;
5. Creation of the extra geohash code column;
6. Conversion of the dataframe into a JSON file;
5. Upload the previous file into AWS S3 using boto3 library.

## Pre-requisits

In order to run the ETL process is necessary to have:
- Python3 installed;
- The following Python libraries installed:
    - Pandas
    - ZipFile
    - argparse
    - json
    - requests
    - geohash2
    - boto3
- AWS Access Key and Secret Key to be able to use the AWS API.


## Development
To be able to get a good and working version in Python it was developed a first draft in a [Jupyter Notebook.](portuguese_cities.ipynb)
The working version of the script is present in this [Python file.](hash_code_cities.py) . 

The final script accepts the parameter "Country" as variable therefore, if we want to extract Portuguese cities we should
insert "Portugal" as input. (The same approach can be done for other country).

For security issues the AWS_ACCESS_KEY and AWS_SECRET_KEY are also parameters.
Therefore, **no sensitive information is hardcoded in the script.**

## To run

To be able to run the Python file is necessary to run the following in a terminal
```bash
python3 hash_code_cities.py <COUNTRY_TO_FILTER> <AWS_ACCESS_KEY> <AWS_SECRET_KEY>
```

## Quality issues

In order to assure the best quality of the Python script I ran the program 
['pep8'](https://peps.python.org/pep-0008/) and ['pylint'](https://pylint.pycqa.org/en/latest/) and improved the script 


[Back to main](https://github.com/guoliveira/hashcode_challenge)
