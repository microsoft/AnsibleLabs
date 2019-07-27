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
module: apimanagementopenidconnectprovider
version_added: '2.9'
short_description: Manage Azure OpenIdConnectProvider instance.
description:
  - 'Create, update and delete instance of Azure OpenIdConnectProvider.'
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
  opid:
    description:
      - Identifier of the OpenID Connect Provider.
    required: true
    type: str
  display_name:
    description:
      - User-friendly OpenID Connect Provider name.
    required: true
    type: str
  description:
    description:
      - User-friendly description of OpenID Connect Provider.
    type: str
  metadata_endpoint:
    description:
      - Metadata endpoint URI.
    required: true
    type: str
  client_id:
    description:
      - Client ID of developer console which is the client application.
    required: true
    type: str
  client_secret:
    description:
      - Client Secret of developer console which is the client application.
    type: str
  state:
    description:
      - Assert the state of the OpenIdConnectProvider.
      - >-
        Use C(present) to create or update an OpenIdConnectProvider and
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
- name: ApiManagementCreateOpenIdConnectProvider
  azure.rm.apimanagementopenidconnectprovider:
    resource_group: myResourceGroup
    service_name: myService
    opid: myOpenidConnectProvider
    display_name: templateoidprovider3
    metadata_endpoint: 'https://oidprovider-template3.net'
    client_id: oidprovidertemplate3
- name: ApiManagementUpdateOpenIdConnectProvider
  azure.rm.apimanagementopenidconnectprovider:
    resource_group: myResourceGroup
    service_name: myService
    opid: myOpenidConnectProvider
    client_secret: updatedsecret
- name: ApiManagementDeleteOpenIdConnectProvider
  azure.rm.apimanagementopenidconnectprovider:
    resource_group: myResourceGroup
    service_name: myService
    opid: myOpenidConnectProvider
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
    - OpenId Connect Provider contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    display_name:
      description:
        - User-friendly OpenID Connect Provider name.
      returned: always
      type: str
      sample: null
    description:
      description:
        - User-friendly description of OpenID Connect Provider.
      returned: always
      type: str
      sample: null
    metadata_endpoint:
      description:
        - Metadata endpoint URI.
      returned: always
      type: str
      sample: null
    client_id:
      description:
        - Client ID of developer console which is the client application.
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - Client Secret of developer console which is the client application.
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


class AzureRMOpenIdConnectProvider(AzureRMModuleBaseExt):
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
            opid=dict(
                type='str',
                updatable=False,
                required=True
            ),
            display_name=dict(
                type='str',
                disposition='/properties/displayName',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            metadata_endpoint=dict(
                type='str',
                disposition='/properties/metadataEndpoint',
                required=True
            ),
            client_id=dict(
                type='str',
                disposition='/properties/clientId',
                required=True
            ),
            client_secret=dict(
                type='str',
                disposition='/properties/clientSecret'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.opid = None

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

        super(AzureRMOpenIdConnectProvider, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/openidConnectProviders' +
                    '/{{ openid_connect_provider_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ openid_connect_provider_name }}', self.opid)

        old_response = self.get_resource()

        if not old_response:
            self.log("OpenIdConnectProvider instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('OpenIdConnectProvider instance already exists')

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
            self.log('Need to Create / Update the OpenIdConnectProvider instance')

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
            self.log('OpenIdConnectProvider instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('OpenIdConnectProvider instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the OpenIdConnectProvider instance {0}'.format(self.))

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
            self.log('Error attempting to create the OpenIdConnectProvider instance.')
            self.fail('Error creating the OpenIdConnectProvider instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the OpenIdConnectProvider instance {0}'.format(self.))
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
            self.log('Error attempting to delete the OpenIdConnectProvider instance.')
            self.fail('Error deleting the OpenIdConnectProvider instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the OpenIdConnectProvider instance {0} is present'.format(self.))
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
            # self.log("OpenIdConnectProvider instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the OpenIdConnectProvider instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMOpenIdConnectProvider()


if __name__ == '__main__':
    main()
