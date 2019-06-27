#!/usr/bin/python
#
# Copyright (c) 2019 Zim Kalinowski, (@zikalino)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_recoveryservicesreplicationnetworkmapping
version_added: '2.9'
short_description: Manage Azure ReplicationNetworkMapping instance.
description:
  - 'Create, update and delete instance of Azure ReplicationNetworkMapping.'
options:
  resource_name:
    description:
      - The name of the recovery services vault.
    required: true
  resource_group:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
  fabric_name:
    description:
      - Primary fabric name.
    required: true
  network_name:
    description:
      - Primary network name.
    required: true
  name:
    description:
      - Resource Name
  recovery_fabric_name:
    description:
      - Recovery fabric Name.
  recovery_network_id:
    description:
      - Recovery network Id.
  fabric_specific_details:
    description:
      - Fabric specific input properties.
  state:
    description:
      - Assert the state of the ReplicationNetworkMapping.
      - >-
        Use C(present) to create or update an ReplicationNetworkMapping and
        C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
  primary_network_friendly_name:
    description:
      - The primary network friendly name.
  primary_network_id:
    description:
      - The primary network id for network mapping.
  primary_fabric_friendly_name:
    description:
      - The primary fabric friendly name.
  recovery_network_friendly_name:
    description:
      - The recovery network friendly name.
  recovery_fabric_arm_id:
    description:
      - The recovery fabric ARM id.
  recovery_fabric_friendly_name:
    description:
      - The recovery fabric friendly name.
  fabric_specific_settings:
    description:
      - The fabric specific settings.
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Creates network mapping.
  azure_rm_recoveryservicesreplicationnetworkmapping:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    network_name: myReplicationNetwork
    name: myReplicationNetworkMapping
    input:
      properties:
        recoveryFabricName: Microsoft Azure
        recoveryNetworkId: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Network/virtualNetworks/{{ virtual_network_name
          }}
        fabricSpecificDetails:
          instanceType: VmmToAzure
- name: Updates network mapping.
  azure_rm_recoveryservicesreplicationnetworkmapping:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    network_name: myReplicationNetwork
    name: myReplicationNetworkMapping
    input:
      properties:
        recoveryFabricName: Microsoft Azure
        recoveryNetworkId: >-
          /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
          }}/providers/Microsoft.Network/virtualNetworks/{{ virtual_network_name
          }}
        fabricSpecificDetails:
          instanceType: VmmToAzure
- name: Delete network mapping.
  azure_rm_recoveryservicesreplicationnetworkmapping:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    network_name: myReplicationNetwork
    name: myReplicationNetworkMapping
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource Id
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource Name
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource Type
  returned: always
  type: str
  sample: null
location:
  description:
    - Resource Location
  returned: always
  type: str
  sample: null
properties:
  description:
    - The Network Mapping Properties.
  returned: always
  type: dict
  sample: null
  contains:
    state:
      description:
        - The pairing state for network mapping.
      returned: always
      type: str
      sample: null
    primary_network_friendly_name:
      description:
        - The primary network friendly name.
      returned: always
      type: str
      sample: null
    primary_network_id:
      description:
        - The primary network id for network mapping.
      returned: always
      type: str
      sample: null
    primary_fabric_friendly_name:
      description:
        - The primary fabric friendly name.
      returned: always
      type: str
      sample: null
    recovery_network_friendly_name:
      description:
        - The recovery network friendly name.
      returned: always
      type: str
      sample: null
    recovery_network_id:
      description:
        - The recovery network id for network mapping.
      returned: always
      type: str
      sample: null
    recovery_fabric_arm_id:
      description:
        - The recovery fabric ARM id.
      returned: always
      type: str
      sample: null
    recovery_fabric_friendly_name:
      description:
        - The recovery fabric friendly name.
      returned: always
      type: str
      sample: null
    fabric_specific_settings:
      description:
        - The fabric specific settings.
      returned: always
      type: dict
      sample: null

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMReplicationNetworkMappings(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                updatable=False,
                disposition='resourceName',
                required=true
            ),
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=true
            ),
            fabric_name=dict(
                type='str',
                updatable=False,
                disposition='fabricName',
                required=true
            ),
            network_name=dict(
                type='str',
                updatable=False,
                disposition='networkName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='networkMappingName',
                required=true
            ),
            recovery_fabric_name=dict(
                type='str',
                disposition='/properties/recoveryFabricName'
            ),
            recovery_network_id=dict(
                type='str',
                disposition='/properties/recoveryNetworkId'
            ),
            fabric_specific_details=dict(
                type='dict',
                disposition='/properties/fabricSpecificDetails'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.fabric_name = None
        self.network_name = None
        self.name = None
        self.id = None
        self.name = None
        self.type = None
        self.location = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMReplicationNetworkMappings, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                supports_check_mode=True,
                                                                supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        if self.location is None:
            self.location = resource_group.location

        self.url = ('/Subscriptions' +
                    '/{{ subscription_name }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.RecoveryServices' +
                    '/vaults' +
                    '/{{ vault_name }}' +
                    '/replicationFabrics' +
                    '/{{ replication_fabric_name }}' +
                    '/replicationNetworks' +
                    '/{{ replication_network_name }}' +
                    '/replicationNetworkMappings' +
                    '/{{ replication_network_mapping_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_network_name }}', self.replication_network_name)
        self.url = self.url.replace('{{ replication_network_mapping_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ReplicationNetworkMapping instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ReplicationNetworkMapping instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ReplicationNetworkMapping instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('ReplicationNetworkMapping instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ReplicationNetworkMapping instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["location"] = response["location"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ReplicationNetworkMapping instance {0}'.format(self.))

        try:
            if self.to_do == Actions.Create:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
            else:
                response = self.mgmt_client.query(self.url,
                                                  'PUT',
                                                  self.query_parameters,
                                                  self.header_parameters,
                                                  self.body,
                                                  self.status_code,
                                                  600,
                                                  30)
        except CloudError as exc:
            self.log('Error attempting to create the ReplicationNetworkMapping instance.')
            self.fail('Error creating the ReplicationNetworkMapping instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ReplicationNetworkMapping instance {0}'.format(self.))
        try:
            response = self.mgmt_client.query(self.url,
                                              'DELETE',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as e:
            self.log('Error attempting to delete the ReplicationNetworkMapping instance.')
            self.fail('Error deleting the ReplicationNetworkMapping instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationNetworkMapping instance {0} is present'.format(self.))
        found = False
        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            found = True
            self.log("Response : {0}".format(response))
            # self.log("ReplicationNetworkMapping instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ReplicationNetworkMapping instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMReplicationNetworkMappings()


if __name__ == '__main__':
    main()
