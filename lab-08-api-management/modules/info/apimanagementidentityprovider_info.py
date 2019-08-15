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
module: apimanagementidentityprovider_info
version_added: '2.9'
short_description: Get IdentityProvider info.
description:
  - Get info of IdentityProvider.
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
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - Identity Provider Type identifier.
    type: str
  allowed_tenants:
    description:
      - List of Allowed Tenants when configuring Azure Active Directory login.
    type: list
  authority:
    description:
      - OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
    type: str
  signup_policy_name:
    description:
      - Signup Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  signin_policy_name:
    description:
      - Signin Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  profile_editing_policy_name:
    description:
      - Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  password_reset_policy_name:
    description:
      - Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
    type: str
  client_id:
    description:
      - >-
        Client Id of the Application in the external Identity Provider. It is
        App ID for Facebook login, Client ID for Google login, App ID for
        Microsoft.
    required: true
    type: str
  client_secret:
    description:
      - >-
        Client secret of the Application in external Identity Provider, used to
        authenticate login request. For example, it is App Secret for Facebook
        login, API Key for Google login, Public Key for Microsoft.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListIdentityProviders
  azure.rm.apimanagementidentityprovider_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetIdentityProvider
  azure.rm.apimanagementidentityprovider_info:
    resource_group: myResourceGroup
    service_name: myService
    name: myIdentityProvider

'''

RETURN = '''
identity_provider:
  description: >-
    A list of dict results where the key is the name of the IdentityProvider and
    the values are the facts for that IdentityProvider.
  returned: always
  type: complex
  contains:
    identityprovider_name:
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
            - Identity Provider contract properties.
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


class AzureRMIdentityProviderInfo(AzureRMModuleBase):
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
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.name = None

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
        super(AzureRMIdentityProviderInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.name is not None):
            self.results['identity_provider'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['identity_provider'] = self.listbyservice()
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
                    '/identityProviders' +
                    '/{{ identity_provider_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ identity_provider_name }}', self.name)

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
                    '/identityProviders')
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
    AzureRMIdentityProviderInfo()


if __name__ == '__main__':
    main()
