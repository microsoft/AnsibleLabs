# Lab 7 - Shared Image Gallery

Summary of Lab
In this exercise you will create a virtual machine using the shared image that you create. Initially, we will start by creating a custom image. Then, we will create shared image gallery and create shared image into this gallery. Finally, we will create a virtual machine using the shared image.

Pre-Requisites
This Lab Exercise will assume that:
    You have added your Resource Group ID, Location, Source VM Name, Image Name, Shared Gallery Name, Shared Image Name, Shared Image Version and VM Name to the vars.yml file prior to executing this lab.

Playbook 0 - Create Custom Image
    ansible-playbook 00-create-image.yml
    Resource Group Creation Task:
    - name: Create resource group if doesn't exist
      azure_rm_resourcegroup:
        name: "{{ resource_group }}"
        location: "{{ location }}"
    Custom Image Creation Task:
    In this task. we will use the azure_rm_image module. 
    - name: Create custom image
      azure_rm_image:
        resource_group: "{{ resource_group }}"
        name: "{{ image_name }}"
        source: "{{ source_vm_name }}"
    After this playbook completes, you can visit the Azure Portal(https://portol.azure.com) and find the custom image in your resource group.

Playbook 1 - Create Shared Image Gallery
    ansible-playbook 01-create-shared-image-gallery.yml
    Shared Image Gallery Creation Task:
    In this task, we will use the azure_rm_gallery module to create a shared image gallery. 
    - name: Create shared image gallery
      azure_rm_gallery:
        resource_group: "{{ resource_group }}"
        name: "{{ shared_gallery_name }}"
        location: "{{ location }}"
        description: This is the gallery description.
    Once again, visit the Azure Portal(https://portol.azure.com) and in your resource group you will see a new shared image gallery.

Playbook 2 - Create Shared Image
    ansible-playbook 02-create-image.yml
    Shared Image Creation Task:
    In this task, we will use the azure_rm_galleryimage module to create a shared image in your gallery. 
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
    Gallery Image Version Creation Task:
    In this task, we will use the azure_rm_galleryimageversion module to create a simple gallery image version.
    - name: Create or update a simple gallery Image Version
      azure_rm_galleryimageversion:
        resource_group: "{{ resource_group }}"
        gallery_name: "{{ shared_gallery_name }}"
        gallery_image_name: "{{ shared_image_name }}"
        name: 10.1.3
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
    After this playbook completes, you can visit the Azure Portal(https://portol.azure.com). Open your resource group, and you can find your shared image gallery. From the gallery you can see the shared image that you just created. There is the resource id of the shared image. Copy the resource id and add it to your vars.yml file as 'image_id'. 


Playbook 3 - Create Virtual Machine Using Shared Image
    ansible-playbook 03-create-vm-using-shared-image.yml
    Virtual Machine Creation Task:
    In this task, we will use the azure_rm_virtualmachine module to create a virtual machine using the shared image that we create in the pervious tasks.
    azure_rm_virtualmachine:
      resource_group: "{{ resource_group }}"
      name: "{{ vm_name }}"
      vm_size: Standard_DS1_v2
      admin_username: adminUser
      admin_password: PassWord01
      managed_disk_type: Standard_LRS
      image:
        id: "{{ image_id }}"
    After this playbook competes, you can visit the Azure Portal(https://portol.azure.com) and find the newly-created virtual machine in your resource group.
