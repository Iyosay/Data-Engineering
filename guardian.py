import awswrangler as wr
import pandas as pd
from dotenv import load_dotenv
import boto3
import os

# Load environment variables
load_dotenv()

# Configure AWS credentials - CORRECTED PARAMETER NAMES
boto3.setup_default_session(
    aws_access_key_id=os.getenv("ACCESS_KEY"),
    aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),  
    region_name='eu-north-1' 
)

# Upload to S3
try:
    wr.s3.to_parquet(
        df=pd.read_csv('article_urls.csv'),
        path="s3://joy-airhunmwunde-bucket/article/articles.parquet",
        dataset=True
    )
    print("Successfully uploaded Parquet file to S3")
except Exception as e:
    print(f"Error uploading to S3: {str(e)}")