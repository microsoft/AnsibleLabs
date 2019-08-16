
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
    Api Management Api Schema Creation Task:
```
- name: ApiManagementCreateApiSchema
  azure.rm.apimanagementapischema:                  
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    schema_id: mySchema
    content_type: application/vnd.ms-azure-apim.xsd+xml
    document:
      value: "<s:schema elementFormDefault=qualified>"
```
    Api Management Tag Creation Task:
```
- name: ApiManagementCreateTag
  apimanagementtag:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    tag_id: myTag
    display_name: tag1
```
    Api Management Api Tag Description Creation Task:
```
- name: ApiManagementCreateApiTagDescription
  azure.rm.apimanagementapitagdescription:                                                                                                                 
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    tag_id: tag1
    description: >-
      Some description that will be displayed for operation's tag if the tag is
      assigned to operation of the API
    external_docs_url: 'http://some.url/additionaldoc'
    external_docs_description: Description of the external docs resource
```
    Api Management Api Release Creation Task:
```
- name: ApiManagementCreateApiRelease                                                                                     
  azure.rm.apimanagementapirelease:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    papi_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqy/apis/myApi
    release_id: myRelease
    notes: yahooagain
```
    Api Management Api Version Set Creation Task:
```
- name: ApiManagementCreateApiVersionSet
  azure.rm.apimanagementapiversionset:                                                                                      
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    version_set_id: myApiVersionSet
    description: Version configuration
    display_name: "api set 1"
    versioning_scheme: Segment
```

# Playbook 2 - Create Diagnostic
    ansible-playbook 02-create-diagnostic.yml
    Api Management Logger Creation Task:
```
- name: ApiManagementCreateAILogger
  azure.rm.apimanagementlogger:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    logger_id: myLogger
    logger_type: applicationInsights
    description: adding a new logger
    credentials:
      instrumentationKey: 714c6d94-e036-4d07-8b0b-979f4b63bc65
```
    Api Management Diagnostic Creation Task:
```
 - name: ApiManagementCreateDiagnostic
  azure.rm.apimanagementdiagnostic:                                                                                         
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    diagnostic_id: applicationinsights
    always_log: allErrors
    logger_id: /loggers/myLoggerId
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
```
    Api Management Api Diagnostic Creation Task:
```
- name: ApiManagementCreateApiDiagnostic
  azure.rm.apimanagementapidiagnostic:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    diagnostic_id: applicationinsights
    always_log: allErrors
    logger_id: /loggers/myLoggerId
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
```

# Playbook 3 - Create Group User
    ansible-playbook 03-create-group-user.yml
    Api Management Group Creation Task:
```
- name: ApiManagementCreateGroup
  azure.rm.apimanagementgroup:                                                                                                                              
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    group_id: myGroup
    display_name: temp group
```
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

# Playbook 4 - Create Policy
    ansible-playbook 04-create-policy.yml
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
    Api Management Api Policy Creation Task:
```
- name: ApiManagementCreateApiPolicy
  azure.rm.apimanagementapipolicy:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    policy_id: policy
    value: "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
s    format: xml
```

# Playbook 5 - Create Product
    ansible-playbook 05-create-product.yml
    Api Management Product Creation Task:
```
- name: ApiManagementCreateProduct
  azure.rm.apimanagementproduct:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    product_id: myProduct
    display_name: Test Template ProductName
    pstate: published
```
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

# Playbook 6 - Create Api Operation
    ansible-playbook 06-create-api-operation.yml
    Api Management Api Operation Creation Task:
```
- name: ApiManagementCreateApiOperation
  azure.rm.apimanagementapioperation:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    operation_id: myOperation
    template_parameters: []
    description: This can only be done by the logged in user.
    request:
      description: Created user object
      query_parameters: []
      headers: []
      representations:
        - content_type: application/json
          schema_id: mySchema
          type_name: User
    responses:
      - status_code: '200'
        description: successful operation
        representations:
          - content_type: application/xml
          - content_type: application/json
        headers: []
    display_name: createUser2
    method: POST
    url_template: /user1
```
    Api Management Api Operation Policy Creation Task:
```
- name: ApiManagementCreateApiOperationPolicy
  azure.rm.apimanagementapioperationpolicy:                                                                                
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    operation_id: myOperation
    policy_id: policy
    value: "<policies>\r\n  <inbound />\r\n  <backend>\r\n    <forward-request />\r\n  </backend>\r\n  <outbound />\r\n</policies>"
    format: xml
```

# Playbook 7 - Create Api Issue
    ansible-playbook 07-create-api-issue.yml
    Api Management Api Issue Creation Task:
```
- name: ApiManagementCreateApiIssue
  azure.rm.apimanagementapiissue:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    issue_id: "{{ issue_name }}"
    created_date: '2018-02-01T22:21:20.467Z'
    pstate: open
    title: New API issue
    description: New API issue description
    papi_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqy/apis/myApi
    user_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqy/users/myUser
```
    Api Management Api Issue Attachment Creation Task:
```
- name: ApiManagementCreateApiIssueAttachment
  azure.rm.apimanagementapiissueattachment:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    issue_id: "{{ issue_name }}"
    attachment_id: myAttachment
    title: Issue attachment.
    content_format: image/jpeg
    content: IEJhc2U2NA==
```
    Api Management Api Issue Comment Creation Task:
```
- name: ApiManagementCreateApiIssueComment
  azure.rm.apimanagementapiissuecomment:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    api_id: "{{ api_name }}"
    issue_id: "{{ issue_name }}"
    comment_id: myComment
    text: Issue comment.
    created_date: '2018-02-01T22:21:20.467Z'
    user_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqy/users/myUser
```

# Playbook 8 - Create Cache
    ansible-playbook 08-create-cache.yml
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

# Playbook 9 - Create Notification
    ansible-playbook 09-create-notification.yml
    Api Management Notification Creation Task:
```
- name: ApiManagementCreateNotification 
  azure.rm.apimanagementnotification:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    name: RequestPublisherNotificationMessage
    title: Subscription requests (requiring approval
```
    Api Management Notification Recipient Email Creation Task:
```
- name: ApiManagementCreateNotificationRecipientEmail
  azure.rm.apimanagementnotificationrecipientemail:                                                                         
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    notification_name: RequestPublisherNotificationMessage
    email: myRecipientEmail
```
    Api Management Notification Recipient User Creation Task:
```
- name: ApiManagementCreateNotificationRecipientUser
  azure.rm.apimanagementnotificationrecipientuser:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    notification_name: RequestPublisherNotificationMessage
    user_id: "{{ user_name }}"
```

# Playbook 10 - Create Authorization Server
    ansible-playbook 10-create-authorization-server.yml
    Api Management Authorization Server Creation Task:
```
- name: ApiManagementCreateAuthorizationServer
  azure.rm.apimanagementauthorizationserver:                                                                                \
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    authsid: myAuthorizationServer
    description: test server
    authorization_methods:
      - GET
    token_endpoint: 'https://www.contoso.com/oauth2/token'
    support_state: true
    default_scope: read write
    bearer_token_sending_methods:
      - authorizationHeader
    client_secret: '2'
    resource_owner_username: un
    resource_owner_password: pwd
    display_name: test2
    client_registration_endpoint: 'https://www.contoso.com/apps'
    authorization_endpoint: 'https://www.contoso.com/oauth2/auth'
    grant_types:
      - authorizationCode
      - implicit
    client_id: '1'
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

# Playbook 12 - Create Backend
    ansible-playbook 11-create-backend.yml
    Api Management Backend Creation Task:
```
- name: ApiManagementCreateBackendServiceFabric
  azure.rmapimanagementbackend:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    backend_id: myBackend
    description: description5308
    credentials:
      query:
        sv:
          - xx
          - bb
          - cc
      header:
        x-my-1:
          - val1
          - val2
      authorization:
        scheme: Basic
        parameter: opensesma
    proxy:
      url: 'http://192.168.1.1:8080'
      username: Contoso\admin
      password: opensesame
    tls:
      validate_certificate_chain: true
      validate_certificate_name: true
    url: 'https://backendname2644/'
    protocol: http
```

# Playbook 13 - Create Identity Provider
    ansible-playbook 17-create-identity-provider.yml
    Api Management Identity Provider Creation Task:
```
- name: ApiManagementCreateIdentityProvider
  azure.rm.apimanagementidentityprovider:                                                                                   
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    name: microsoft
    client_id: facebookid
    client_secret: facebookapplicationsecret
```

# Playbook 14 - Create Subscription
    ansible-playbook 15-create-subscription.yml
    Api Management Subscription Creation Task:
```
- name: ApiManagementCreateSubscription
  azure.rm.apimanagementsubscription:
    resource_group: "{{ resource_group }}"
    service_name: "{{ service_name }}"
    sid: testsub
    owner_id: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqy/users/myUser
    scope: /subscriptions/1c5b82ee-9294-4568-b0c0-b9c523bc0d86/resourceGroups/myResourceGroup/providers/Microsoft.ApiManagement/service/myServiceLqt/products/myProduct
    display_name: testsub
```

# Playbook 15 - Create Property
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
