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
module: apimanagementbackend_info
version_added: '2.9'
short_description: Get Backend info.
description:
  - Get info of Backend.
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
  backend_id:
    description:
      - >-
        Identifier of the Backend entity. Must be unique in the current API
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
  title:
    description:
      - Backend Title.
    type: str
  description:
    description:
      - Backend Description.
    type: str
  resource_id:
    description:
      - >-
        Management Uri of the Resource in External System. This url can be the
        Arm Resource Id of Logic Apps, Function Apps or Api Apps.
    type: str
  service_fabric_cluster:
    description:
      - Backend Service Fabric Cluster Properties
    type: dict
    suboptions:
      client_certificatethumbprint:
        description:
          - The client certificate thumbprint for the management endpoint.
        required: true
        type: str
      max_partition_resolution_retries:
        description:
          - Maximum number of retries while attempting resolve the partition.
        type: number
      management_endpoints:
        description:
          - The cluster management endpoint.
        required: true
        type: list
      server_certificate_thumbprints:
        description:
          - >-
            Thumbprints of certificates cluster management service uses for tls
            communication
        type: list
      server_x509names:
        description:
          - Server X509 Certificate Names Collection
        type: list
        suboptions:
          name:
            description:
              - Common Name of the Certificate.
            type: str
          issuer_certificate_thumbprint:
            description:
              - Thumbprint for the Issuer of the Certificate.
            type: str
  credentials:
    description:
      - Backend Credentials Contract Properties
    type: dict
    suboptions:
      certificate:
        description:
          - List of Client Certificate Thumbprint.
        type: list
      query:
        description:
          - Query Parameter description.
        type: str
      header:
        description:
          - Header Parameter description.
        type: str
      authorization:
        description:
          - Authorization header authentication
        type: dict
        suboptions:
          scheme:
            description:
              - Authentication Scheme name.
            required: true
            type: str
          parameter:
            description:
              - Authentication Parameter value.
            required: true
            type: str
  proxy:
    description:
      - Backend Proxy Contract Properties
    type: dict
    suboptions:
      url:
        description:
          - >-
            WebProxy Server AbsoluteUri property which includes the entire URI
            stored in the Uri instance, including all fragments and query
            strings.
        required: true
        type: str
      username:
        description:
          - Username to connect to the WebProxy server
        type: str
      password:
        description:
          - Password to connect to the WebProxy Server
        type: str
  tls:
    description:
      - Backend TLS Properties
    type: dict
    suboptions:
      validate_certificate_chain:
        description:
          - >-
            Flag indicating whether SSL certificate chain validation should be
            done when using self-signed certificates for this backend host.
        type: boolean
      validate_certificate_name:
        description:
          - >-
            Flag indicating whether SSL certificate name validation should be
            done when using self-signed certificates for this backend host.
        type: boolean
  url:
    description:
      - Runtime Url of the Backend.
    required: true
    type: str
  protocol:
    description:
      - Backend communication protocol.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListBackends
  azure.rm.apimanagementbackend_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetBackend
  azure.rm.apimanagementbackend_info:
    resource_group: myResourceGroup
    service_name: myService
    backend_id: myBackend

'''

RETURN = '''
backend:
  description: >-
    A list of dict results where the key is the name of the Backend and the
    values are the facts for that Backend.
  returned: always
  type: complex
  contains:
    backend_name:
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
            - Backend entity contract properties.
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


class AzureRMBackendInfo(AzureRMModuleBase):
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
            backend_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.backend_id = None

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
        super(AzureRMBackendInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.backend_id is not None):
            self.results['backend'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['backend'] = self.listbyservice()
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
                    '/backends' +
                    '/{{ backend_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ backend_name }}', self.backend_id)

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

    def listbyservice(self):
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
                    '/backends')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)

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
    AzureRMBackendInfo()


if __name__ == '__main__':
    main()
