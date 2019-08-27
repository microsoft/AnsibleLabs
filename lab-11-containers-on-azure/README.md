
# Lab 08 - Api Management

## Summary of Lab

## Pre-Requisites
    Before runing the playbook, you should install the collection by using the command - "mazer install azure.rm".

## Playbook 0 - Create OpenShift Managed Cluster
    ansible-playbook 00-create-openshift-managed-cluster.yml
    OpenShift Managed Cluster Creation Task:
```
- name: Create/Update OpenShift Managed Cluster
  azure.rm.openshiftmanagedcluster:
    resource_group: "{{ resource_group }}"
    name: myOpenShiftManagedCluster
    location: eastus
    open_shift_version: v3.11
    network_profile:
      vnet_cidr: 10.0.0.0/8
    router_profiles:
      - name: default
    master_pool_profile:
      name: master
      count: 3
      vm_size: Standard_D4s_v3
      subnet_cidr: 10.0.0.0/24
      os_type: Linux
    agent_pool_profiles:
      - name: infra
        count: 2
        vm_size: Standard_D4s_v3
        subnet_cidr: 10.0.0.0/24
        os_type: Linux
        role: infra
      - name: compute
        count: 4
        vm_size: Standard_D4s_v3
        subnet_cidr: 10.0.0.0/24
        os_type: Linux
        role: compute
    auth_profile:
      identity_providers:
        - name: Azure AD
          provider:
            kind: AADIdentityProvider
            clientId: "{{ client_id }}"
            secret: "{{ secret }}"
            tenantId: "{{ tenant_id }}"
```

