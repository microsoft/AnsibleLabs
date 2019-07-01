# Lab 7 - Shared Image Gallery

## Summary of Lab
In this exercise you will create a virtual machine using the shared image that you create. Initially, we will start by creating a custom image. Then, we will create shared image gallery and create shared image into this gallery. Finally, we will create a virtual machine using the shared image.

## Pre-Requisites
This Lab Exercise will assume that:
    You have added your Resource Group ID, Location, Source VM Name, Image Name, Shared Gallery Name, Shared Image Name, Shared Image Version and VM Name to the vars.yml file prior to executing this lab.

## Playbook 0 - Create Custom Image

    ansible-playbook 00-create-image.yml
    Resource Group Creation Task:
```
- name: Create resource group if doesn't exist
  azure_rm_resourcegroup:
    name: "{{ resource_group }}"
    location: "{{ location }}"
```
    Virtual Network Creation Task:
```
- name: Create virtual network
  azure_rm_virtualnetwork:
    resource_group: "{{ resource_group }}"
    name: "{{ virtual_network_name }}"
    address_prefixes: "10.0.0.0/16"
- name: Add subnet
  azure_rm_subnet:
    resource_group: "{{ resource_group }}"
    name: "{{ subnet_name }}"
    address_prefix: "10.0.1.0/24"
    virtual_network: "{{ virtual_network_name }}"
```
    Public IP Address Creation Task:
```
- name: Create public IP address
  azure_rm_publicipaddress:
    resource_group: "{{ resource_group }}"
    allocation_method: Static
    name: "{{ ip_name }}"
```
Virtual Network Inteface Cards Creation Task:
```
- name: Create virtual network inteface cards for VM A and B
  azure_rm_networkinterface:
    resource_group: "{{ resource_group }}"
    name: "{{ network_interface_name }}"
    virtual_network: "{{ virtual_network_name }}"
    subnet: "{{ subnet_name }}"
```
    Virtual Machine Creation Task:
```
- name: Create VM
  azure_rm_virtualmachine:
    resource_group: "{{ resource_group }}"
    name: "{{ source_vm_name }}"
    admin_username: testuser
    admin_password: "Password1234!"
    vm_size: Standard_B1ms
    network_interfaces: "{{ network_interface_name }}"
    image:
      offer: UbuntuServer
      publisher: Canonical
      sku: 16.04-LTS
      version: latest
- name: Generalize VM
  azure_rm_virtualmachine:
    resource_group: "{{ resource_group }}"
    name: "{{ source_vm_name }}"
    generalized: yes
```
    Custom Image Creation Task:
    In this task. we will use the azure_rm_image module. 
```
- name: Create custom image
  azure_rm_image:
    resource_group: "{{ resource_group }}"
    name: "{{ image_name }}"
    source: "{{ source_vm_name }}"
```
    After this playbook completes, you can visit the Azure Portal(https://portol.azure.com) and find the custom image in your resource group.

## Playbook 1 - Create Shared Image Gallery
    ansible-playbook 01-create-shared-image-gallery.yml
    Shared Image Gallery Creation Task:
    In this task, we will use the azure_rm_gallery module to create a shared image gallery. 
```
    - name: Create shared image gallery
      azure_rm_gallery:
        resource_group: "{{ resource_group }}"
        name: "{{ shared_gallery_name }}"
        location: "{{ location }}"
        description: This is the gallery description.
```
    Once again, visit the Azure Portal(https://portol.azure.com) and in your resource group you will see a new shared image gallery.

## Playbook 2 - Create Shared Image
    ansible-playbook 02-create-image.yml
    Shared Image Creation Task:
    In this task, we will use the azure_rm_galleryimage module to create a shared image in your gallery. 
```
    - name: Create shared image
      azure_rm_galleryimage:
        resource_group: "{{ resource_group }}"
        gallery_name: "{{ shared_gallery_name }}"
        name: "{{ shared_image_name }}"
        location: "{{ location }}"
        os_type: linux
        os_state: generalized
        identifier:
          publisher: myPublisherName
          offer: myOfferName
          sku: mySkuName
        description: Image Description  
```
    Gallery Image Version Creation Task: 
    In this task, we will use the azure_rm_galleryimageversion module to create a simple gallery image version. 
```
    - name: Create or update a simple gallery Image Version
      azure_rm_galleryimageversion:
        resource_group: "{{ resource_group }}"
        gallery_name: "{{ shared_gallery_name }}"
        gallery_image_name: "{{ shared_image_name }}"
        name: "{{ shared_image_version }}"
        location: "{{ location }}"
        publishing_profile:
          end_of_life_date: "2020-10-01t00:00:00+00:00"
          exclude_from_latest: yes
          replica_count: 3
          storage_account_type: Standard_LRS
          target_regions:
            - name: West US
              regional_replica_count: 1
            - name: East US
              regional_replica_count: 2
              storage_account_type: Standard_ZRS
          managed_image:
            name: "{{ shared_image_name }}"
            resource_group: "{{ resource_group }}"
```
    After this playbook completes, you can visit the Azure Portal(https://portol.azure.com). Open your resource group, and you can find your shared image gallery. From the gallery you can see the shared image that you just created. There is the resource id of the shared image. Copy the resource id and add it to your vars.yml file as 'image_id'. 


## Playbook 3 - Create Virtual Machine Using Shared Image
    ansible-playbook 03-create-vm-using-shared-image.yml
    Virtual Machine Creation Task:
    In this task, we will use the azure_rm_virtualmachine module to create a virtual machine using the shared image that we create in the pervious tasks.
```
    azure_rm_virtualmachine:
      resource_group: "{{ resource_group }}"
      name: "{{ vm_name }}"
      vm_size: Standard_DS1_v2
      admin_username: adminUser
      admin_password: PassWord01
      managed_disk_type: Standard_LRS
      image:
        id: "{{ image_id }}"
```
    After this playbook competes, you can visit the Azure Portal(https://portol.azure.com) and find the newly-created virtual machine in your resource group.



## Playbook 4 - Create Virtual Machine Scale Set Using Shared Image
    ansible-playbook 04-create-vmss-using-shared-image
    Virtual Machine Scale Set Creation Task:
```
  - name: Create VMSS using shared image
    azure_rm_virtualmachinescaleset:
      resource_group: "{{ resource_group }}"
      name: "{{ vmss_name }}"
      vm_size: Standard_DS1_v2
      capacity: 2
      virtual_network_name: "{{ virtual_network_name }}"
      upgrade_policy: Manual
      subnet_name: "{{ subnet_name }}"
      admin_username: adminUser
      admin_password: PassWord01
      managed_disk_type: Standard_LRS
      image:
        id: "{{ image_id }}"
```
    After this playbook competes, you can visit the Azure Portal(https://portol.azure.com) and find the newly-created virtual machine scale set in your resource group.

## Playbook 5 - Get Information
    ansible-playbook 05-get-info
    Gallery Information Get Task:
    In this task, we can get the information of the gallery. 
```
  - name: Get Shared Image Gallery Information
    azure_rm_gallery_info:
      resource_group: "{{ resource_group }}"
      name: "{{ shared_gallery_name }}"
```
    Shared Image Information Get Task:
    In this task, we can get the information of the shared image. 
```
  - name: Get Shared Image Information
    azure_rm_galleryimage_info:
      resource_group: "{{ resource_group }}"
      gallery_name: "{{ shared_gallery_name }}"
      name: "{{ shared_image_name }}"
```
    Shared Image Version Information Get Task:
    In this task, we can get the information of the shared image version.
```
  - name: Get Gallery Image Version Information
    azure_rm_galleryimageversion_info:
      resource_group: "{{ resource_group }}"
      gallery_name: "{{ shared_gallery_name }}"
      gallery_image_name: "{{ shared_image_name }}"
      name: "{{ shared_image_version }}"
```


## Playbook 6 - Delete Gallery
    ansible-playbook 06-delete-gallery
    Gallery Image Version Deletion Task:
```
  - name: Delete gallery Image Version.
    azure_rm_galleryimageversion:
      resource_group: "{{ resource_group }}"
      gallery_name: "{{ shared_gallery_name }}"
      gallery_image_name: "{{ shared_image_name }}"
      name: "{{ shared_image_version }}"
      absent: yes
```
    Gallery Image Deletion Task:
```
  - name: Delete gallery image
    azure_rm_galleryimage:
      resource_group: "{{ resource_group }}"
      gallery_name: "{{ shared_gallery_name }}"
      name: "{{ shared_image_name }}"
      absent: yes
```
    Gallery Deletion Task:
```
  - name: Delete a simple gallery.
    azure_rm_gallery:
      resource_group: "{{ resource_group }}"
      name: "{{ shared_gallery_name }}"
      absent: yes
```
    After this playbook competes, you can visit the Azure Portal(https://portol.azure.com) and find your image version, image and gallery being removed from your resource group.
