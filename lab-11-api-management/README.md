
# Lab 11 - Api Management

## Summary of Lab

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
