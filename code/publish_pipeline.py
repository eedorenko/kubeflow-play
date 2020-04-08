import kfp
import os
import argparse


def main():
    parser = argparse.ArgumentParser("publish pipeline")

    parser.add_argument(
        "--run_id",
        type=str,
        required=True,
        help="unique CI run id"
    )

    parser.add_argument(
        "--kfp_host",
        type=str,
        required=False,
        default="http://localhost:8080/pipeline",
        help="KFP endpoint"
    )

    parser.add_argument(
        "--pipeline_file_path",
        type=str,
        required=False,
        default="pipeline.py.tar.gz",
        help="KFP pipeline file path"
    )

    parser.add_argument(
        "--pipeline_name",
        type=str,
        required=True,
        help="KFP pipeline name "
    )

    parser.add_argument(
        "--experiment_name",
        type=str,
        required=False,
        default="Default",
        help="Kubeflow experiment name "
    )

    args = parser.parse_args()

    host = args.kfp_host
    pipeline_file_path = args.pipeline_file_path
    pipeline_name = "{0}-{1}".format(args.pipeline_name, args.run_id)
    # experiment_name = args.experiment_name

    client = kfp.Client(host=host)
    pipeline_file = os.path.join(pipeline_file_path)
    try:
        # We upload a new pipline every time with a run_id in the pipeline name
        # until the issue with uploading a pipeline version is resolved
        # see  https://github.com/kubeflow/pipelines/issues/3442
        pipeline = client.pipeline_uploads.upload_pipeline(pipeline_file, name=pipeline_name)  # noqa: E501    
        return pipeline.id
        
        # pipeline_params = {}
        # pipeline_params["tenant_id"] = "72f988bf-86f1-41af-91ab-2d7cd011db47"  # noqa: E501
        # pipeline_params["service_principal_id"] = "6e85e789-3b22-4edb-89d0-2ab7fc09d488"  # noqa: E501
        # pipeline_params["service_principal_password"] = "73c9a58f-6080-4ff1-9619-e0e3c0a35d7f"  # noqa: E501
        # pipeline_params["subscription_id"] = "0fe1cc35-0cfa-4152-97d7-5dfb45a8d4ba"  # noqa: E501
        # pipeline_params["resource_group"] = "kubeflowyo"  # noqa: E501
        # pipeline_params["workspace"] = "kubeflowyo-aml-ws"  # noqa: E501
        # exp = client.get_experiment(experiment_name=experiment_name)  # noqa: E501
        # client.run_pipeline(exp.id, job_name=pipeline_name, pipeline_package_path=pipeline_file, params=pipeline_params, pipeline_id="81ccc728-d6a0-4260-b6f7-21f20779c640")  # noqa: E501

    except TypeError as err:
        print("An error related to this issue https://github.com/kubeflow/pipelines/issues/3441 {0}".format(err))  # noqa: E501
    # pipeline_version = client.pipeline_uploads.upload_pipeline_version(pipeline_file,  # noqa: E501  # noqa: E501
    #                                                                    name="Version1",  # noqa: E501  # noqa: E501
    #                                                                    pipelineid=pipeline.id)  # noqa: E501  # noqa: E501


if __name__ == '__main__':
    main()
