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
module: azure_rm_recoveryservicesreplicationfabric_info
version_added: '2.9'
short_description: Get ReplicationFabric info.
description:
  - Get info of ReplicationFabric.
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
  friendly_name:
    description:
      - Friendly name of the fabric.
  encryption_details:
    description:
      - Encryption details for the fabric.
    suboptions:
      kek_state:
        description:
          - The key encryption key state for the Vmm.
      kek_cert_thumbprint:
        description:
          - The key encryption key certificate thumbprint.
      kek_cert_expiry_date:
        description:
          - The key encryption key certificate expiry date.
  rollover_encryption_details:
    description:
      - Rollover encryption details for the fabric.
    suboptions:
      kek_state:
        description:
          - The key encryption key state for the Vmm.
      kek_cert_thumbprint:
        description:
          - The key encryption key certificate thumbprint.
      kek_cert_expiry_date:
        description:
          - The key encryption key certificate expiry date.
  internal_identifier:
    description:
      - Dra Registration Id.
  bcdr_state:
    description:
      - BCDR state of the fabric.
  custom_details:
    description:
      - Fabric specific settings.
  health_error_details:
    description:
      - Fabric health error details.
    type: list
    suboptions:
      inner_health_errors:
        description:
          - >-
            The inner health errors. HealthError having a list of HealthError as
            child errors is problematic. InnerHealthError is used because this
            will prevent an infinite loop of structures when Hydra tries to
            auto-generate the contract. We are exposing the related health
            errors as inner health errors and all API consumers can utilize this
            in the same fashion as Exception -&gt; InnerException.
        type: list
        suboptions:
          error_source:
            description:
              - Source of error.
          error_type:
            description:
              - Type of error.
          error_level:
            description:
              - Level of error.
          error_category:
            description:
              - Category of error.
          error_code:
            description:
              - Error code.
          summary_message:
            description:
              - Summary message of the entity.
          error_message:
            description:
              - Error message.
          possible_causes:
            description:
              - Possible causes of error.
          recommended_action:
            description:
              - Recommended action to resolve error.
          creation_time_utc:
            description:
              - Error creation time (UTC)
          recovery_provider_error_message:
            description:
              - DRA error message.
          entity_id:
            description:
              - ID of the entity.
      error_source:
        description:
          - Source of error.
      error_type:
        description:
          - Type of error.
      error_level:
        description:
          - Level of error.
      error_category:
        description:
          - Category of error.
      error_code:
        description:
          - Error code.
      summary_message:
        description:
          - Summary message of the entity.
      error_message:
        description:
          - Error message.
      possible_causes:
        description:
          - Possible causes of error.
      recommended_action:
        description:
          - Recommended action to resolve error.
      creation_time_utc:
        description:
          - Error creation time (UTC)
      recovery_provider_error_message:
        description:
          - DRA error message.
      entity_id:
        description:
          - ID of the entity.
      error_id:
        description:
          - The health error unique id.
      customer_resolvability:
        description:
          - Value indicating whether the health error is customer resolvable.
  health:
    description:
      - Health of fabric.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of ASR fabrics
  azure_rm_recoveryservicesreplicationfabric_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the details of an ASR fabric.
  azure_rm_recoveryservicesreplicationfabric_info:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationFabric

'''

RETURN = '''
replication_fabrics:
  description: >-
    A list of dict results where the key is the name of the ReplicationFabric
    and the values are the facts for that ReplicationFabric.
  returned: always
  type: complex
  contains:
    replicationfabric_name:
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
            - Fabric related data.
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


class AzureRMReplicationFabricsInfo(AzureRMModuleBase):
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
            name=dict(
                type='str'
            )
        )

        self.resource_name = None
        self.resource_group = None
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
        super(AzureRMReplicationFabricsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.name is not None):
            self.results['replication_fabrics'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_fabrics'] = self.format_item(self.list())
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
                    '/{{ replication_fabric_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.name)

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
                    '/replicationFabrics')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.name)

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
    AzureRMReplicationFabricsInfo()


if __name__ == '__main__':
    main()
