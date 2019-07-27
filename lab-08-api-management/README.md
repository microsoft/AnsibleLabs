
# Lab 08 - Api Management

## Summary of Lab

This lab covers Azure API Management service.
It's experimental in several ways:

- it uses modules deployed as Ansible Collection
- modules follow new light-weight pattern - they have no dependencies on Python SDK (except of msrestazure), meaning no additional packages have to be installed on the top of Ansible
- Modules are aligned with Azure CLI, meaning that Ansible modules have almost exactly the same parameter structure and that results in very smooth transition between Azure CLI and Ansible.
- Exactly the same examples are included in Azure CLI command module help, in Ansible documentation and in this lab.
- All the examples are imported from Azure REST API specification directly (any necessary fixes are backpropagated)

For **Azure CLI** equivalent of this lab instructions, open **README-AZURE-CLI.md**

## Pre-Requisites
    Before runing the playbook, you should install the collection by using the command - "mazer install azure.rm".

## Playbook 0 - Create Service
    ansible-playbook 00-create-image.yml
    Api Management Service Creation Task:
```
- name: ApiManagementCreateService
  azure.rm.apimanagementservice:
    resource_group: "{{ resource_group }}"
    name: "{{ service_name }}"
    publisher_email: "{{ publisher_email }}"
    publisher_name: "{{ publisher_name }}"
    sku_name: Developer
```

## Playbook 1 - Create Api
    ansible-playbook 01-create-api.yml
    Api Management Api Creation Task:
```
- name: ApiManagementCreateApi
  azure.rm.apimanagementapi:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    description: apidescription5200
    subscription_key_parameter_names:
      header: header4520
      query: query3037
    display_name: apiname1463
    service_url: 'http://newechoapi.cloudapp.net/api'
    path: newapiPath
    protocols:
      - https
      - http
```

## Playbook 2 - Create Api Schema
    ansible-playbook 02-create-api-schema.yml
    Api Management Api Schema Creation Task:
```
- name: ApiManagementCreateApiSchema
  azure.rm.apimanagementapischema:                  
    resource_group: myResourceGroup
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    schema_id: mySchema
    content_type: application/vnd.ms-azure-apim.xsd+xml
    document:
      value: "<s:schema elementFormDefault=qualified>"
```

## Playbook 3 - Create Api Tag Description
    ansible-playbook 03-create-api-tag-description.yml
    Api Management Api Tag Description Creation Task:
```
- name: ApiManagementCreateApiTagDescription
  azure.rm.apimanagementapitagdescription:                                                                                                                 
    resource_group: myResourceGroup
    service_name: "{{ resource_group }}"
    api_id: "{{ api_name }}"
    tag_id: tag1
    description: >-
      Some description that will be displayed for operation's tag if the tag is
      assigned to operation of the API
    external_docs_url: 'http://some.url/additionaldoc'
    external_docs_description: Description of the external docs resource
```

# Playbook 4 - Create Cache
    ansible-playbook 04-create-cache.yml
    Api Management Cache Creation Task:
```
- name: ApiManagementCreateCache
  azure.rm.apimanagementcache:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    cache_id: westindia
    description: Update Cache in west India
    connection_string: 'contoso5.redis.cache.windows.net,ssl=true,password=...'
    resource_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.Cache/Redis/contoso5
```

# Playbook 5 - Create Group
    ansible-playbook 05-create-group.yml
    Api Management Group Creation Task:
```
- name: ApiManagementCreateGroup
  azure.rm.apimanagementgroup:                                                                                                                              
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    group_id: myGroup
    display_name: temp group
```

# Playbook 6 - Create User
    ansible-playbook 06-create-user.yml
    Api Management User Creation Task:
```
- name: ApiManagementCreateUser
  azure.rm.apimanagementuser:                                                                                                                               
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    user_id: "{{ user_name }}"
    email: foobar@outlook.com
    first_name: foo
    last_name: bar
    confirmation: signup
```

# Playbook 7 - Create Group User
    ansible-playbook 07-create-group-user.yml
    Api Management Group User Creation Task:
```
- name: ApiManagementCreateGroupUser                                                                                      
  azure.rm.apimanagementgroupuser:                                                                                          
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    group_id: myGroup
    user_id: "{{ user_name }}"
    first_name: test
    last_name: user
```

# Playbook 8 - Create Notification
    ansible-playbook 08-create-notification.yml
    Api Management Notification Creation Task:
```
- name: ApiManagementCreateNotification 
  azure.rm.apimanagementnotification:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    name: RequestPublisherNotificationMessage
    title: Subscription requests (requiring approval
```

# Playbook 9 - Create Notification Recipient Email
    ansible-playbook 09-create-notification-recipient-email.yml
    Api Management Notification Recipient Email Creation Task:
```
- name: ApiManagementCreateNotificationRecipientEmail
  azure.rm.apimanagementnotificationrecipientemail:                                                                         
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    notification_name: RequestPublisherNotificationMessage
    email: myRecipientEmail
```

# Playbook 10 - Create Notification Recipient User
    ansible-playbook 10-create-notification-recipient-user.yml
    Api Management Notification Recipient User Creation Task:
```
- name: ApiManagementCreateNotificationRecipientUser
  azure.rm.apimanagementnotificationrecipientuser:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    notification_name: RequestPublisherNotificationMessage
    user_id: "{{ user_name }}"
```

# Playbook 11 - Create Open Id Connect Provider
    ansible-playbook 11-create-open-id-connect-provider.yml
    Api Management Open Id Connect Provider Creation Task:
```
- name: ApiManagementCreateOpenIdConnectProvider
  azure.rm.apimanagementopenidconnectprovider:                                                                             
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    opid: myOpenidConnectProvider
    display_name: templateoidprovider3
    metadata_endpoint: 'https://oidprovider-template3.net'
    client_id: oidprovidertemplate3
```

# Playbook 12 - Create Product
    ansible-playbook 12-create-product.yml
    Api Management Product Creation Task:
```
- name: ApiManagementCreateProduct
  azure.rm.apimanagementproduct:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    product_id: myProduct
    display_name: Test Template ProductName
```

# Playbook 13 - Create Product Api
    ansible-playbook 13-create-product-api.yml
    Api Management Product Api Creation Task:
```
- name: ApiManagementCreateProductApi
  azure.rm.apimanagementproductapi:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    product_id: myProduct
    api_id: "{{ api_name }}"
    path: newapiPath
```

# Playbook 14 - Create Policy
    ansible-playbook 14-create-policy.yml
    Api Management Policy Creation Task:
```
- name: ApiManagementCreatePolicy
  azure.rm.apimanagementpolicy:                                                                                             
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    policy_id: policy
    value: "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
    format: xml
```

# Playbook 15 - Create Product Policy
    ansible-playbook 15-create-product-policy.yml
    Api Management Product Policy Creation Task:
```
- name: ApiManagementCreateProductPolicy
  azure.rm.apimanagementproductpolicy:                                                                                      
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    product_id: myProduct
    policy_id: policy
    value: "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
    format: xml
```

# Playbook 16 - Create Product Group
    ansible-playbook 16-create-product-group.yml
    Api Management Product Group Creation Task:
```
- name: ApiManagementCreateProductGroup                                                                                   
  azure.rm.apimanagementproductgroup:                                                                                       
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    product_id: myProduct
    group_id: myGroup
    display_name: EchoApi
```

# Playbook 17 - Create Property
    ansible-playbook 17-create-property.yml
    Api Management Property Creation Task:
```
- name: ApiManagementCreateProperty
  azure.rm.apimanagementproperty:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    prop_id: myProperty                                                                                                     
    secret: true
    display_name: prop3name
    value: propValue
```

# Playbook 18 - Create Tag
    ansible-playbook 18-create-tag.yml
    Api Management Tag Creation Task:
```
- name: ApiManagementCreateTag
  apimanagementtag:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    tag_id: myTag
    display_name: tag1
```