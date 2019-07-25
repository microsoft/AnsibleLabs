
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
