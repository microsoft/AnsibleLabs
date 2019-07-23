# Ansible Deployment Labs for Microsoft Azure 

This is a collection of Ansible Labs originally presented at Red Hat Summit 2019. All labs perform various actions on Microsoft Azure using Ansible. Ansible >= 2.8 is required as well as the Ansible Modules for Azure.

![Cloud Workshop](./images/microsoft-cloud-workshop-mcw-logo.png)

<b>Deploy and scale Microsoft Azure infrastructures and applications with Red Hat Ansible Automation.</b>
<HR>
<b>Attendees will have hands-on access to Azure to perform the following tasks which build on one another:</b>

	* Lab 1: Deploying applications with AKS
	* Lab 2: Configuring a serverless application using Azure Functions
	* Lab 3: Building an HDInsight Cluster and performing Big Data queries
	* Lab 4: Provisioning an MPIO-Capable HPC Infrastructure and testing Infiniband Latency
	* Lab 5: Configuring an IaaS application on a virtual machine, connecting MySQL and scaling
	* Lab 6: Containerize a NodeJS Application, load to ACR and deploy as an Azure Web App
	* Lab 7: Using Azure Shared Image Gallery
	* Lab 9: Leveraging Azure Management Groups to control Azure subscriptions
	* Lab 10: Azure Migration at scale
	* Lab 11: Azure REST API Management

<b>These hands-on labs will showcase the following:</b>

	* Working with the Azure Linux CLI
	* Connecting Ansible to Microsoft Azure
	* Create a Red Hat Enterprise Linux virtual machine in Azure using the Azure Marketplace.
	* Create and configure an Azure MySQL PaaS database.
	* Deploy an application on the RHEL virtual machine which utilizes the Azure MySQL PaaS database.
	* Generalize the RHEL virtual machine image to create a golden image template for group deployments.
	* Scale out the application to multiple servers using Azure virtual machine scale sets.
	* Big data workloads using Azure HDInsight.
	* High-performance computing using Azure virtual machine infiniband interconnects.
	* Hosting an Azure Application Service
	* Running a containerized application using Azure Web Apps
	* Launching an application in Azure Kubernetes Service (AKS).
	* Serverless applications using Azure functions.

Original content created by: [Stuart Kirk](https://github.com/stuartatmicrosoft) & [Zim Kalinowski](https://github.com/zikalino) with assistance from [Steve Roach](https://github.com/grandparoach), [Sasha Rosenbaum](https://github.com/divineops), [Harold Wong](https://github.com/haroldwongms), [Jason De Lorme](https://github.com/ms-jasondel), [Michael Yen-Chi Ho](https://github.com/yenchiho), [Patrick Rutledge](https://github.com/rut31337)

Base implementation for Function App Docker container comes from here:

https://github.com/Azure/azure-functions-docker-python-sample

The content of this program can be re-delivered, on request, to any Microsoft customer seeking to deploy open source workloads on Azure.  Please contact stkirk@microsoft.com for additional details and to coordinate delivery of the program.
