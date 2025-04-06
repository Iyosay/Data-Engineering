import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = "https://content.guardianapis.com/search?api-key=test&q=nigeria&from-date=2025-01-01&page-size=100"

response_API = requests.get(url)

get_data = response_API.json()

get_data.keys()

get_data['response'].keys()

get_data['response']['results']

data = get_data['response']

data['results']

article_urls = []

for article in data['results']:
    urls = article['webUrl']
    article_urls.append(urls)

df = pd.DataFrame({'article_urls': article_urls})

# Create a boto3 session
session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    region_name='eu-north-1'
)

# Save DataFrame as a Parquet file in S3 bucket
wr.s3.to_parquet(
    df=df,
    path="s3://joy-airhunmwunde-bucket/articles_urls.parquet",
    dataset=True,
    mode='append',
    boto3_session=session
)
