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
module: apimanagementauthorizationserver_info
version_added: '2.9'
short_description: Get AuthorizationServer info.
description:
  - Get info of AuthorizationServer.
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
  authsid:
    description:
      - Identifier of the authorization server.
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
  description:
    description:
      - >-
        Description of the authorization server. Can contain HTML formatting
        tags.
    type: str
  authorization_methods:
    description:
      - >-
        HTTP verbs supported by the authorization endpoint. GET must be always
        present. POST is optional.
    type: list
  client_authentication_method:
    description:
      - >-
        Method of authentication supported by the token endpoint of this
        authorization server. Possible values are Basic and/or Body. When Body
        is specified, client credentials and other parameters are passed within
        the request body in the application/x-www-form-urlencoded format.
    type: list
  token_body_parameters:
    description:
      - >-
        Additional parameters required by the token endpoint of this
        authorization server represented as an array of JSON objects with name
        and value string properties, i.e. {"name" : "name value", "value": "a
        value"}.
    type: list
    suboptions:
      name:
        description:
          - body parameter name.
        required: true
        type: str
      value:
        description:
          - body parameter value.
        required: true
        type: str
  token_endpoint:
    description:
      - OAuth token endpoint. Contains absolute URI to entity being referenced.
    type: str
  support_state:
    description:
      - >-
        If true, authorization server will include state parameter from the
        authorization request to its response. Client may use state parameter to
        raise protocol security.
    type: boolean
  default_scope:
    description:
      - >-
        Access token scope that is going to be requested by default. Can be
        overridden at the API level. Should be provided in the form of a string
        containing space-delimited values.
    type: str
  bearer_token_sending_methods:
    description:
      - 'Specifies the mechanism by which access token is passed to the API. '
    type: list
  client_secret:
    description:
      - Client or app secret registered with this authorization server.
    type: str
  resource_owner_username:
    description:
      - >-
        Can be optionally specified when resource owner password grant type is
        supported by this authorization server. Default resource owner username.
    type: str
  resource_owner_password:
    description:
      - >-
        Can be optionally specified when resource owner password grant type is
        supported by this authorization server. Default resource owner password.
    type: str
  display_name:
    description:
      - User-friendly authorization server name.
    required: true
    type: str
  client_registration_endpoint:
    description:
      - >-
        Optional reference to a page where client or app registration for this
        authorization server is performed. Contains absolute URL to entity being
        referenced.
    required: true
    type: str
  authorization_endpoint:
    description:
      - >-
        OAuth authorization endpoint. See
        http://tools.ietf.org/html/rfc6749#section-3.2.
    required: true
    type: str
  grant_types:
    description:
      - >-
        Form of an authorization grant, which the client uses to request the
        access token.
    required: true
    type: list
  client_id:
    description:
      - Client or app id registered with this authorization server.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListAuthorizationServers
  azure.rm.apimanagementauthorizationserver_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetAuthorizationServer
  azure.rm.apimanagementauthorizationserver_info:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer

'''

RETURN = '''
authorization_server:
  description: >-
    A list of dict results where the key is the name of the AuthorizationServer
    and the values are the facts for that AuthorizationServer.
  returned: always
  type: complex
  contains:
    authorizationserver_name:
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
            - Properties of the External OAuth authorization server Contract.
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


class AzureRMAuthorizationServerInfo(AzureRMModuleBase):
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
            authsid=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.authsid = None

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
        super(AzureRMAuthorizationServerInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.authsid is not None):
            self.results['authorization_server'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['authorization_server'] = self.listbyservice()
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
                    '/authorizationServers' +
                    '/{{ authorization_server_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ authorization_server_name }}', self.authsid)

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
                    '/authorizationServers')
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
    AzureRMAuthorizationServerInfo()


if __name__ == '__main__':
    main()
