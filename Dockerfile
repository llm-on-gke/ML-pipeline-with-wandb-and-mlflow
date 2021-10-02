FROM ubuntu:18.04

# install curl, git, and vim
RUN apt-get update && apt-get install -y curl git vim

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

RUN apt update && apt install -y git vim

# switch workdir to source folder /usr/src
WORKDIR /usr/src

# install conda env
COPY environment.yml .
RUN conda env create -f environment.yml

# activate the conda env
ARG conda_env_name=nyc_airbnb_dev
RUN echo "source activate $conda_env_name" > ~/.bashrc
ENV PATH /opt/conda/envs/$conda_env_name/bin:$PATH

# fetch data, run eda
# RUN mlflow run . -P steps=download
# RUN mlflow run src/eda
