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
module: azure_rm_recoveryservicesreplicationprotectioncontainer_info
version_added: '2.9'
short_description: Get ReplicationProtectionContainer info.
description:
  - Get info of ReplicationProtectionContainer.
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
      - Fabric name.
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
  fabric_friendly_name:
    description:
      - Fabric friendly name.
  friendly_name:
    description:
      - The name.
  fabric_type:
    description:
      - The fabric type.
  protected_item_count:
    description:
      - Number of protected PEs
  pairing_status:
    description:
      - The pairing status of this cloud.
  role:
    description:
      - The role of this cloud.
  fabric_specific_details:
    description:
      - Fabric specific details.
    suboptions:
      instance_type:
        description:
          - Gets the class type. Overridden in derived classes.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of all protection containers in a vault.
  azure_rm_recoveryservicesreplicationprotectioncontainer_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the list of protection container for a fabric.
  azure_rm_recoveryservicesreplicationprotectioncontainer_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
- name: Gets the protection container details.
  azure_rm_recoveryservicesreplicationprotectioncontainer_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationProtectionContainer

'''

RETURN = '''
replication_protection_containers:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationProtectionContainer and the values are the facts for that
    ReplicationProtectionContainer.
  returned: always
  type: complex
  contains:
    replicationprotectioncontainer_name:
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
            - The custom data.
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


class AzureRMReplicationProtectionContainersInfo(AzureRMModuleBase):
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
            name=dict(
                type='str'
            )
        )

        self.resource_name = None
        self.resource_group = None
        self.fabric_name = None
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
        super(AzureRMReplicationProtectionContainersInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.name is not None):
            self.results['replication_protection_containers'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None):
            self.results['replication_protection_containers'] = self.format_item(self.listbyreplicationfabrics())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_protection_containers'] = self.format_item(self.list())
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
                    '/replicationProtectionContainers' +
                    '/{{ replication_protection_container_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_protection_container_name }}', self.name)

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

    def listbyreplicationfabrics(self):
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
                    '/replicationProtectionContainers')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_protection_container_name }}', self.name)

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
                    '/replicationProtectionContainers')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_protection_container_name }}', self.name)

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
    AzureRMReplicationProtectionContainersInfo()


if __name__ == '__main__':
    main()
