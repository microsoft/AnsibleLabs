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
module: azure_rm_recoveryservicesreplicationjob_info
version_added: '2.9'
short_description: Get ReplicationJob info.
description:
  - Get info of ReplicationJob.
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
  activity_id:
    description:
      - The activity id.
  scenario_name:
    description:
      - The ScenarioName.
  friendly_name:
    description:
      - The DisplayName.
  state:
    description:
      - >-
        The status of the Job. It is one of these values - NotStarted,
        InProgress, Succeeded, Failed, Cancelled, Suspended or Other.
  state_description:
    description:
      - >-
        The description of the state of the Job. For e.g. - For Succeeded state,
        description can be Completed, PartiallySucceeded,
        CompletedWithInformation or Skipped.
  tasks:
    description:
      - The tasks.
    type: list
    suboptions:
      task_id:
        description:
          - The Id.
      name:
        description:
          - The unique Task name.
      start_time:
        description:
          - The start time.
      end_time:
        description:
          - The end time.
      allowed_actions:
        description:
          - The state/actions applicable on this task.
        type: list
      friendly_name:
        description:
          - The name.
      state:
        description:
          - >-
            The State. It is one of these values - NotStarted, InProgress,
            Succeeded, Failed, Cancelled, Suspended or Other.
      state_description:
        description:
          - >-
            The description of the task state. For example - For Succeeded
            state, description can be Completed, PartiallySucceeded,
            CompletedWithInformation or Skipped.
      task_type:
        description:
          - >-
            The type of task. Details in CustomDetails property depend on this
            type.
      custom_details:
        description:
          - The custom task details based on the task type.
      group_task_custom_details:
        description:
          - >-
            The custom task details based on the task type, if the task type is
            GroupTaskDetails or one of the types derived from it.
        suboptions:
          child_tasks:
            description:
              - The child tasks.
            type: list
            suboptions:
              task_id:
                description:
                  - The Id.
              name:
                description:
                  - The unique Task name.
              start_time:
                description:
                  - The start time.
              end_time:
                description:
                  - The end time.
              allowed_actions:
                description:
                  - The state/actions applicable on this task.
                type: list
              friendly_name:
                description:
                  - The name.
              state:
                description:
                  - >-
                    The State. It is one of these values - NotStarted,
                    InProgress, Succeeded, Failed, Cancelled, Suspended or
                    Other.
              state_description:
                description:
                  - >-
                    The description of the task state. For example - For
                    Succeeded state, description can be Completed,
                    PartiallySucceeded, CompletedWithInformation or Skipped.
              task_type:
                description:
                  - >-
                    The type of task. Details in CustomDetails property depend
                    on this type.
              custom_details:
                description:
                  - The custom task details based on the task type.
              group_task_custom_details:
                description:
                  - >-
                    The custom task details based on the task type, if the task
                    type is GroupTaskDetails or one of the types derived from
                    it.
              errors:
                description:
                  - The task error details.
                type: list
      errors:
        description:
          - The task error details.
        type: list
        suboptions:
          service_error_details:
            description:
              - The Service error details.
            suboptions:
              code:
                description:
                  - Error code.
              message:
                description:
                  - Error message.
              possible_causes:
                description:
                  - Possible causes of error.
              recommended_action:
                description:
                  - Recommended action to resolve error.
              activity_id:
                description:
                  - Activity Id.
          provider_error_details:
            description:
              - The Provider error details.
            suboptions:
              error_code:
                description:
                  - The Error code.
              error_message:
                description:
                  - The Error message.
              error_id:
                description:
                  - The Provider error Id.
              possible_causes:
                description:
                  - The possible causes for the error.
              recommended_action:
                description:
                  - The recommended action to resolve the error.
          error_level:
            description:
              - Error level of error.
          creation_time:
            description:
              - The creation time of job error.
          task_id:
            description:
              - The Id of the task.
  errors:
    description:
      - The errors.
    type: list
    suboptions:
      service_error_details:
        description:
          - The Service error details.
        suboptions:
          code:
            description:
              - Error code.
          message:
            description:
              - Error message.
          possible_causes:
            description:
              - Possible causes of error.
          recommended_action:
            description:
              - Recommended action to resolve error.
          activity_id:
            description:
              - Activity Id.
      provider_error_details:
        description:
          - The Provider error details.
        suboptions:
          error_code:
            description:
              - The Error code.
          error_message:
            description:
              - The Error message.
          error_id:
            description:
              - The Provider error Id.
          possible_causes:
            description:
              - The possible causes for the error.
          recommended_action:
            description:
              - The recommended action to resolve the error.
      error_level:
        description:
          - Error level of error.
      creation_time:
        description:
          - The creation time of job error.
      task_id:
        description:
          - The Id of the task.
  start_time:
    description:
      - The start time.
  end_time:
    description:
      - The end time.
  allowed_actions:
    description:
      - The Allowed action the job.
    type: list
  target_object_id:
    description:
      - The affected Object Id.
  target_object_name:
    description:
      - The name of the affected object.
  target_instance_type:
    description:
      - >-
        The type of the affected object which is of
        {Microsoft.Azure.SiteRecovery.V2015_11_10.AffectedObjectType} class.
  custom_details:
    description:
      - The custom job details like test failover job details.
    suboptions:
      affected_object_details:
        description:
          - >-
            The affected object properties like source server, source cloud,
            target server, target cloud etc. based on the workflow object
            details.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Gets the list of jobs.
  azure_rm_recoveryservicesreplicationjob_info:
    resource_name: myVault
    resource_group: myResourceGroup
- name: Gets the job details.
  azure_rm_recoveryservicesreplicationjob_info:
    resource_name: myVault
    resource_group: myResourceGroup
    name: myReplicationJob

'''

RETURN = '''
replication_jobs:
  description: >-
    A list of dict results where the key is the name of the ReplicationJob and
    the values are the facts for that ReplicationJob.
  returned: always
  type: complex
  contains:
    replicationjob_name:
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


class AzureRMReplicationJobsInfo(AzureRMModuleBase):
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
        super(AzureRMReplicationJobsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_name is not None and
            self.resource_group is not None and
            self.name is not None):
            self.results['replication_jobs'] = self.format_item(self.get())
        elif (self.resource_name is not None and
              self.resource_group is not None):
            self.results['replication_jobs'] = self.format_item(self.list())
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
                    '/replicationJobs' +
                    '/{{ replication_job_name }}')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_job_name }}', self.name)

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
                    '/replicationJobs')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ vault_name }}', self.vault_name)
        self.url = self.url.replace('{{ replication_job_name }}', self.name)

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
    AzureRMReplicationJobsInfo()


if __name__ == '__main__':
    main()
