import awswrangler as wr
import pandas as pd
from dotenv import load_dotenv
import boto3
import os
import requests

# Load environment variables
load_dotenv()

url = "https://randomuser.me/api/?results=500"
response = requests.get(url)
data = response.json()

# Extract relevant columns and fileds
information_data = []
for user in data["results"]:
    information_data.append({
        "gender": user["gender"],
        "date_of_birth": user["dob"]["date"],
        "first_name": user["name"]["first"],
        "last_name": user["name"]["last"],
        "full_name": f"{user['name']['first']} {user['name']['last']}"
    })

# Convert to DataFrame
df = pd.DataFrame(information_data)

# Upload to S3
session = boto3.Session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
    region_name="eu-north-1"
)

wr.s3.to_parquet(
    df=df,
    path="s3://joy-airhunmwunde-bucket/information_data",
    dataset=True,
    mode="append",
    boto3_session=session
)
