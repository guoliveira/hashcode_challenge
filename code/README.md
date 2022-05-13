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





## Development
To be able to get a good and working version in Python it was developed a first draft in a (Jupyter Notebook.)[portuguese_cities.ipynb]
The working version of the script is present in this Python file.


[Back to main](https://github.com/guoliveira/hashcode_challenge)
