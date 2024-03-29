 **Docker Build**:

In order to run Airflow locally (in a container), I used an extended image, 
    containing some additional dependencies therefore I created a `Dockerfile` pointing to Airflow version you've just downloaded, 
    such as `apache/airflow:2.2.3`, as the base image,
       
   And customize this `Dockerfile` by:
* Added your custom packages to be installed. The one we'll need the most is `gcloud` to connect with the GCS bucket/Data Lake.
* Integrating `requirements.txt` to install libraries via  `pip install`
* Inserting bash commands to set Java env
* Inserting commands to download all the necessary files to run Spark 
   
4. **Import the official docker-compose setup file** from the latest Airflow version:
   ```shell
   curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
   ```

5. **Docker Compose**:

    Back in my `docker-compose.yaml`:
    * In `x-airflow-common`: 
        * Removed the `image` tag, to replace it with my `build` from my Dockerfile, as shown
        * Add the following line _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:- geohash2}
    * Changed `AIRFLOW__CORE__LOAD_EXAMPLES` to `false`;
    * Removed `redis`, `worker`, `triggerer` and `flower` from the file;
    * Set the CoreExecutor to LocalExecutor.    

6. Here's how the final versions:
   - [Dockerfile](./Dockerfile) and 
   - [docker-compose.yml](./docker-compose.yaml).
   
7. Additionally, it was necessary to do the following:

Create a new sub-directory called `Airflow` in mine `project` dir 

Set the Airflow user using the following commands:

    ```bash
    mkdir -p ./dags ./logs ./plugins ./scripts
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
