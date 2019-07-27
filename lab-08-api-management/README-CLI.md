
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
az apim create --resource-group "rg1" --name "apimService1" --publisher-email \
"apim@autorestsdk.com" --publisher-name "autorestsdk" --sku-name "Developer" \
--sku-capacity "1" --location "Central US"
```

## Step 1 - Create Api

```
az apim api create --resource-group "rg1" --service-name "apimService1" --api-id \
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

## Step XX - Work with API Properties

To create new API property execute following command:

```
az apim property create --resource-group "rg1" --service-name "apimService1" --prop-id \
"testprop2" --secret true --display-name "prop3name" --value "propValue"
```

The response looks as follows:

```
{
  "displayName": "prop3name",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/properties/testprop2",
  "name": "testprop2",
  "resourceGroup": "rg1",
  "secret": true,
  "tags": null,
  "type": "Microsoft.ApiManagement/service/properties",
  "value": "propValue"
}
```

## Step XX - API Operation

### Create API Operation

```
az apim api operation create --resource-group "rg1" --service-name "apimService1" \
--api-id "petstore" --operation-id "newoperations" --description \
"This can only be done by the logged in user." --display-name "createUser2" --method \
"POST" --url-template "/user1"
```

```
{
  "description": "This can only be done by the logged in user.",
  "displayName": "createUser2",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apis/petstore/operations/newoperations",
  "method": "POST",
  "name": "newoperations",
  "policies": null,
  "request": {
    "description": null,
    "headers": [],
    "queryParameters": [],
    "representations": []
  },
  "resourceGroup": "rg1",
  "responses": [],
  "templateParameters": [],
  "type": "Microsoft.ApiManagement/service/apis/operations",
  "urlTemplate": "/user1"
}
```

> Renamed --api-id to "petstore"

### Create API Operation Policy

```
az apim api operation policy create --resource-group "rg1" --service-name \
"apimService1" --api-id "petstore" --operation-id \
"newoperations" --policy-id "policy" --value "<policies> <inbound /> <backend>
    <forward-request />  </backend>  <outbound /></policies>" --format "xml"
```

```
{
  "format": "xml",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apis/petstore/operations/newoperations/policies/policy",
  "name": "policy",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/apis/operations/policies",
  "value": "<policies>\r\n\t<inbound />\r\n\t<backend>\r\n\t\t<forward-request />\r\n\t</backend>\r\n\t<outbound />\r\n</policies>"
}
```

> Needed to change --operation-id to "newoperations" inside xml and --api-id to "petstore"

### Create API Policy

```
az apim policy create --resource-group "rg1" --service-name "apimService1" --policy-id \
"policy" --value "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\
n  </backend>\r\n  <outbound />\r\n</policies>" --format "xml"
```

```
{
  "format": "xml",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/policies/policy",
  "name": "policy",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/policies",
  "value": "<policies>\\r\\n  <inbound />\\r\\n  <backend>\\r\\n    <forward-request />\\r        n  </backend>\\r\\n  <outbound />\\r\\n</policies>"
}
```

### Create API Diagnostic

az apim api diagnostic create --resource-group "rg1" --service-name "apimService1" \
--api-id "petstore" --diagnostic-id "applicationinsights" --always-log \
"allErrors" --logger-id "/loggers/myloggerins"

> This needs logger 
> /loggers/..... --> renamed to "/loggers/mylogger"
> Diagnostic does not accept AzureEventHub logger

{
  "alwaysLog": "allErrors",
  "backend": null,
  "enableHttpCorrelationHeaders": true,
  "frontend": null,
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apis/petstore/diagnostics/applicationinsights",
  "loggerId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/loggers/myloggerins",
  "name": "applicationinsights",
  "resourceGroup": "rg1",
  "sampling": null,
  "type": "Microsoft.ApiManagement/service/apis/diagnostics"
}

## Create Diagnostic

        az apim diagnostic create --resource-group "rg1" --service-name "apimService1" \
        --diagnostic-id "applicationinsights" --always-log "allErrors" --logger-id \
        "/loggers/myloggerins" --debug

{
  "alwaysLog": "allErrors",
  "backend": null,
  "enableHttpCorrelationHeaders": true,
  "frontend": null,
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/diagnostics/applicationinsights",
  "loggerId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/loggers/myloggerins",
  "name": "applicationinsights",
  "resourceGroup": "rg1",
  "sampling": null,
  "type": "Microsoft.ApiManagement/service/diagnostics"
}

## Create Logger

First you have to create eventhub namespace:

```
az eventhubs namespace create --resource-group rg1 --name myeventhubzysysy --location \
westus --tags tag1=value1 tag2=value2 --sku Standard --enable-auto-inflate False --maximum-throughput-units 21
```

> original example was not broken correctly
> unit must be <=20 (was 30)
> "Cannot set MaximumThroughputUnits property if AutoInflate is not enabled"
> Name must be random

```
{
  "createdAt": "2019-07-25T13:22:27.107000+00:00",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.EventHub/namespaces/myeventhubzysysy",
  "isAutoInflateEnabled": true,
  "kafkaEnabled": false,
  "location": "West US",
  "maximumThroughputUnits": 20,
  "metricId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:myeventhubzysysy",
  "name": "myeventhubzysysy",
  "provisioningState": "Succeeded",
  "resourceGroup": "rg1",
  "serviceBusEndpoint": "https://myeventhubzysysy.servicebus.windows.net:443/",
  "sku": {
    "capacity": 1,
    "name": "Standard",
    "tier": "Standard"
  },
  "tags": {
    "tag1": "value1",
    "tag2": "value2"
  },
  "type": "Microsoft.EventHub/Namespaces",
  "updatedAt": "2019-07-25T13:23:17.117000+00:00"
}
```

```
az eventhubs eventhub create --resource-group rg1 --namespace-name myeventhubzysysy \
--name myeventhub --message-retention 4 --partition-count 15
```

```
{
  "captureDescription": null,
  "createdAt": "2019-07-25T13:25:28.963000+00:00",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.EventHub/namespaces/myeventhubzysysy/eventhubs/myeventhub",
  "location": "West US",
  "messageRetentionInDays": 4,
  "name": "myeventhub",
  "partitionCount": 15,
  "partitionIds": [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14"
  ],
  "resourceGroup": "rg1",
  "status": "Active",
  "type": "Microsoft.EventHub/Namespaces/EventHubs",
  "updatedAt": "2019-07-25T13:25:29.380000+00:00"
}
```

### Create Authorization Rule

az eventhubs eventhub authorization-rule create --resource-group rg1 \
--namespace-name myeventhubzysysy --eventhub-name myeventhub --name myauthorule --rights Send

{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.EventHub/namespaces/myeventhubzysysy/eventhubs/myeventhub/authorizationRules/myauthorule",
  "location": "West US",
  "name": "myauthorule",
  "resourceGroup": "rg1",
  "rights": [
    "Send"
  ],
  "type": "Microsoft.EventHub/Namespaces/EventHubs/AuthorizationRules"
}

### Get Keys

 az eventhubs eventhub authorization-rule keys list --resource-group rg1 \
 --namespace-name myeventhubzysysy --eventhub-name myeventhub --name myauthorule

{
  "aliasPrimaryConnectionString": null,
  "aliasSecondaryConnectionString": null,
  "keyName": "myauthorule",
  "primaryConnectionString": "Endpoint=sb://myeventhubzysysy.servicebus.windows.net/;SharedAccessKeyName=myauthorule;SharedAccessKey=dlnQ5grFrcTPvj+mznKUlb+BzD5wFpwxyvPMa21ddIs=;EntityPath=myeventhub",
  "primaryKey": "dlnQ5grFrcTPvj+mznKUlb+BzD5wFpwxyvPMa21ddIs=",
  "secondaryConnectionString": "Endpoint=sb://myeventhubzysysy.servicebus.windows.net/;SharedAccessKeyName=myauthorule;SharedAccessKey=zY/rGgpruNGaQzQidd+nTbTw8zKObaZTNBFqMx6dqzg=;EntityPath=myeventhub",
  "secondaryKey": "zY/rGgpruNGaQzQidd+nTbTw8zKObaZTNBFqMx6dqzg="
}

### Create Logger

az apim logger create --resource-group "rg1" --service-name "apimService1" --logger-id \
"mylogger" --logger-type "azureEventHub" --description "adding a new logger" --credentials "{\"name\":\"myeventhub\",\"connectionString\": \"Endpoint=sb://myeventhubzysysy.servicebus.windows.net/;SharedAccessKeyName=myauthorule;SharedAccessKey=zY/rGgpruNGaQzQidd+nTbTw8zKObaZTNBFqMx6dqzg=;EntityPath=myeventhub\"}"

{
  "credentials": {
    "connectionString": "{{Logger-Credentials-5d39b3464187911230654d5a}}",
    "name": "myeventhub"
  },
  "description": "adding a new logger",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/loggers/mylogger",
  "isBuffered": true,
  "loggerType": "azureEventHub",
  "name": "mylogger",
  "resourceGroup": "rg1",
  "resourceId": null,
  "type": "Microsoft.ApiManagement/service/loggers"
}

> This needs to be less complex (name, endpoint pramameters?)

> Create logger from insights

az apim logger create --resource-group "rg1" --service-name "apimService1" --logger-id \
"myloggerins" --logger-type "applicationInsights" --description "adding a new logger" --credentials "{\"instrumentationKey\":\"0c5fa0bc-386c-406b-92bd-ffbd862f8a1d\"}"

{
  "credentials": {
    "instrumentationKey": "{{Logger-Credentials-5d39b9b74187911230654d5d}}"
  },
  "description": "adding a new logger",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/loggers/myloggerins",
  "isBuffered": true,
  "loggerType": "applicationInsights",
  "name": "myloggerins",
  "resourceGroup": "rg1",
  "resourceId": null,
  "type": "Microsoft.ApiManagement/service/loggers"
}

## Step XX - Create Backend

```
az apim backend create --resource-group "rg1" --service-name "apimService1" \
--backend-id "sfbackend" --description "Service Fabric Test App 1" --url \
"fabric:/mytestapp/mytestservice" --protocol "http"
```

```
{
  "credentials": null,
  "description": "Service Fabric Test App 1",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/backends/sfbackend",
  "name": "sfbackend",
  "properties": null,
  "protocol": "http",
  "proxy": null,
  "resourceGroup": "rg1",
  "resourceId": null,
  "title": null,
  "tls": null,
  "type": "Microsoft.ApiManagement/service/backends",
  "url": "fabric:/mytestapp/mytestservice"
}
```

## Step XX - Adding Certificate

```
az apim certificate create --resource-group "rg1" --service-name "apimService1" \
--certificate-id "tempcert" --data \
"MIIDsTCCApmgAwIB6s+k2it5iRCiWZXKgA4AsCQGRTUDQ==" --password \
"somepassword"
```

> This sample needs to be tested with proper certificate

## Step XX - Create Versionset

```
az apim api-version-set create --resource-group "rg1" --service-name "apimService1" \
--version-set-id "api1" --description "Version configuration" --display-name "api set 1" \
--versioning-scheme "Segment"
```

```
{
  "description": "Version configuration",
  "displayName": "api set 1",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/apiVersionSets/api1",
  "name": "api1",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/apiVersionSets",
  "versionHeaderName": null,
  "versionQueryName": null,
  "versioningScheme": "Segment"
}
```

## Step XX - Manage Users and Groups

```
az apim user create --resource-group "rg1" --service-name "apimService1" --user-id \
"foobar" --email "foobar@outlook.com" --first-name "foo" --last-name \
"bar" --confirmation "signup"
```

```
{
  "email": "foobar@outlook.com",
  "firstName": "foo",
  "groups": [
    {
      "builtIn": true,
      "description": "Developers is a built-in group. Its membership is managed by the system. Signed-in users fall into this group.",
      "displayName": null,
      "externalId": null,
      "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/groups/developers",
      "name": "Developers",
      "resourceGroup": "rg1",
      "type": "system"
    }
  ],
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/users/foobar",
  "identities": [
    {
      "id": "foobar@outlook.com",
      "provider": "Basic"
    }
  ],
  "lastName": "bar",
  "name": "foobar",
  "note": null,
  "registrationDate": "2019-07-25T11:40:34.020000+00:00",
  "resourceGroup": "rg1",
  "state": "active",
  "type": "Microsoft.ApiManagement/service/users"
}
```

> Note: I have renamed original --user-id from "5931a75ae4bbd512288c680b" to "foobar". This should be propagated to REST API specs

### Create group

```
az apim group create --resource-group "rg1" --service-name "apimService1" --group-id \
"aadGroup" --display-name "NewGroup (samiraad.onmicrosoft.com)" --description \
"new group to test" --type "external" --external-id \
"aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d"
```

```
{
  "builtIn": false,
  "description": "new group to test",
  "displayName": "NewGroup (samiraad.onmicrosoft.com)",
  "externalId": null,
  "groupContractType": "custom",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/groups/aadGroup",
  "name": "aadGroup",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/groups"
}
```

### Assign User To Group

```
az apim group user create --resource-group "rg1" --service-name "apimService1" \
--group-id "aadGroup" --user-id "foobar"
```

```
{
  "email": "foobar@outlook.com",
  "firstName": "foo",
  "groups": [],
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/groups/aadGroup/users/foobar",
  "identities": [],
  "lastName": "bar",
  "name": "foobar",
  "note": null,
  "registrationDate": "2019-07-25T11:40:34.020000+00:00",
  "resourceGroup": "rg1",
  "state": "active",
  "type": "Microsoft.ApiManagement/service/groups/users"
}
```

> Note: I changed --group-id to aadGroup and --user-id to foobar

## Working with Tags

### Create a tag

```
az apim tag create --resource-group "rg1" --service-name "apimService1" --tag-id \
"tagId1" --display-name "tag1"
```

Response:

```
{
  "displayName": "tag1",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/tags/tagId1",
  "name": "tagId1",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/tags"
}
```

### Create API Tag Description

```
az apim api tag-description create --resource-group "rg1" --service-name "apimService1" \
--api-id "petstore" --tag-id "tagId1" --description "Some description that
    will be displayed for operation's tag if the tag is assigned to operation of the API" \
--external-docs-url "http://some.url/additionaldoc" --external-docs-description \
"Description of the external docs resource"
```

```
{
  "description": "Some description that\n    will be displayed for operation's tag if the tag is assigned to operation of the API",
  "displayName": "tag1",
  "externalDocsDescription": "Description of the external docs resource",
  "externalDocsUrl": "http://some.url/additionaldoc",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/tags/tagId1",
  "name": "tagId1",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/apis/tagDescriptions"
}
```

> Note: --api-id --> "petstore"

## Working with Notifications

### Create Notification

```
az apim notification create --resource-group "rg1" --service-name "apimService1" \
--name "RequestPublisherNotificationMessage" --title "My Notification"
```

```
{
  "description": "The following email recipients and users will receive email notifications about subscription requests for API products requiring approval.",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/notifications/RequestPublisherNotificationMessage",
  "name": "RequestPublisherNotificationMessage",
  "recipients": {
    "emails": [],
    "users": []
  },
  "resourceGroup": "rg1",
  "title": "Subscription requests (requiring approval)",
  "type": "Microsoft.ApiManagement/service/notifications"
}
```

> I think --title shouldn't be here

### Add E-mail to Notification

```
az apim notification recipient-email create --resource-group "rg1" --service-name \
"apimService1" --notification-name "RequestPublisherNotificationMessage" --email \
"foobar@live.com"
```

```
{
  "email": "foobar@live.com",
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/notifications/RequestPublisherNotificationMessage/recipientEmails/foobar@live.com",
  "name": "foobar@live.com",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/notifications/recipientEmails"
}
```

### Add User to Notification

```
az apim notification recipient-user create --resource-group "rg1" --service-name \
"apimService1" --notification-name "RequestPublisherNotificationMessage" --user-id \
"foobar"
```

```
{
  "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/notifications/RequestPublisherNotificationMessage/recipientUsers/foobar",
  "name": "foobar",
  "resourceGroup": "rg1",
  "type": "Microsoft.ApiManagement/service/notifications/recipientUsers",
  "userId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/users/foobar"
}
```

> Note: I changed --user-id to foobar to match created user

## Step XX - Working with Products

### Create Product

```
az apim product create --resource-group "rg1" --service-name "apimService1" \
--product-id "testproduct" --display-name "Test Template ProductName 4"
```


## Clean Up

```
az apim delete --resource-group "rg1" --name "apimService1"
```
