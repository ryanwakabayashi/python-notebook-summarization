# FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel
#FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu22.04
FROM jupyter/scipy-notebook
#WORKDIR /app
#COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8888
#ENV NAME World
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]

# commands for building and running the docker image
#docker build -t my-jupyter .
#docker run --rm -p 8888:8888 -v C:\Users\ryanw\PycharmProjects\llama3-test:/app my-jupyter
