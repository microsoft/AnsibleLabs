
# Lab 08 - Api Management

## Summary of Lab

This lab covers Azure API Management service.
It's experimental in several ways:

- it uses modules deployed as Ansible Collection
- modules follow new light-weight pattern - they have no dependencies on Python SDK (except of msrestazure), meaning no additional packages have to be installed on the top of Ansible
- Modules are aligned with Azure CLI, meaning that Ansible modules have almost exactly the same parameter structure and that results in very smooth transition between Azure CLI and Ansible.
- Exactly the same examples are included in Azure CLI command module help, in Ansible documentation and in this lab.
- All the examples are imported from Azure REST API specification directly (any necessary fixes are backpropagated)

## Pre-Requisites

## Step 0 - Create Service

```
az apimgmt create --resource-group "rg1" --name "apimService1" --publisher-email \
"apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Developer" \
--sku-capacity "1" --location "Central US"
```

## Step 1 - Create Api

```
az apimgmt api create --resource-group "rg1" --service-name "apimService1" --api-id \
"petstore" --path "petstore" --value "http://petstore.swagger.io/v2/swagger.json" \
--format "swagger-link-json" --protocols "[\"http\",\"https\"]" --display-name "Pet Store API"
```

You will see following response:

```
{
  "apiRevision": "1",
  "apiRevisionDescription": null,
  "apiType": null,
  "apiVersion": null,
  "apiVersionDescription": null,
  "apiVersionSet": null,
  "apiVersionSetId": null,
  "authenticationSettings": {
    "oAuth2": null,
    "openid": null,
    "subscriptionKeyRequired": null
  },
  "description": null,
  "displayName": "Pet Store API",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apis/petstore",
  "isCurrent": true,
  "isOnline": null,
  "name": "petstore",
  "path": "petstore",
  "protocols": [
    "http",
    "https"
  ],
  "resourceGroup": "rg1",
  "serviceUrl": null,
  "sourceApiId": null,
  "subscriptionKeyParameterNames": {
    "header": "Ocp-Apim-Subscription-Key",
    "query": "subscription-key"
  },
  "subscriptionRequired": null,
  "type": "Microsoft.ApiManagement/service/apis"
}
```



## Clean Up

```
az apimgmt delete --resource-group "rg1" --name "apimService1"
```
