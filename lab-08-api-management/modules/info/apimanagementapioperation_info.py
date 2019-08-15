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
module: apimanagementapioperation_info
version_added: '2.9'
short_description: Get ApiOperation info.
description:
  - Get info of ApiOperation.
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
  api_id:
    description:
      - >-
        API revision identifier. Must be unique in the current API Management
        service instance. Non-current revision has ;rev=n as a suffix where n is
        the revision number.
    required: true
    type: str
  operation_id:
    description:
      - >-
        Operation identifier within an API. Must be unique in the current API
        Management service instance.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  name:
    description:
      - Resource name.
    type: str
  type:
    description:
      - Resource type for API Management resource.
    type: str
  template_parameters:
    description:
      - Collection of URL template parameters.
    type: list
    suboptions:
      name:
        description:
          - Parameter name.
        required: true
        type: str
      description:
        description:
          - Parameter description.
        type: str
      type:
        description:
          - Parameter type.
        required: true
        type: str
      default_value:
        description:
          - Default parameter value.
        type: str
      required:
        description:
          - Specifies whether parameter is required or not.
        type: boolean
      values:
        description:
          - Parameter values.
        type: list
  description:
    description:
      - Description of the operation. May include HTML formatting tags.
    type: str
  request:
    description:
      - An entity containing request details.
    type: dict
    suboptions:
      description:
        description:
          - Operation request description.
        type: str
      query_parameters:
        description:
          - Collection of operation request query parameters.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
            type: str
          description:
            description:
              - Parameter description.
            type: str
          type:
            description:
              - Parameter type.
            required: true
            type: str
          default_value:
            description:
              - Default parameter value.
            type: str
          required:
            description:
              - Specifies whether parameter is required or not.
            type: boolean
          values:
            description:
              - Parameter values.
            type: list
      headers:
        description:
          - Collection of operation request headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
            type: str
          description:
            description:
              - Parameter description.
            type: str
          type:
            description:
              - Parameter type.
            required: true
            type: str
          default_value:
            description:
              - Default parameter value.
            type: str
          required:
            description:
              - Specifies whether parameter is required or not.
            type: boolean
          values:
            description:
              - Parameter values.
            type: list
      representations:
        description:
          - Collection of operation request representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
            type: str
          sample:
            description:
              - An example of the representation.
            type: str
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
            type: str
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
            type: str
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
                type: str
              description:
                description:
                  - Parameter description.
                type: str
              type:
                description:
                  - Parameter type.
                required: true
                type: str
              default_value:
                description:
                  - Default parameter value.
                type: str
              required:
                description:
                  - Specifies whether parameter is required or not.
                type: boolean
              values:
                description:
                  - Parameter values.
                type: list
  responses:
    description:
      - Array of Operation responses.
    type: list
    suboptions:
      status_code:
        description:
          - Operation response HTTP status code.
        required: true
        type: number
      description:
        description:
          - Operation response description.
        type: str
      representations:
        description:
          - Collection of operation response representations.
        type: list
        suboptions:
          content_type:
            description:
              - >-
                Specifies a registered or custom content type for this
                representation, e.g. application/xml.
            required: true
            type: str
          sample:
            description:
              - An example of the representation.
            type: str
          schema_id:
            description:
              - >-
                Schema identifier. Applicable only if 'contentType' value is
                neither 'application/x-www-form-urlencoded' nor
                'multipart/form-data'.
            type: str
          type_name:
            description:
              - >-
                Type name defined by the schema. Applicable only if
                'contentType' value is neither
                'application/x-www-form-urlencoded' nor 'multipart/form-data'.
            type: str
          form_parameters:
            description:
              - >-
                Collection of form parameters. Required if 'contentType' value
                is either 'application/x-www-form-urlencoded' or
                'multipart/form-data'..
            type: list
            suboptions:
              name:
                description:
                  - Parameter name.
                required: true
                type: str
              description:
                description:
                  - Parameter description.
                type: str
              type:
                description:
                  - Parameter type.
                required: true
                type: str
              default_value:
                description:
                  - Default parameter value.
                type: str
              required:
                description:
                  - Specifies whether parameter is required or not.
                type: boolean
              values:
                description:
                  - Parameter values.
                type: list
      headers:
        description:
          - Collection of operation response headers.
        type: list
        suboptions:
          name:
            description:
              - Parameter name.
            required: true
            type: str
          description:
            description:
              - Parameter description.
            type: str
          type:
            description:
              - Parameter type.
            required: true
            type: str
          default_value:
            description:
              - Default parameter value.
            type: str
          required:
            description:
              - Specifies whether parameter is required or not.
            type: boolean
          values:
            description:
              - Parameter values.
            type: list
  policies:
    description:
      - Operation Policies
    type: str
  display_name:
    description:
      - Operation Name.
    required: true
    type: str
  method:
    description:
      - >-
        A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST
        but not limited by only them.
    required: true
    type: str
  url_template:
    description:
      - >-
        Relative URL template identifying the target resource for this
        operation. May include parameters. Example:
        /customers/{cid}/orders/{oid}/?date={date}
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiOperations
  azure.rm.apimanagementapioperation_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: 57d2ef278aa04f0ad01d6cdc
- name: ApiManagementGetApiOperation
  azure.rm.apimanagementapioperation_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation
- name: ApiManagementGetApiOperationPetStore
  azure.rm.apimanagementapioperation_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    operation_id: myOperation

'''

RETURN = '''
api_operation:
  description: >-
    A list of dict results where the key is the name of the ApiOperation and the
    values are the facts for that ApiOperation.
  returned: always
  type: complex
  contains:
    apioperation_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
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
            - Properties of the Operation Contract.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
  from msrestazure.azure_exceptions import CloudError
except ImportError:
  # This is handled in azure_rm_common
  pass


class AzureRMApiOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            service_name=dict(
                type='str',
                required=True
            ),
            api_id=dict(
                type='str',
                required=True
            ),
            operation_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.tags = None
        self.operation_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-01-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMApiOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.operation_id is not None):
            self.results['api_operation'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None):
            self.results['api_operation'] = self.listbyapi()
        return self.results

    def get(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/apis' +
                    '/{{ api_name }}' +
                    '/operations' +
                    '/{{ operation_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_id)
        self.url = self.url.replace('{{ operation_name }}', self.operation_id)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return self.format_item(results)

    def listbyapi(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service' +
                    '/{{ service_name }}' +
                    '/apis' +
                    '/{{ api_name }}' +
                    '/operations')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_id)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return [self.format_item(x) for x in results['value']] if results['value'] else []

    def format_item(self, item):
        d = {
            'id': item['id'],
            'name': item['name'],
            'type': item['type'],
            'properties': item['properties']
        }
        return d


def main():
    AzureRMApiOperationInfo()


if __name__ == '__main__':
    main()
