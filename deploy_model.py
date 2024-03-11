import uuid
from azureml.core.model import InferenceConfig, Model
from azureml.core.environment import Environment
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.webservice import AciWebservice

# get a curated environment
env = Environment.get(
    workspace=ws,
    name="AzureML-sklearn-0.24.1-ubuntu18.04-py37-cpu-inference",
    version=1
)
env.inferencing_stack_version = 'latest'

# create deployment config i.e. compute resources
aciconfig = AciWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    tags={"data": "AppleQuality", "method": "sklearn"},
    description="Predict Apple Quality with sklearn",
)

# get the registered model
model = Model(ws, "sklearn_apple_model")

# create an inference config i.e. the scoring script and environment
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# deploy the service
service_name = "sklearn-apple-mlp-" + str(uuid.uuid4())[:4]
service = Model.deploy(
    workspace=ws,
    name=service_name,
    models=[model],
    inference_config=inference_config,
    deployment_config=aciconfig,
)

service.wait_for_deployment(show_output=True)
