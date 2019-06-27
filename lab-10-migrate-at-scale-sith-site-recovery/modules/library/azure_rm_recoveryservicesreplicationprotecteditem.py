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
module: azure_rm_recoveryservicesreplicationprotecteditem
version_added: '2.9'
short_description: Manage Azure ReplicationProtectedItem instance.
description:
  - 'Create, update and delete instance of Azure ReplicationProtectedItem.'
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
      - Name of the fabric.
    required: true
  protection_container_name:
    description:
      - Protection container name.
    required: true
  name:
    description:
      - Resource Name
  policy_id:
    description:
      - The Policy Id.
  protectable_item_id:
    description:
      - The protectable item Id.
  provider_specific_details:
    description:
      - >-
        The ReplicationProviderInput. For HyperVReplicaAzure provider, it will
        be AzureEnableProtectionInput object. For San provider, it will be
        SanEnableProtectionInput object. For HyperVReplicaAzure provider, it can
        be null.
  friendly_name:
    description:
      - The name.
  protected_item_type:
    description:
      - The type of protected item type.
  recovery_services_provider_id:
    description:
      - The recovery provider ARM Id.
  primary_fabric_friendly_name:
    description:
      - The friendly name of the primary fabric.
  primary_fabric_provider:
    description:
      - The fabric provider of the primary fabric.
  recovery_fabric_friendly_name:
    description:
      - The friendly name of recovery fabric.
  recovery_fabric_id:
    description:
      - The Arm Id of recovery fabric.
  primary_protection_container_friendly_name:
    description:
      - The name of primary protection container friendly name.
  recovery_protection_container_friendly_name:
    description:
      - The name of recovery container friendly name.
  protection_state:
    description:
      - The protection status.
  protection_state_description:
    description:
      - The protection state description.
  active_location:
    description:
      - The Current active location of the PE.
  test_failover_state:
    description:
      - The Test failover state.
  test_failover_state_description:
    description:
      - The Test failover state description.
  allowed_operations:
    description:
      - The allowed operations on the Replication protected item.
    type: list
  replication_health:
    description:
      - >-
        The consolidated protection health for the VM taking any issues with SRS
        as well as all the replication units associated with the VM's
        replication group into account. This is a string representation of the
        ProtectionHealth enumeration.
  failover_health:
    description:
      - The consolidated failover health for the VM.
  health_errors:
    description:
      - List of health errors.
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
  policy_friendly_name:
    description:
      - The name of Policy governing this PE.
  last_successful_failover_time:
    description:
      - The Last successful failover time.
  last_successful_test_failover_time:
    description:
      - The Last successful test failover time.
  current_scenario:
    description:
      - The current scenario.
    suboptions:
      scenario_name:
        description:
          - Scenario name.
      job_id:
        description:
          - ARM Id of the job being executed.
      start_time:
        description:
          - Start time of the workflow.
  failover_recovery_point_id:
    description:
      - The recovery point ARM Id to which the Vm was failed over.
  recovery_container_id:
    description:
      - The recovery container Id.
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
      - Assert the state of the ReplicationProtectedItem.
      - >-
        Use C(present) to create or update an ReplicationProtectedItem and
        C(absent) to delete it.
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
- name: Enables protection.
  azure_rm_recoveryservicesreplicationprotecteditem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationProtectedItem
    input:
      properties:
        policyId: >-
          /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationPolicies/protectionprofile1
        protectableItemId: >-
          /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1/replicationProtectionContainers/cloud_6d224fc6-f326-5d35-96de-fbf51efb3179/replicationProtectableItems/f8491e4f-817a-40dd-a90c-af773978c75b
        providerSpecificDetails:
          instanceType: HyperVReplicaAzure
- name: Updates protection.
  azure_rm_recoveryservicesreplicationprotecteditem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationProtectedItem
- name: Disables protection.
  azure_rm_recoveryservicesreplicationprotecteditem:
    resource_name: myVault
    resource_group: myResourceGroup
    fabric_name: myReplicationFabric
    protection_container_name: myReplicationProtectionContainer
    name: myReplicationProtectedItem

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
    - The custom data.
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - The name.
      returned: always
      type: str
      sample: null
    protected_item_type:
      description:
        - The type of protected item type.
      returned: always
      type: str
      sample: null
    protectable_item_id:
      description:
        - The protected item ARM Id.
      returned: always
      type: str
      sample: null
    recovery_services_provider_id:
      description:
        - The recovery provider ARM Id.
      returned: always
      type: str
      sample: null
    primary_fabric_friendly_name:
      description:
        - The friendly name of the primary fabric.
      returned: always
      type: str
      sample: null
    primary_fabric_provider:
      description:
        - The fabric provider of the primary fabric.
      returned: always
      type: str
      sample: null
    recovery_fabric_friendly_name:
      description:
        - The friendly name of recovery fabric.
      returned: always
      type: str
      sample: null
    recovery_fabric_id:
      description:
        - The Arm Id of recovery fabric.
      returned: always
      type: str
      sample: null
    primary_protection_container_friendly_name:
      description:
        - The name of primary protection container friendly name.
      returned: always
      type: str
      sample: null
    recovery_protection_container_friendly_name:
      description:
        - The name of recovery container friendly name.
      returned: always
      type: str
      sample: null
    protection_state:
      description:
        - The protection status.
      returned: always
      type: str
      sample: null
    protection_state_description:
      description:
        - The protection state description.
      returned: always
      type: str
      sample: null
    active_location:
      description:
        - The Current active location of the PE.
      returned: always
      type: str
      sample: null
    test_failover_state:
      description:
        - The Test failover state.
      returned: always
      type: str
      sample: null
    test_failover_state_description:
      description:
        - The Test failover state description.
      returned: always
      type: str
      sample: null
    allowed_operations:
      description:
        - The allowed operations on the Replication protected item.
      returned: always
      type: str
      sample: null
    replication_health:
      description:
        - >-
          The consolidated protection health for the VM taking any issues with
          SRS as well as all the replication units associated with the VM's
          replication group into account. This is a string representation of the
          ProtectionHealth enumeration.
      returned: always
      type: str
      sample: null
    failover_health:
      description:
        - The consolidated failover health for the VM.
      returned: always
      type: str
      sample: null
    health_errors:
      description:
        - List of health errors.
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
    policy_id:
      description:
        - The ID of Policy governing this PE.
      returned: always
      type: str
      sample: null
    policy_friendly_name:
      description:
        - The name of Policy governing this PE.
      returned: always
      type: str
      sample: null
    last_successful_failover_time:
      description:
        - The Last successful failover time.
      returned: always
      type: datetime
      sample: null
    last_successful_test_failover_time:
      description:
        - The Last successful test failover time.
      returned: always
      type: datetime
      sample: null
    current_scenario:
      description:
        - The current scenario.
      returned: always
      type: dict
      sample: null
      contains:
        scenario_name:
          description:
            - Scenario name.
          returned: always
          type: str
          sample: null
        job_id:
          description:
            - ARM Id of the job being executed.
          returned: always
          type: str
          sample: null
        start_time:
          description:
            - Start time of the workflow.
          returned: always
          type: datetime
          sample: null
    failover_recovery_point_id:
      description:
        - The recovery point ARM Id to which the Vm was failed over.
      returned: always
      type: str
      sample: null
    provider_specific_details:
      description:
        - The Replication provider custom settings.
      returned: always
      type: dict
      sample: null
    recovery_container_id:
      description:
        - The recovery container Id.
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


class AzureRMReplicationProtectedItems(AzureRMModuleBaseExt):
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
            protection_container_name=dict(
                type='str',
                updatable=False,
                disposition='protectionContainerName',
                required=true
            ),
            name=dict(
                type='str',
                updatable=False,
                disposition='replicatedProtectedItemName',
                required=true
            ),
            policy_id=dict(
                type='str',
                disposition='/properties/policyId'
            ),
            protectable_item_id=dict(
                type='str',
                disposition='/properties/protectableItemId'
            ),
            provider_specific_details=dict(
                type='dict',
                disposition='/properties/providerSpecificDetails'
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
        self.protection_container_name = None
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

        super(AzureRMReplicationProtectedItems, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/replicationProtectionContainers' +
                    '/{{ replication_protection_container_name }}' +
                    '/replicationProtectedItems' +
                    '/{{ replication_protected_item_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_fabric_name }}', self.replication_fabric_name)
        self.url = self.url.replace('{{ replication_protection_container_name }}', self.replication_protection_container_name)
        self.url = self.url.replace('{{ replication_protected_item_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ReplicationProtectedItem instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ReplicationProtectedItem instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ReplicationProtectedItem instance')

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
            self.log('ReplicationProtectedItem instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ReplicationProtectedItem instance unchanged')
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
        # self.log('Creating / Updating the ReplicationProtectedItem instance {0}'.format(self.))

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
            self.log('Error attempting to create the ReplicationProtectedItem instance.')
            self.fail('Error creating the ReplicationProtectedItem instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ReplicationProtectedItem instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ReplicationProtectedItem instance.')
            self.fail('Error deleting the ReplicationProtectedItem instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationProtectedItem instance {0} is present'.format(self.))
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
            # self.log("ReplicationProtectedItem instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ReplicationProtectedItem instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMReplicationProtectedItems()


if __name__ == '__main__':
    main()
