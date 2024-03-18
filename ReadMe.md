# FNMA Mortgage Default Predictor

The purpose of this project is to practice training a model and deploying it in a production environment.

## Model Training

The [FNMA Predictor](fnma_predictor.ipynb) notebook contains a rundown of how to train and save the model.

After training the model, the model is Dockerised.

## Dockerisation

We build a Docker image and run the image to test it locally.

The [Dockerfile](Dockerfile) is quite straightforward. It specifies the base image, loads Pipfile and installs libraries, and runs the Gunicorn server.

We build and run the image with the following commands:

```docker build --platform linux/amd64 -t default-predictor .```

We map port 80 on the Docker image to our local port 80 when running it:

```docker run -dp 80:80 default-predictor```

