import os
import boto3

s3_client = boto3.client('s3')
s3_bucket = "aiworkflow"

training_dataset = "sim_data"

training_files = os.listdir(training_dataset+"/IMG/")

for file in training_files:
    file_name = training_dataset+"/IMG/"+file
    object_name = training_dataset+"_"+file
    print(object_name)
    s3_client.upload_file(file_name, s3_bucket, object_name)