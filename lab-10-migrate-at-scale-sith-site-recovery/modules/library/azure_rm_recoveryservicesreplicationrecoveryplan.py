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
module: azure_rm_recoveryservicesreplicationrecoveryplan
version_added: '2.9'
short_description: Manage Azure ReplicationRecoveryPlan instance.
description:
  - 'Create, update and delete instance of Azure ReplicationRecoveryPlan.'
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
  primary_fabric_id:
    description:
      - The primary fabric Id.
    required: true
  recovery_fabric_id:
    description:
      - The recovery fabric Id.
    required: true
  failover_deployment_model:
    description:
      - The failover deployment model.
  groups:
    description:
      - The recovery plan groups.
    required: true
    type: list
    suboptions:
      group_type:
        description:
          - The group type.
        required: true
      replication_protected_items:
        description:
          - The list of protected items.
        type: list
        suboptions:
          id:
            description:
              - The ARM Id of the recovery plan protected item.
          virtual_machine_id:
            description:
              - The virtual machine Id.
      start_group_actions:
        description:
          - The start group actions.
        type: list
        suboptions:
          action_name:
            description:
              - The action name.
            required: true
          failover_types:
            description:
              - The list of failover types.
            required: true
            type: list
          failover_directions:
            description:
              - The list of failover directions.
            required: true
            type: list
          custom_details:
            description:
              - The custom details.
            required: true
      end_group_actions:
        description:
          - The end group actions.
        type: list
        suboptions:
          action_name:
            description:
              - The action name.
            required: true
          failover_types:
            description:
              - The list of failover types.
            required: true
            type: list
          failover_directions:
            description:
              - The list of failover directions.
            required: true
            type: list
          custom_details:
            description:
              - The custom details.
            required: true
  friendly_name:
    description:
      - The friendly name.
  primary_fabric_friendly_name:
    description:
      - The primary fabric friendly name.
  recovery_fabric_friendly_name:
    description:
      - The recovery fabric friendly name.
  replication_providers:
    description:
      - The list of replication providers.
    type: list
  allowed_operations:
    description:
      - The list of allowed operations.
    type: list
  last_planned_failover_time:
    description:
      - The start time of the last planned failover.
  last_unplanned_failover_time:
    description:
      - The start time of the last unplanned failover.
  last_test_failover_time:
    description:
      - The start time of the last test failover.
  current_scenario:
    description:
      - The current scenario details.
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
  current_scenario_status:
    description:
      - The recovery plan status.
  current_scenario_status_description:
    description:
      - The recovery plan status description.
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
      - Assert the state of the ReplicationRecoveryPlan.
      - >-
        Use C(present) to create or update an ReplicationRecoveryPlan and
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
- name: Creates a recovery plan with the given details.
  azure_rm_recoveryservicesreplicationrecoveryplan:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationRecoveryPlan
    input:
      properties:
        primaryFabricId: >-
          /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1
        recoveryFabricId: Microsoft Azure
        failoverDeploymentModel: ResourceManager
        groups:
          - groupType: Boot
            replicationProtectedItems:
              - id: >-
                  /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1/replicationProtectionContainers/cloud_6d224fc6-f326-5d35-96de-fbf51efb3179/replicationProtectedItems/f8491e4f-817a-40dd-a90c-af773978c75b
                virtualMachineId: f8491e4f-817a-40dd-a90c-af773978c75b
            startGroupActions: []
            endGroupActions: []
- name: Updates the given recovery plan.
  azure_rm_recoveryservicesreplicationrecoveryplan:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationRecoveryPlan
    input:
      properties:
        groups:
          - groupType: Shutdown
            replicationProtectedItems: []
            startGroupActions: []
            endGroupActions: []
          - groupType: Failover
            replicationProtectedItems: []
            startGroupActions: []
            endGroupActions: []
          - groupType: Boot
            replicationProtectedItems:
              - id: >-
                  /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1/replicationProtectionContainers/cloud_6d224fc6-f326-5d35-96de-fbf51efb3179/replicationProtectedItems/f8491e4f-817a-40dd-a90c-af773978c75b
                virtualMachineId: f8491e4f-817a-40dd-a90c-af773978c75b
            startGroupActions: []
            endGroupActions: []
          - groupType: Boot
            replicationProtectedItems:
              - id: >-
                  /Subscriptions/c183865e-6077-46f2-a3b1-deb0f4f4650a/resourceGroups/resourceGroupPS1/providers/Microsoft.RecoveryServices/vaults/vault1/replicationFabrics/cloud1/replicationProtectionContainers/cloud_6d224fc6-f326-5d35-96de-fbf51efb3179/replicationProtectedItems/c0c14913-3d7a-48ea-9531-cc99e0e686e6
                virtualMachineId: c0c14913-3d7a-48ea-9531-cc99e0e686e6
            startGroupActions: []
            endGroupActions: []
- name: Deletes the specified recovery plan.
  azure_rm_recoveryservicesreplicationrecoveryplan:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationRecoveryPlan
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
    - The custom details.
  returned: always
  type: dict
  sample: null
  contains:
    friendly_name:
      description:
        - The friendly name.
      returned: always
      type: str
      sample: null
    primary_fabric_id:
      description:
        - The primary fabric Id.
      returned: always
      type: str
      sample: null
    primary_fabric_friendly_name:
      description:
        - The primary fabric friendly name.
      returned: always
      type: str
      sample: null
    recovery_fabric_id:
      description:
        - The recovery fabric Id.
      returned: always
      type: str
      sample: null
    recovery_fabric_friendly_name:
      description:
        - The recovery fabric friendly name.
      returned: always
      type: str
      sample: null
    failover_deployment_model:
      description:
        - The failover deployment model.
      returned: always
      type: str
      sample: null
    replication_providers:
      description:
        - The list of replication providers.
      returned: always
      type: str
      sample: null
    allowed_operations:
      description:
        - The list of allowed operations.
      returned: always
      type: str
      sample: null
    last_planned_failover_time:
      description:
        - The start time of the last planned failover.
      returned: always
      type: datetime
      sample: null
    last_unplanned_failover_time:
      description:
        - The start time of the last unplanned failover.
      returned: always
      type: datetime
      sample: null
    last_test_failover_time:
      description:
        - The start time of the last test failover.
      returned: always
      type: datetime
      sample: null
    current_scenario:
      description:
        - The current scenario details.
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
    current_scenario_status:
      description:
        - The recovery plan status.
      returned: always
      type: str
      sample: null
    current_scenario_status_description:
      description:
        - The recovery plan status description.
      returned: always
      type: str
      sample: null
    groups:
      description:
        - The recovery plan groups.
      returned: always
      type: dict
      sample: null
      contains:
        group_type:
          description:
            - The group type.
          returned: always
          type: str
          sample: null
        replication_protected_items:
          description:
            - The list of protected items.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - The ARM Id of the recovery plan protected item.
              returned: always
              type: str
              sample: null
            virtual_machine_id:
              description:
                - The virtual machine Id.
              returned: always
              type: str
              sample: null
        start_group_actions:
          description:
            - The start group actions.
          returned: always
          type: dict
          sample: null
          contains:
            action_name:
              description:
                - The action name.
              returned: always
              type: str
              sample: null
            failover_types:
              description:
                - The list of failover types.
              returned: always
              type: str
              sample: null
            failover_directions:
              description:
                - The list of failover directions.
              returned: always
              type: str
              sample: null
            custom_details:
              description:
                - The custom details.
              returned: always
              type: dict
              sample: null
        end_group_actions:
          description:
            - The end group actions.
          returned: always
          type: dict
          sample: null
          contains:
            action_name:
              description:
                - The action name.
              returned: always
              type: str
              sample: null
            failover_types:
              description:
                - The list of failover types.
              returned: always
              type: str
              sample: null
            failover_directions:
              description:
                - The list of failover directions.
              returned: always
              type: str
              sample: null
            custom_details:
              description:
                - The custom details.
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


class AzureRMReplicationRecoveryPlans(AzureRMModuleBaseExt):
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
                disposition='recoveryPlanName',
                required=true
            ),
            primary_fabric_id=dict(
                type='str',
                disposition='/properties/primaryFabricId',
                required=true
            ),
            recovery_fabric_id=dict(
                type='str',
                disposition='/properties/recoveryFabricId',
                required=true
            ),
            failover_deployment_model=dict(
                type='str',
                disposition='/properties/failoverDeploymentModel',
                choices=['NotApplicable',
                         'Classic',
                         'ResourceManager']
            ),
            groups=dict(
                type='list',
                disposition='/properties/*',
                required=true,
                options=dict(
                    group_type=dict(
                        type='str',
                        disposition='groupType',
                        choices=['Shutdown',
                                 'Boot',
                                 'Failover'],
                        required=true
                    ),
                    replication_protected_items=dict(
                        type='list',
                        disposition='replicationProtectedItems',
                        options=dict(
                            id=dict(
                                type='str'
                            ),
                            virtual_machine_id=dict(
                                type='str',
                                disposition='virtualMachineId'
                            )
                        )
                    ),
                    start_group_actions=dict(
                        type='list',
                        disposition='startGroupActions',
                        options=dict(
                            action_name=dict(
                                type='str',
                                disposition='actionName',
                                required=true
                            ),
                            failover_types=dict(
                                type='list',
                                disposition='failoverTypes',
                                choices=['ReverseReplicate',
                                         'Commit',
                                         'PlannedFailover',
                                         'UnplannedFailover',
                                         'DisableProtection',
                                         'TestFailover',
                                         'TestFailoverCleanup',
                                         'Failback',
                                         'FinalizeFailback',
                                         'ChangePit',
                                         'RepairReplication',
                                         'SwitchProtection',
                                         'CompleteMigration'],
                                required=true
                            ),
                            failover_directions=dict(
                                type='list',
                                disposition='failoverDirections',
                                choices=['PrimaryToRecovery',
                                         'RecoveryToPrimary'],
                                required=true
                            ),
                            custom_details=dict(
                                type='dict',
                                disposition='customDetails',
                                required=true
                            )
                        )
                    ),
                    end_group_actions=dict(
                        type='list',
                        disposition='endGroupActions',
                        options=dict(
                            action_name=dict(
                                type='str',
                                disposition='actionName',
                                required=true
                            ),
                            failover_types=dict(
                                type='list',
                                disposition='failoverTypes',
                                choices=['ReverseReplicate',
                                         'Commit',
                                         'PlannedFailover',
                                         'UnplannedFailover',
                                         'DisableProtection',
                                         'TestFailover',
                                         'TestFailoverCleanup',
                                         'Failback',
                                         'FinalizeFailback',
                                         'ChangePit',
                                         'RepairReplication',
                                         'SwitchProtection',
                                         'CompleteMigration'],
                                required=true
                            ),
                            failover_directions=dict(
                                type='list',
                                disposition='failoverDirections',
                                choices=['PrimaryToRecovery',
                                         'RecoveryToPrimary'],
                                required=true
                            ),
                            custom_details=dict(
                                type='dict',
                                disposition='customDetails',
                                required=true
                            )
                        )
                    )
                )
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

        super(AzureRMReplicationRecoveryPlans, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/replicationRecoveryPlans' +
                    '/{{ replication_recovery_plan_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_recovery_plan_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ReplicationRecoveryPlan instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ReplicationRecoveryPlan instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ReplicationRecoveryPlan instance')

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
            self.log('ReplicationRecoveryPlan instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ReplicationRecoveryPlan instance unchanged')
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
        # self.log('Creating / Updating the ReplicationRecoveryPlan instance {0}'.format(self.))

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
            self.log('Error attempting to create the ReplicationRecoveryPlan instance.')
            self.fail('Error creating the ReplicationRecoveryPlan instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ReplicationRecoveryPlan instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ReplicationRecoveryPlan instance.')
            self.fail('Error deleting the ReplicationRecoveryPlan instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ReplicationRecoveryPlan instance {0} is present'.format(self.))
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
            # self.log("ReplicationRecoveryPlan instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ReplicationRecoveryPlan instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMReplicationRecoveryPlans()


if __name__ == '__main__':
    main()
