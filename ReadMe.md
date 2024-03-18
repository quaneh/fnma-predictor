# FNMA Mortgage Default Predictor

The purpose of this project is to practice training a model and deploying it in a production environment.

## Model Training

The [FNMA Predictor](fnma_predictor.ipynb) notebook contains a rundown of how to train and save the model.

## Creating an API

We wrap the model in a simple [Flask API](app.py)

Our API has two simple endpoints, one for checking that the API is running, and the other for making predictions.

We also create a [data model](data_model/application_details.py), to verify that all of the necessary mortage application details are sent to the API each time it is called.

After building the API, the app is Dockerised.

## Dockerisation

We build a Docker image and run the image to test it locally.

The [Dockerfile](Dockerfile) is quite straightforward. It specifies the base image, loads Pipfile and installs libraries, and runs the Gunicorn server.

We build and run the image with the following commands:

```docker build --platform linux/amd64 -t default-predictor .```

We map port 80 on the Docker image to our local port 80 when running it:

```docker run -dp 80:80 default-predictor```

## Deploy to Amazon ECS

Now we need to deploy our container image to Amazon ECS.

First we create a repository (also called default-predictor) on ECR.
Then, we retreive our AWS credentials:

```aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin <my_amazon_acc_no>.dkr.ecr.ap-southeast-2.amazonaws.com```

Tag our Docker image:

```docker tag default-predictor:latest <my_amazon_acc_no>.dkr.ecr.ap-southeast-2.amazonaws.com/default-predictor:latest```

And push the image to the repository

```docker push <my_amazon_acc_no>.dkr.ecr.ap-southeast-2.amazonaws.com/default-predictor:latest```

After this, we need to carry out three more steps:

1. Create an IAM Execution Role.
    
    _Go to IAM --> Create Role --> Elastic Container Service Task --> AmazonElasticContainerServiceTaskExecutionRolePolicy_

2. Create a Security Group.
    
    _Go to EC2 --> Security Groups --> Create Group --> Add Inbound Rule on Port 80_

3. Create an ECS Cluster.
    
    _Choose AWS Fargate Cluster_

4. Create a Task Definition.
    
    _Task Role: None --> Executor Role: AmazonElasticContainerServiceTaskExecutionRolePolicy_

5. Run the Task.

Your API will now be running on ECS and can be accessed at the public URL provided.