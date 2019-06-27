# Lab 10 - Scale migration of VMs using Azure Site Recovery

# [WIP] This lab is currently in preparation

## Summary of Lab

This lab is based on following PowerShell Example:

https://github.com/Azure/azure-docs-powershell-samples/tree/master/azure-migrate/migrate-at-scale-with-site-recovery

## Playbook 00 - Prerequisites

This playbook will install following prereqisites:

- Ensure that the Site Recovery vault is created in your Azure subscription
- Ensure that the Configuration Server and Process Server are installed in the source environment and the vault is able to discover the environment
- Ensure that a Replication Policy is created and associated with the Configuration Server
- Ensure that you have added the VM admin account to the config server (that will be used to replicate the on-prem VMs)
- Ensure that the target artefacts in Azure are created
    - Target Resource Group
    - Target Storage Account (and its Resource Group) - Create a premium storage account if you plan to migrate to premium disks
    - Target Cache Storage Account (and its Resource Group) - Create a standard storage account in the same region as the vault
    - Target Virtual Network for failover (and its Resource Group)
    - Target Subnet
    - Target Virtual Network for Test failover (and its Resource Group)
    - Availability Set (if needed)
    - Target Network Security Group and its Resource Group
- Ensure that you have decided on the properties of the target VM
    - Target VM name
    - Target VM size in Azure (can be decided using Azure Migrate assessment)
    - Private IP Address of the primary NIC in the VM

## Playbook 01 - Create Custom Image

01_start_migration.yml

Enable replication for all the VMs listed in the csv, the script creates a CSV output with the job details for each VM

## Playbook 02 - Check the status of replication

02_asr_replicationstatus.yml | Check the status of replication, the script creates a csv with the status for each VM

## Playbook 03 - Update Target Properties

03_asr_updateproperties.yml

Once the VMs are replicated/protected, use this script to update the target properties of the VM (Compute and Network properties)

## Playbook 04 - Verify if Properties Updated

04_asr_propertiescheck.yml | Verify if the properties are appropriately updated

## Playbook 05 - Start the test failover

05_asr_testmigration.yml |  Start the test failover of the VMs listed in the csv, the script creates a CSV output with the job details for each VM

## Playbook 06 - Clean Up Failed-over VMs

06_asr_cleanuptestmigration.yml | Once you manually validate the VMs that were test failed-over, you can use this script to clean up the test failover VMs

## Playbook 07 - Perform Unplanned Failover

07_asr_migration.yml | Perform an unplanned failover for the VMs listed in the csv, the script creates a CSV output with the job details for each VM. The script does not shutdown the on-prem VMs before triggering the failover, for application consistency, it is recommended that you manually shut down the VMs before executing the script.

## Playbook 08 - Complete Migration

08_asr_completemigration.yml

Perform the commit operation on the VMs and delete the ASR entities

## Playbook 09 - Post Migration

09_asr_postmigration.yml

If you plan to assign network security groups to the NICs post-failover, you can use this script to do that. It assigns a NSG to any one NIC in the target VM.

