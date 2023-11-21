from local_secrets import bucket
from connect import s3
import os

root = os.getcwd()
file = 'video.mp4'
folder = 'to_upload'
path = os.path.join(root, folder, file)

target = 'video.mp4'

s3.Bucket(bucket.name).upload_file(path, 'video.mp4')