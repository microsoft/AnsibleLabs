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
module: azure_rm_recoveryservicesreplicationrecoveryplan_info
version_added: '2.9'
short_description: Get ReplicationRecoveryPlan info.
description:
  - Get info of ReplicationRecoveryPlan.
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
      - The friendly name.
  primary_fabric_id:
    description:
      - The primary fabric Id.
  primary_fabric_friendly_name:
    description:
      - The primary fabric friendly name.
  recovery_fabric_id:
    description:
      - The recovery fabric Id.
  recovery_fabric_friendly_name:
    description:
      - The recovery fabric friendly name.
  failover_deployment_model:
    description:
      - The failover deployment model.
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
  groups:
    description:
      - The recovery plan groups.
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
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of recovery plans.
  azure_rm_recoveryservicesreplicationrecoveryplan_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the requested recovery plan.
  azure_rm_recoveryservicesreplicationrecoveryplan_info:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationRecoveryPlan

'''

RETURN = '''
replication_recovery_plans:
  description: >-
    A list of dict results where the key is the name of the
    ReplicationRecoveryPlan and the values are the facts for that
    ReplicationRecoveryPlan.
  returned: always
  type: complex
  contains:
    replicationrecoveryplan_name:
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
            - The custom details.
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


class AzureRMReplicationRecoveryPlansInfo(AzureRMModuleBase):
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
        super(AzureRMReplicationRecoveryPlansInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.name is not None):
            self.results['replication_recovery_plans'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_recovery_plans'] = self.format_item(self.list())
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
                    '/replicationRecoveryPlans' +
                    '/{{ replication_recovery_plan_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_recovery_plan_name }}', self.name)

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
                    '/replicationRecoveryPlans')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_recovery_plan_name }}', self.name)

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
    AzureRMReplicationRecoveryPlansInfo()


if __name__ == '__main__':
    main()
