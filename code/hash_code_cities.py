import requests as rq
from zipfile import ZipFile
import pandas as pd
import pygeohash as gh
import json
import boto3
import argparse


def main(params):
    # Parameters
    access_key = params.access_key
    secret_key = params.secret_key
    country_to_filter = params.country

    # Download and conversion into dataframe
    download_zip_file('https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip',
                      'worldcities.zip')
    dataframe_cities = get_full_df('worldcities.zip', 'worldcities.csv')

    # Country filtering
    dataframe_country = filter_country(dataframe_cities, country_to_filter)
    # Columns selections
    dataframe_select = select_columns(dataframe_country, 'city', 'lat', 'lng', 'population')

    # Adding extra geohash_code
    final_df = adding_geohash_code(dataframe_select)

    # Conversion of dataframe into json file
    country_name = 'World' if country_to_filter is None else country_to_filter
    from_df_to_json(final_df, f'cites_from_{country_name}.json')


def download_zip_file(online_path, local_path):
    """
    Function to download a zip file in the online_path into the local_path
    :param online_path: string of a URL of a zip file
    :param local_path: string of a full path of the file
    :return: None
    """
    with rq.get(online_path) as response:
        open(local_path, "wb").write(response.content)


def get_full_df(local_zip_path, filename):
    """

    :param local_zip_path:
    :param filename:
    :return:
    """
    with ZipFile(local_zip_path) as zip_file:
        df = pd.read_csv(zip_file.open(filename))
    return df


def filter_country(dataframe, country_to_filter):
    """

    :param dataframe:
    :param country_to_filter:
    :return:
    """
    # If there is no country to filter it will return all the dataset
    if country_to_filter is None:
        print('LOG: No country to filter. Returning all the World')
        df = dataframe
    else:
        print(f'LOG: Getting cities from {country_to_filter}..')
        df = dataframe[dataframe.country == country_to_filter]
    return df


def select_columns(dataframe, *argv):
    """

    :param dataframe:
    :param argv:
    :return:
    """
    df = pd.DataFrame()
    print('LOG: Selecting columns...')
    for arg in argv:
        df[arg] = dataframe[[arg]]
    return df


def adding_geohash_code(dataframe):
    """

    :param dataframe:
    :return:
    """
    print('LOG: Adding GeoHash column...')
    dataframe["geohash"] = dataframe.apply(lambda x: gh.encode(x.lat, x.lng, precision=12), axis=1)
    return dataframe


def from_df_to_json(dataframe, json_filename):
    """

    :param dataframe:
    :param json_filename:
    :return:
    """
    result = dataframe.to_json(orient="records")
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    return None

#def upload_to_s3(filename, s3_bucket, s3_path):
#    s3_client = boto3.client('s3')
#    try:
#        response = s3_client.upload_file(filename, s3_bucket, f'{s3_path}{filename}')
#    except ClientError as e:
#        logging.error(e)
#        return False
#    return True


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process of ETL to extract information of the cities of one country'
                                                 ', obtain the geohash code and load a json into AWS S3')

    # Arguments
    parser.add_argument('country', help='The country we want to filter ', nargs='?', const='', type=str)
    parser.add_argument('access_key', help='Access_key AWS ', nargs='?', const='', type=str)
    parser.add_argument('secret_key', help='Secret_key AWS ', nargs='?', const='', type=str)

    args = parser.parse_args()


    main(args)




