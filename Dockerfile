# ref https://github.com/tebeka/pythonwise/blob/master/docker-miniconda/Dockerfile
FROM ubuntu:18.04

# System packages
RUN apt-get update && apt-get install -y curl

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# install git, vim and nano
RUN apt update && apt install -y git && apt install vim nano -y

# switch workdir to source folder /usr/src
WORKDIR /usr/src

# install conda env
COPY environment.yml .
RUN conda env create -f environment.yml


# Pull the environment name out of the environment.yml
ARG conda_env_name=nyc_airbnb_dev
RUN echo "source activate $conda_env_name" > ~/.bashrc
ENV PATH /opt/conda/envs/$conda_env_name/bin:$PATH
