import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError, ClientError

# Load environment variables from .env file
load_dotenv()

def joy_bucket():
    try:
        AWS_ACCESS_KEY = os.getenv("ACCESS_KEY")
        AWS_SECRET_KEY = os.getenv("SECRET_ACCESS_KEY")
        region = 'eu-north-1'
        bucket_name = 'joy-airhunmwunde-bucket' 

    

        # Create session with credentials
        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=region
        )

        # Create S3 client
        s3 = session.client('s3')

        # Create bucket
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )

        print(f"Success! Created bucket: {bucket_name}")
        return bucket_name

    except NoCredentialsError:
        print("AWS credentials not found. Please configure them in your .env file:")
        print("ACCESS_KEY=your_access_key")
        print("AWS_SECRET_KEY=your_secret_key")
        return None
    except ClientError as e:
        print(f"AWS error occurred: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Call the function
joy_bucket()