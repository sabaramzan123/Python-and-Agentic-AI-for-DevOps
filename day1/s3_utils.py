import boto3

s3 = boto3.client('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)
    
    
file_name = 'C:\\Python-for-DevOps\\day1\\api.py'
object_name = 'api.py'
bucket_name = 'devops-ai-powered-saba'

response = s3.upload_file(file_name, bucket_name, object_name)
