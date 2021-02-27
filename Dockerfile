# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /

# copy the dependencies file to the working directory
COPY requirements.txt /

# copy the content of the local src directory to the working directory
COPY . /

# install dependencies
RUN pip install -r requirements.txt

# Expose the prediction app through port 8501
EXPOSE 8501

# command to run on container start
CMD streamlit run main.py predictModel

# Steps - execute the following to containerize the model

# To build the docker image
# docker build -t heartdisease:latest .

# To run the prediction app from docker image
# docker run -p 8501:8501 heartdisease:latest

# To debug the docker image - optional
# docker run -it heartdisease bash

# To delete all containers including its volumes and images
# docker rm -vf $(docker ps -a -q)
# docker rmi -f $(docker images -a -q)


