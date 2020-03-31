import kfp
import os


host="http://23.101.114.95/pipeline"
namespace="play"
pipeline_file_path = "pipeline.py.tar.gz"
pipeline_name = "mexicanfood"

client = kfp.Client(host=host, namespace=namespace)
pipeline_file = os.path.join(pipeline_file_path)
pipeline = client.pipeline_uploads.upload_pipeline(pipeline_file, name=pipeline_name)
