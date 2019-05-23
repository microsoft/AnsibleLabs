This repository hosts the instructions and neccessary artifacts for building and publishing Python Functions as a Docker container on Linux.

For comprehensive information about Python in Azure Functions, refer to the [azure-functions-python-worker](https://github.com/Azure/azure-functions-python-worker) repo.

# Getting Started

## Prerequisites

* [Git](https://git-scm.com/downloads)
* An active [Azure subscription](https://azure.microsoft.com/pricing/free-trial/?ref=microsoft.com&utm_source=microsoft.com&utm_medium=docs&utm_campaign=visualstudio)
* [Docker](https://docs.docker.com/get-started/#setup)
* A [Docker Hub account](https://docs.docker.com/docker-id/)

## Download the sample

In a terminal window, run the following command to clone the sample app repository to your local machine, then change to the directory that contains the sample code.

```bash
git clone https://github.com/Azure/azure-functions-docker-python-sample.git
cd azure-functions-docker-python-sample
```

## Understanding the environment

In the Git repository, take a look at the `Dockerfile`. This file describes the environment that is required to run Python functions on Linux. 

```dockerfile
# Base the image on the built-in Azure Functions Python image
FROM microsoft/azure-functions-python3.6:v2.0.11737-alpha

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt
```

## Build and deploy the custom image

To build and test your image locally, and deploy to Azure, follow the instructions here -

[Create a function on Linux using a custom image](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image#run-the-build-command)

## Configure storage

Azure Functions needs a storage account in order to run locally.

The best way to add this is to create a Storage Account in Azure and pass the connection string as an environment variable called `AzureWebJobsStorage` to the `docker run` command. 


``` bash
docker run -p 8080:80 -it -e AzureWebJobsStorage="{connection-string}" <docker-id>/mydockerimage:v1.0.0
```


# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
