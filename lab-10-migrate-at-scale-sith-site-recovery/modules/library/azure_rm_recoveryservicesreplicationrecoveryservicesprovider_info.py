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
module: azure_rm_recoveryservicesreplicationrecoveryservicesprovider_info
version_added: '2.9'
short_description: Get ReplicationRecoveryServicesProvider info.
description:
  - Get info of ReplicationRecoveryServicesProvider.
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
  fabric_type:
    description:
      - Type of the site.
  friendly_name:
    description:
      - Friendly name of the DRA.
  provider_version:
    description:
      - The provider version.
  server_version:
    description:
      - The fabric provider.
  provider_version_state:
    description:
      - DRA version status.
  provider_version_expiry_date:
    description:
      - Expiry date of the version.
  fabric_friendly_name:
    description:
      - The fabric friendly name.
  last_heart_beat:
    description:
      - Time when last heartbeat was sent by the DRA.
  connection_status:
    description:
      - A value indicating whether DRA is responsive.
  protected_item_count:
    description:
      - Number of protected VMs currently managed by the DRA.
  allowed_scenarios:
    description:
      - The scenarios allowed on this provider.
    type: list
  health_error_details:
    description:
      - The recovery services provider health error details.
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
  dra_identifier:
    description:
      - The DRA Id.
  authentication_identity_details:
    description:
      - The authentication identity details.
    suboptions:
      tenant_id:
        description:
          - >-
            The tenant Id for the service principal with which the on-premise
            management/data plane components would communicate with our Azure
            services.
      application_id:
        description:
          - >-
            The application/client Id for the service principal with which the
            on-premise management/data plane components would communicate with
            our Azure services.
      object_id:
        description:
          - >-
            The object Id of the service principal with which the on-premise
            management/data plane components would communicate with our Azure
            services.
      audience:
        description:
          - >-
            The intended Audience of the service principal with which the
            on-premise management/data plane components would communicate with
            our Azure services.
      aad_authority:
        description:
          - The base authority for Azure Active Directory authentication.
  resource_access_identity_details:
    description:
      - The resource access identity details.
    suboptions:
      tenant_id:
        description:
          - >-
            The tenant Id for the service principal with which the on-premise
            management/data plane components would communicate with our Azure
            services.
      application_id:
        description:
          - >-
            The application/client Id for the service principal with which the
            on-premise management/data plane components would communicate with
            our Azure services.
      object_id:
        description:
          - >-
            The object Id of the service principal with which the on-premise
            management/data plane components would communicate with our Azure
            services.
      audience:
        description:
          - >-
            The intended Audience of the service principal with which the
            on-premise management/data plane components would communicate with
            our Azure services.
      aad_authority:
        description:
          - The base authority for Azure Active Directory authentication.
  provider_version_details:
    description:
      - The provider version details.
    suboptions:
      version:
        description:
          - The agent version.
      expiry_date:
        description:
          - Version expiry date.
      status:
        description:
          - A value indicating whether security update required.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: >-
    Gets the list of registered recovery services providers in the vault. This
    is a view only api.
  azure_rm_recoveryservicesreplicationrecoveryservicesprovider_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the list of registered recovery services providers for the fabric.
  azure_rm_recoveryservicesreplicationrecoveryservicesprovider_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
- name: Gets the details of a recovery services provider.
  azure_rm_recoveryservicesreplicationrecoveryservicesprovider_info:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    name: myReplicationRecoveryServicesProvider

'''

RETURN = '''
replication_recovery_services_providers:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationRecoveryServicesProvider and the values are the facts for that
    ReplicationRecoveryServicesProvider.
  returned: always
  type: complex
  contains:
    replicationrecoveryservicesprovider_name:
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
            - Provider properties.
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


class AzureRMReplicationRecoveryServicesProvidersInfo(AzureRMModuleBase):
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
        super(AzureRMReplicationRecoveryServicesProvidersInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.fabric_name is not None and
            self.name is not None):
            self.results['replication_recovery_services_providers'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None and
              self.fabric_name is not None):
            self.results['replication_recovery_services_providers'] = self.format_item(self.listbyreplicationfabrics())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_recovery_services_providers'] = self.format_item(self.list())
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
                    '/replicationRecoveryServicesProviders' +
                    '/{{ replication_recovery_services_provider_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_recovery_services_provider_name }}', self.name)

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
                    '/replicationRecoveryServicesProviders')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_recovery_services_provider_name }}', self.name)

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
                    '/replicationRecoveryServicesProviders')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_recovery_services_provider_name }}', self.name)

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
    AzureRMReplicationRecoveryServicesProvidersInfo()


if __name__ == '__main__':
    main()
