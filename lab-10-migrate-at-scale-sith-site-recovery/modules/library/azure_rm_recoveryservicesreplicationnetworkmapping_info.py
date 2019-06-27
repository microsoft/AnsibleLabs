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
module: azure_rm_recoveryservicesreplicationnetworkmapping_info
version_added: '2.9'
short_description: Get ReplicationNetworkMapping info.
description:
  - Get info of ReplicationNetworkMapping.
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
  network_name:
    description:
      - Primary network name.
  name:
    description:
      - Resource Name
  id:
    description:
      - Resource Id
  type:
    description:
      - Resource Type
  location:
    description:
      - Resource Location
  state:
    description:
      - The pairing state for network mapping.
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
  recovery_network_id:
    description:
      - The recovery network id for network mapping.
  recovery_fabric_arm_id:
    description:
      - The recovery fabric ARM id.
  recovery_fabric_friendly_name:
    description:
      - The recovery fabric friendly name.
  fabric_specific_settings:
    description:
      - The fabric specific settings.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets all the network mappings under a vault.
  azure_rm_recoveryservicesreplicationnetworkmapping_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets all the network mappings under a network.
  azure_rm_recoveryservicesreplicationnetworkmapping_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    network_name: myReplicationNetwork
- name: Gets network mapping by name.
  azure_rm_recoveryservicesreplicationnetworkmapping_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    network_name: myReplicationNetwork
    name: myReplicationNetworkMapping

'''

RETURN = '''
replication_network_mappings:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationNetworkMapping and the values are the facts for that
    ReplicationNetworkMapping.
  returned: always
  type: complex
  contains:
    replicationnetworkmapping_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMReplicationNetworkMappingsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_name=dict(
                type='str',
                required=true
            ),
            resource_group=dict(
                type='str',
                required=true
            ),
            fabric_name=dict(
                type='str'
            ),
            network_name=dict(
                type='str'
            ),
            name=dict(
                type='str'
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
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMReplicationNetworkMappingsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.network_name is not None and
            self.name is not None):
            self.results['replication_network_mappings'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None and
              self.network_name is not None):
            self.results['replication_network_mappings'] = self.format_item(self.listbyreplicationnetworks())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_network_mappings'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
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

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def listbyreplicationnetworks(self):
        response = None
        results = {}
        # prepare url
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
                    '/replicationNetworkMappings')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_network_name }}', self.replication_network_name)
        self.url = self.url.replace('{{ replication_network_mapping_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/Subscriptions' +
                    '/{{ subscription_name }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.RecoveryServices' +
                    '/vaults' +
                    '/{{ vault_name }}' +
                    '/replicationNetworkMappings')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_network_name }}', self.replication_network_name)
        self.url = self.url.replace('{{ replication_network_mapping_name }}', self.name)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMReplicationNetworkMappingsInfo()


if __name__ == '__main__':
    main()
