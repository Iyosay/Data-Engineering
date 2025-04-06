import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = "http://api.football-data.org/v4/competitions/"

response_API = requests.get(url)

football_data = response_API.json()

football_data['competitions']

competition_names_list = []

for competition in football_data['competitions']:
    name = competition['name']
    competition_names_list.append(name)

distinct_competition_names = set(competition_names_list)

competition_names = list(set(competition_names_list))

# Normalize the 'jobs_list' JSON data into a DataFrame
df = pd.json_normalize(competition_names)

# Create a boto3 session
session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    region_name='eu-north-1'
)

# Save DataFrame as a Parquet file in S3 bucket
wr.s3.to_parquet(
    df=df,
    path="s3://joy-airhunmwunde-bucket/competition_names.parquet",
    dataset=True,
    mode='append',
    boto3_session=session
)
