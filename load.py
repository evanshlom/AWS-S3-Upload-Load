from local_secrets import bucket
from connect import s3
import os

root = os.getcwd()
target = 'video.mp4'
t_folder = 'get_here'
t_path = os.path.join(root, t_folder, target)

obj = s3.Bucket(bucket.name).Object('video.mp4').get()

with open(t_path, 'wb') as data:
    data.write(obj['Body'].read())
    data.close()