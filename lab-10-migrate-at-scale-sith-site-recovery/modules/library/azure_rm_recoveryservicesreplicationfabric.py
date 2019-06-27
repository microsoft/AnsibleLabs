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
module: azure_rm_recoveryservicesreplicationfabric
version_added: '2.9'
short_description: Manage Azure ReplicationFabric instance.
description:
  - 'Create, update and delete instance of Azure ReplicationFabric.'
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
  custom_details:
    description:
      - Fabric provider specific creation input.
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
      - Assert the state of the ReplicationFabric.
      - >-
        Use C(present) to create or update an ReplicationFabric and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Creates an Azure Site Recovery fabric.
  azure_rm_recoveryservicesreplicationfabric:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationFabric
    input:
      properties:
        customDetails:
          instanceType: FabricSpecificCreationInput
- name: Deletes the site.
  azure_rm_recoveryservicesreplicationfabric:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationFabric

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
    - Fabric related data.
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - Friendly name of the fabric.
      returned: always
      type: str
      sample: null
    encryption_details:
      description:
        - Encryption details for the fabric.
      returned: always
      type: dict
      sample: null
      contains:
        kek_state:
          description:
            - The key encryption key state for the Vmm.
          returned: always
          type: str
          sample: null
        kek_cert_thumbprint:
          description:
            - The key encryption key certificate thumbprint.
          returned: always
          type: str
          sample: null
        kek_cert_expiry_date:
          description:
            - The key encryption key certificate expiry date.
          returned: always
          type: datetime
          sample: null
    rollover_encryption_details:
      description:
        - Rollover encryption details for the fabric.
      returned: always
      type: dict
      sample: null
      contains:
        kek_state:
          description:
            - The key encryption key state for the Vmm.
          returned: always
          type: str
          sample: null
        kek_cert_thumbprint:
          description:
            - The key encryption key certificate thumbprint.
          returned: always
          type: str
          sample: null
        kek_cert_expiry_date:
          description:
            - The key encryption key certificate expiry date.
          returned: always
          type: datetime
          sample: null
    internal_identifier:
      description:
        - Dra Registration Id.
      returned: always
      type: str
      sample: null
    bcdr_state:
      description:
        - BCDR state of the fabric.
      returned: always
      type: str
      sample: null
    custom_details:
      description:
        - Fabric specific settings.
      returned: always
      type: dict
      sample: null
    health_error_details:
      description:
        - Fabric health error details.
      returned: always
      type: dict
      sample: null
      contains:
        inner_health_errors:
          description:
            - >-
              The inner health errors. HealthError having a list of HealthError
              as child errors is problematic. InnerHealthError is used because
              this will prevent an infinite loop of structures when Hydra tries
              to auto-generate the contract. We are exposing the related health
              errors as inner health errors and all API consumers can utilize
              this in the same fashion as Exception -&gt; InnerException.
          returned: always
          type: dict
          sample: null
          contains:
            error_source:
              description:
                - Source of error.
              returned: always
              type: str
              sample: null
            error_type:
              description:
                - Type of error.
              returned: always
              type: str
              sample: null
            error_level:
              description:
                - Level of error.
              returned: always
              type: str
              sample: null
            error_category:
              description:
                - Category of error.
              returned: always
              type: str
              sample: null
            error_code:
              description:
                - Error code.
              returned: always
              type: str
              sample: null
            summary_message:
              description:
                - Summary message of the entity.
              returned: always
              type: str
              sample: null
            error_message:
              description:
                - Error message.
              returned: always
              type: str
              sample: null
            possible_causes:
              description:
                - Possible causes of error.
              returned: always
              type: str
              sample: null
            recommended_action:
              description:
                - Recommended action to resolve error.
              returned: always
              type: str
              sample: null
            creation_time_utc:
              description:
                - Error creation time (UTC)
              returned: always
              type: datetime
              sample: null
            recovery_provider_error_message:
              description:
                - DRA error message.
              returned: always
              type: str
              sample: null
            entity_id:
              description:
                - ID of the entity.
              returned: always
              type: str
              sample: null
        error_source:
          description:
            - Source of error.
          returned: always
          type: str
          sample: null
        error_type:
          description:
            - Type of error.
          returned: always
          type: str
          sample: null
        error_level:
          description:
            - Level of error.
          returned: always
          type: str
          sample: null
        error_category:
          description:
            - Category of error.
          returned: always
          type: str
          sample: null
        error_code:
          description:
            - Error code.
          returned: always
          type: str
          sample: null
        summary_message:
          description:
            - Summary message of the entity.
          returned: always
          type: str
          sample: null
        error_message:
          description:
            - Error message.
          returned: always
          type: str
          sample: null
        possible_causes:
          description:
            - Possible causes of error.
          returned: always
          type: str
          sample: null
        recommended_action:
          description:
            - Recommended action to resolve error.
          returned: always
          type: str
          sample: null
        creation_time_utc:
          description:
            - Error creation time (UTC)
          returned: always
          type: datetime
          sample: null
        recovery_provider_error_message:
          description:
            - DRA error message.
          returned: always
          type: str
          sample: null
        entity_id:
          description:
            - ID of the entity.
          returned: always
          type: str
          sample: null
        error_id:
          description:
            - The health error unique id.
          returned: always
          type: str
          sample: null
        customer_resolvability:
          description:
            - Value indicating whether the health error is customer resolvable.
          returned: always
          type: str
          sample: null
    health:
      description:
        - Health of fabric.
      returned: always
      type: str
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


class AzureRMReplicationFabrics(AzureRMModuleBaseExt):
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
            name=dict(
                type='str',
                updatable=False,
                disposition='fabricName',
                required=true
            ),
            custom_details=dict(
                type='dict',
                disposition='/properties/customDetails'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_name = None
        self.resource_group = None
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

        super(AzureRMReplicationFabrics, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/{{ replication_fabric_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ReplicationFabric instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ReplicationFabric instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ReplicationFabric instance')

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
            self.log('ReplicationFabric instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ReplicationFabric instance unchanged')
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
        # self.log('Creating / Updating the ReplicationFabric instance {0}'.format(self.))

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
            self.log('Error attempting to create the ReplicationFabric instance.')
            self.fail('Error creating the ReplicationFabric instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ReplicationFabric instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ReplicationFabric instance.')
            self.fail('Error deleting the ReplicationFabric instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationFabric instance {0} is present'.format(self.))
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
            # self.log("ReplicationFabric instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ReplicationFabric instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMReplicationFabrics()


if __name__ == '__main__':
    main()
