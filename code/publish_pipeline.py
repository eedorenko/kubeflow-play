import kfp
import os


host = "http://localhost:8080/pipeline"
namespace = "kubeflow"
pipeline_file_path = "/Users/efedorenko/work/kfp/pipeline.yaml"
pipeline_name = "Banditos Tacos and Burritos"

client = kfp.Client(host=host, namespace=namespace)
pipeline_file = os.path.join(pipeline_file_path)
pipeline = client.pipeline_uploads.upload_pipeline(pipeline_file, name=pipeline_name)  # noqa: E501
pipeline_version = client.pipeline_uploads.upload_pipeline_version(pipeline_file,  # noqa: E501
                                                                   name="Version1",  # noqa: E501
                                                                   pipelineid=pipeline.id)  # noqa: E501
