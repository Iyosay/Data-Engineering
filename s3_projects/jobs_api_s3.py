import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"

response_API = requests.get(url)

get_data = response_API.json()

job_data = get_data['jobs']

job_data[0]

job_data[0]['jobTitle']

senior_role_list = []

manager_role_list = []

for jobs in job_data:
    role_list = jobs['jobTitle']
for jobs in job_data:
    if 'Senior' in jobs['jobTitle']:
        senior_role_list.append(jobs['jobTitle'])
    if 'Manager' in jobs['jobTitle']:
        manager_role_list.append(jobs['jobTitle'])

# Combine the two lists
job_list = senior_role_list + manager_role_list


# Normalize the 'jobs_list' JSON data into a DataFrame
df = pd.json_normalize(job_list)

# Create a boto3 session
session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    region_name='eu-north-1'
)

# Save DataFrame as a Parquet file in S3 bucket
wr.s3.to_parquet(
    df=df,
    path="s3://joy-airhunmwunde-bucket/job_list.parquet",
    dataset=True,
    mode='append',
    boto3_session=session
)
