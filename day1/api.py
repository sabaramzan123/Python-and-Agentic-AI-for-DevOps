from fastapi import FastAPI
from system_util import get_system_details
import boto3

s3 = boto3.resource('s3')
app = FastAPI(title = "DevOps utilities API")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/metrics")
def metrics():
    """
    Get system metrics such as CPU, memory, and disk usage.
    """
    return get_system_details()

@app.get("/aws/s3")
def get_buckets():
    buckets = []
    for bucket in s3.buckets.all():
        buckets.append(bucket.name)
    return buckets


    
