#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

FROM python:3.7

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git, process tools, lsb-release (common in install instructions for CLIs) installed
    && apt-get -y install git iproute2 procps lsb-release \
    #
    # Install pylint
    && pip --disable-pip-version-check --no-cache-dir install pylint \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
RUN pip install uwsgi\
    && pip install Django\
    #
    #for run manage.py runscript
    && pip install django-extensions\
    #
    #for run_client_jobs
    && pip install croniter\
    #
    #for client and worker use faktory service
    && pip install faktory\
    && pip install BeautifulSoup4\
    && pip install requests\
    #for google api get api key by .env file by using dotenv module
    && pip install googlemaps\
    && pip install python-dotenv
    


ADD ./mysite /map/src/mysite
WORKDIR /map/src/mysite

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=
