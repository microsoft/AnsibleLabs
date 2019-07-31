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
module: apimanagementdiagnostic
version_added: '2.9'
short_description: Manage Azure Diagnostic instance.
description:
  - 'Create, update and delete instance of Azure Diagnostic.'
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
  diagnostic_id:
    description:
      - >-
        Diagnostic identifier. Must be unique in the current API Management
        service instance.
    required: true
    type: str
  always_log:
    description:
      - Specifies for what type of messages sampling settings should not apply.
    type: str
  logger_id:
    description:
      - Resource Id of a target logger.
    required: true
    type: str
  sampling:
    description:
      - Sampling settings for Diagnostic.
    type: dict
    suboptions:
      sampling_type:
        description:
          - Sampling type.
        type: str
      percentage:
        description:
          - Rate of sampling for fixed-rate sampling.
        type: int
  frontend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
    type: dict
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: int
      response:
        description:
          - Diagnostic settings for response.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: int
  backend:
    description:
      - Diagnostic settings for incoming/outgoing HTTP messages to the Backend
    type: dict
    suboptions:
      request:
        description:
          - Diagnostic settings for request.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: int
      response:
        description:
          - Diagnostic settings for response.
        type: dict
        suboptions:
          headers:
            description:
              - Array of HTTP Headers to log.
            type: list
          body:
            description:
              - Body logging settings.
            type: dict
            suboptions:
              bytes:
                description:
                  - Number of request body bytes to log.
                type: int
  enable_http_correlation_headers:
    description:
      - >-
        Whether to process Correlation Headers coming to Api Management Service.
        Only applicable to Application Insights diagnostics. Default is true.
    type: boolean
  state:
    description:
      - Assert the state of the Diagnostic.
      - >-
        Use C(present) to create or update an Diagnostic and C(absent) to delete
        it.
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
- name: ApiManagementCreateDiagnostic
  azure.rm.apimanagementdiagnostic:
    resource_group: myResourceGroup
    service_name: myService
    diagnostic_id: applicationinsights
    always_log: allErrors
    logger_id: /loggers/azuremonitor
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
- name: ApiManagementUpdateDiagnostic
  azure.rm.apimanagementdiagnostic:
    resource_group: myResourceGroup
    service_name: myService
    diagnostic_id: myDiagnostic
    always_log: allErrors
    logger_id: /loggers/applicationinsights
    sampling:
      sampling_type: fixed
      percentage: '50'
    frontend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
    backend:
      request:
        headers:
          - Content-type
        body:
          bytes: '512'
      response:
        headers:
          - Content-type
        body:
          bytes: '512'
- name: ApiManagementDeleteDiagnostic
  azure.rm.apimanagementdiagnostic:
    resource_group: myResourceGroup
    service_name: myService
    diagnostic_id: myDiagnostic
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
    - Diagnostic entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    always_log:
      description:
        - >-
          Specifies for what type of messages sampling settings should not
          apply.
      returned: always
      type: str
      sample: null
    logger_id:
      description:
        - Resource Id of a target logger.
      returned: always
      type: str
      sample: null
    sampling:
      description:
        - Sampling settings for Diagnostic.
      returned: always
      type: dict
      sample: null
      contains:
        sampling_type:
          description:
            - Sampling type.
          returned: always
          type: str
          sample: null
        percentage:
          description:
            - Rate of sampling for fixed-rate sampling.
          returned: always
          type: int
          sample: null
    frontend:
      description:
        - >-
          Diagnostic settings for incoming/outgoing HTTP messages to the
          Gateway.
      returned: always
      type: dict
      sample: null
      contains:
        request:
          description:
            - Diagnostic settings for request.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: int
                  sample: null
        response:
          description:
            - Diagnostic settings for response.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: int
                  sample: null
    backend:
      description:
        - Diagnostic settings for incoming/outgoing HTTP messages to the Backend
      returned: always
      type: dict
      sample: null
      contains:
        request:
          description:
            - Diagnostic settings for request.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: int
                  sample: null
        response:
          description:
            - Diagnostic settings for response.
          returned: always
          type: dict
          sample: null
          contains:
            headers:
              description:
                - Array of HTTP Headers to log.
              returned: always
              type: str
              sample: null
            body:
              description:
                - Body logging settings.
              returned: always
              type: dict
              sample: null
              contains:
                bytes:
                  description:
                    - Number of request body bytes to log.
                  returned: always
                  type: int
                  sample: null
    enable_http_correlation_headers:
      description:
        - >-
          Whether to process Correlation Headers coming to Api Management
          Service. Only applicable to Application Insights diagnostics. Default
          is true.
      returned: always
      type: boolean
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


class AzureRMDiagnostic(AzureRMModuleBaseExt):
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
            diagnostic_id=dict(
                type='str',
                updatable=False,
                disposition='diagnosticId',
                required=True
            ),
            always_log=dict(
                type='str',
                disposition='/properties/alwaysLog',
                choices=['allErrors']
            ),
            logger_id=dict(
                type='str',
                disposition='/properties/loggerId',
                required=True
            ),
            sampling=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    sampling_type=dict(
                        type='str',
                        disposition='samplingType',
                        choices=['fixed']
                    ),
                    percentage=dict(
                        type='int'
                    )
                )
            ),
            frontend=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    request=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='int'
                                    )
                                )
                            )
                        )
                    ),
                    response=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='int'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            backend=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    request=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='int'
                                    )
                                )
                            )
                        )
                    ),
                    response=dict(
                        type='dict',
                        options=dict(
                            headers=dict(
                                type='list'
                            ),
                            body=dict(
                                type='dict',
                                options=dict(
                                    bytes=dict(
                                        type='int'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            enable_http_correlation_headers=dict(
                type='boolean',
                disposition='/properties/enableHttpCorrelationHeaders'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.diagnostic_id = None

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

        super(AzureRMDiagnostic, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/diagnostics' +
                    '/{{ diagnostic_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ diagnostic_name }}', self.diagnostic_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("Diagnostic instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Diagnostic instance already exists')

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
            self.log('Need to Create / Update the Diagnostic instance')

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
            self.log('Diagnostic instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Diagnostic instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Diagnostic instance {0}'.format(self.))

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
            self.log('Error attempting to create the Diagnostic instance.')
            self.fail('Error creating the Diagnostic instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Diagnostic instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Diagnostic instance.')
            self.fail('Error deleting the Diagnostic instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Diagnostic instance {0} is present'.format(self.))
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
            # self.log("Diagnostic instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Diagnostic instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMDiagnostic()


if __name__ == '__main__':
    main()
