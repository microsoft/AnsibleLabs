
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

## Step XX - Work with API Properties

To create new API property execute following command:

```
az apimgmt property create --resource-group "rg1" --service-name "apimService1" --prop-id \
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

## Step XX - Create Versionset

```
az apimgmt apiversionset create --resource-group "rg1" --service-name "apimService1" \
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
az apimgmt user create --resource-group "rg1" --service-name "apimService1" --user-id \
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
az apimgmt group create --resource-group "rg1" --service-name "apimService1" --group-id \
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
az apimgmt group user create --resource-group "rg1" --service-name "apimService1" \
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

Create a tag:

```
az apimgmt tag create --resource-group "rg1" --service-name "apimService1" --tag-id \
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

## Working with Notifications

### Create Notification

```
az apimgmt notification create --resource-group "rg1" --service-name "apimService1" \
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
az apimgmt notification recipientemail create --resource-group "rg1" --service-name \
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
az apimgmt notification recipientuser create --resource-group "rg1" --service-name \
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
az apimgmt product create --resource-group "rg1" --service-name "apimService1" \
--product-id "testproduct" --display-name "Test Template ProductName 4"
```


## Clean Up

```
az apimgmt delete --resource-group "rg1" --name "apimService1"
```
