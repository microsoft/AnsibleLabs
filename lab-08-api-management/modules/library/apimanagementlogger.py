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
module: apimanagementlogger
version_added: '2.9'
short_description: Manage Azure Logger instance.
description:
  - 'Create, update and delete instance of Azure Logger.'
options:
  resource_group:
    description:
      - The name of the resource group.
    required: true
    type: str
  service_name:
    description:
      - The name of the API Management service.
    required: true
    type: str
  logger_id:
    description:
      - >-
        Logger identifier. Must be unique in the API Management service
        instance.
    required: true
    type: str
  logger_type:
    description:
      - Logger type.
    required: true
    type: str
  description:
    description:
      - Logger description.
    type: str
  credentials:
    description:
      - >-
        The name and SendRule connection string of the event hub for
        azureEventHub logger.<br>Instrumentation key for applicationInsights
        logger.
    required: true
    type: str
  is_buffered:
    description:
      - >-
        Whether records are buffered in the logger before publishing. Default is
        assumed to be true.
    type: boolean
  resource_id:
    description:
      - >-
        Azure Resource Id of a log target (either Azure Event Hub resource or
        Azure Application Insights resource).
    type: str
  state:
    description:
      - Assert the state of the Logger.
      - Use C(present) to create or update an Logger and C(absent) to delete it.
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
- name: ApiManagementCreateEHLogger
  azure.rm.apimanagementlogger:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    logger_type: azureEventHub
    description: adding a new logger
    credentials:
      name: hydraeventhub
      connectionString: >-
        Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********=
- name: ApiManagementCreateAILogger
  azure.rm.apimanagementlogger:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    logger_type: applicationInsights
    description: adding a new logger
    credentials:
      instrumentationKey: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- name: ApiManagementUpdateLogger
  azure.rm.apimanagementlogger:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    credentials:
      name: hydraeventhub
      connectionString: >-
        Endpoint=sb://hydraeventhub-ns.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=********=
- name: ApiManagementDeleteLogger
  azure.rm.apimanagementlogger:
    resource_group: myResourceGroup
    service_name: myService
    logger_id: myLogger
    state: absent

'''

RETURN = '''
id:
  description:
    - Resource ID.
  returned: always
  type: str
  sample: null
name:
  description:
    - Resource name.
  returned: always
  type: str
  sample: null
type:
  description:
    - Resource type for API Management resource.
  returned: always
  type: str
  sample: null
properties:
  description:
    - Logger entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    logger_type:
      description:
        - Logger type.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Logger description.
      returned: always
      type: str
      sample: null
    credentials:
      description:
        - >-
          The name and SendRule connection string of the event hub for
          azureEventHub logger.<br>Instrumentation key for applicationInsights
          logger.
      returned: always
      type: str
      sample: null
    is_buffered:
      description:
        - >-
          Whether records are buffered in the logger before publishing. Default
          is assumed to be true.
      returned: always
      type: boolean
      sample: null
    resource_id:
      description:
        - >-
          Azure Resource Id of a log target (either Azure Event Hub resource or
          Azure Application Insights resource).
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
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMLogger(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                updatable=False,
                disposition='resourceGroupName',
                required=True
            ),
            service_name=dict(
                type='str',
                updatable=False,
                disposition='serviceName',
                required=True
            ),
            logger_id=dict(
                type='str',
                updatable=False,
                disposition='loggerId',
                required=True
            ),
            logger_type=dict(
                type='str',
                disposition='/properties/loggerType',
                choices=['azureEventHub',
                         'applicationInsights'],
                required=True
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            credentials=dict(
                type='dict',
                disposition='/properties/*',
                required=True
            ),
            is_buffered=dict(
                type='boolean',
                disposition='/properties/isBuffered'
            ),
            resource_id=dict(
                type='str',
                disposition='/properties/resourceId'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.logger_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMLogger, self).__init__(derived_arg_spec=self.module_arg_spec,
                                            supports_check_mode=True,
                                            supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            # if hasattr(self, key):
                # setattr(self, key, kwargs[key])
            # elif kwargs[key] is not None:
                # self.body[key] = kwargs[key]
            if kwargs[key] is not None and not hasattr(self, key):
                self.body[key] = kwargs[key]

        self.resource_group = kwargs['resource_group']
        self.service_name = kwargs['service_name']
        self.logger_id = kwargs['logger_id']
        self.body['credentials'] = kwargs['credentials']
        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        resource_group = self.get_resource_group(self.resource_group)

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/loggers' +
                    '/{{ logger_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ logger_name }}', self.logger_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("Logger instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Logger instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the Logger instance')

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
            self.log('Logger instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Logger instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Logger instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'PUT',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the Logger instance.')
            self.fail('Error creating the Logger instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Logger instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Logger instance.')
            self.fail('Error deleting the Logger instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Logger instance {0} is present'.format(self.))
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
            # self.log("Logger instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Logger instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMLogger()


if __name__ == '__main__':
    main()
