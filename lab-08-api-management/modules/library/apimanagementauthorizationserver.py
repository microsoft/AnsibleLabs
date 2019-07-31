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
module: apimanagementauthorizationserver
version_added: '2.9'
short_description: Manage Azure AuthorizationServer instance.
description:
  - 'Create, update and delete instance of Azure AuthorizationServer.'
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
    required: true
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
    type: bool
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
  state:
    description:
      - Assert the state of the AuthorizationServer.
      - >-
        Use C(present) to create or update an AuthorizationServer and C(absent)
        to delete it.
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
- name: ApiManagementCreateAuthorizationServer
  azure.rm.apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
    description: test server
    authorization_methods:
      - GET
    token_endpoint: 'https://www.contoso.com/oauth2/token'
    support_state: true
    default_scope: read write
    bearer_token_sending_methods:
      - authorizationHeader
    client_secret: '2'
    resource_owner_username: un
    resource_owner_password: pwd
    display_name: test2
    client_registration_endpoint: 'https://www.contoso.com/apps'
    authorization_endpoint: 'https://www.contoso.com/oauth2/auth'
    grant_types:
      - authorizationCode
      - implicit
    client_id: '1'
- name: ApiManagementUpdateAuthorizationServer
  azure.rm.apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
    client_secret: updated
    client_id: update
- name: ApiManagementDeleteAuthorizationServer
  azure.rm.apimanagementauthorizationserver:
    resource_group: myResourceGroup
    service_name: myService
    authsid: myAuthorizationServer
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
    - Properties of the External OAuth authorization server Contract.
  returned: always
  type: dict
  sample: null
  contains:
    description:
      description:
        - >-
          Description of the authorization server. Can contain HTML formatting
          tags.
      returned: always
      type: str
      sample: null
    authorization_methods:
      description:
        - >-
          HTTP verbs supported by the authorization endpoint. GET must be always
          present. POST is optional.
      returned: always
      type: str
      sample: null
    client_authentication_method:
      description:
        - >-
          Method of authentication supported by the token endpoint of this
          authorization server. Possible values are Basic and/or Body. When Body
          is specified, client credentials and other parameters are passed
          within the request body in the application/x-www-form-urlencoded
          format.
      returned: always
      type: str
      sample: null
    token_body_parameters:
      description:
        - >-
          Additional parameters required by the token endpoint of this
          authorization server represented as an array of JSON objects with name
          and value string properties, i.e. {"name" : "name value", "value": "a
          value"}.
      returned: always
      type: dict
      sample: null
      contains:
        name:
          description:
            - body parameter name.
          returned: always
          type: str
          sample: null
        value:
          description:
            - body parameter value.
          returned: always
          type: str
          sample: null
    token_endpoint:
      description:
        - >-
          OAuth token endpoint. Contains absolute URI to entity being
          referenced.
      returned: always
      type: str
      sample: null
    support_state:
      description:
        - >-
          If true, authorization server will include state parameter from the
          authorization request to its response. Client may use state parameter
          to raise protocol security.
      returned: always
      type: bool
      sample: null
    default_scope:
      description:
        - >-
          Access token scope that is going to be requested by default. Can be
          overridden at the API level. Should be provided in the form of a
          string containing space-delimited values.
      returned: always
      type: str
      sample: null
    bearer_token_sending_methods:
      description:
        - 'Specifies the mechanism by which access token is passed to the API. '
      returned: always
      type: str
      sample: null
    client_secret:
      description:
        - Client or app secret registered with this authorization server.
      returned: always
      type: str
      sample: null
    resource_owner_username:
      description:
        - >-
          Can be optionally specified when resource owner password grant type is
          supported by this authorization server. Default resource owner
          username.
      returned: always
      type: str
      sample: null
    resource_owner_password:
      description:
        - >-
          Can be optionally specified when resource owner password grant type is
          supported by this authorization server. Default resource owner
          password.
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - User-friendly authorization server name.
      returned: always
      type: str
      sample: null
    client_registration_endpoint:
      description:
        - >-
          Optional reference to a page where client or app registration for this
          authorization server is performed. Contains absolute URL to entity
          being referenced.
      returned: always
      type: str
      sample: null
    authorization_endpoint:
      description:
        - >-
          OAuth authorization endpoint. See
          http://tools.ietf.org/html/rfc6749#section-3.2.
      returned: always
      type: str
      sample: null
    grant_types:
      description:
        - >-
          Form of an authorization grant, which the client uses to request the
          access token.
      returned: always
      type: str
      sample: null
    client_id:
      description:
        - Client or app id registered with this authorization server.
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


class AzureRMAuthorizationServer(AzureRMModuleBaseExt):
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
            authsid=dict(
                type='str',
                updatable=False,
                required=True
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            authorization_methods=dict(
                type='list',
                disposition='/properties/authorizationMethods',
                choices=['HEAD',
                         'OPTIONS',
                         'TRACE',
                         'GET',
                         'POST',
                         'PUT',
                         'PATCH',
                         'DELETE']
            ),
            client_authentication_method=dict(
                type='list',
                disposition='/properties/clientAuthenticationMethod',
                choices=['Basic',
                         'Body']
            ),
            token_body_parameters=dict(
                type='list',
                disposition='/properties/tokenBodyParameters',
                options=dict(
                    name=dict(
                        type='str',
                        required=True
                    ),
                    value=dict(
                        type='str',
                        required=True
                    )
                )
            ),
            token_endpoint=dict(
                type='str',
                disposition='/properties/tokenEndpoint'
            ),
            support_state=dict(
                type='bool',
                disposition='/properties/supportState'
            ),
            default_scope=dict(
                type='str',
                disposition='/properties/defaultScope'
            ),
            bearer_token_sending_methods=dict(
                type='list',
                disposition='/properties/bearerTokenSendingMethods',
                choices=['authorizationHeader',
                         'query']
            ),
            client_secret=dict(
                type='str',
                disposition='/properties/clientSecret'
            ),
            resource_owner_username=dict(
                type='str',
                disposition='/properties/resourceOwnerUsername'
            ),
            resource_owner_password=dict(
                type='str',
                disposition='/properties/resourceOwnerPassword'
            ),
            display_name=dict(
                type='str',
                disposition='/properties/displayName',
                required=True
            ),
            client_registration_endpoint=dict(
                type='str',
                disposition='/properties/clientRegistrationEndpoint',
                required=True
            ),
            authorization_endpoint=dict(
                type='str',
                disposition='/properties/authorizationEndpoint',
                required=True
            ),
            grant_types=dict(
                type='list',
                disposition='/properties/grantTypes',
                choices=['authorizationCode',
                         'implicit',
                         'resourceOwnerPassword',
                         'clientCredentials'],
                required=True
            ),
            client_id=dict(
                type='str',
                disposition='/properties/clientId',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.authsid = None

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

        super(AzureRMAuthorizationServer, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/authorizationServers' +
                    '/{{ authorization_server_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ authorization_server_name }}', self.authsid)

        old_response = self.get_resource()

        if not old_response:
            self.log("AuthorizationServer instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('AuthorizationServer instance already exists')

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
            self.log('Need to Create / Update the AuthorizationServer instance')

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
            self.log('AuthorizationServer instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('AuthorizationServer instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the AuthorizationServer instance {0}'.format(self.))

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
            self.log('Error attempting to create the AuthorizationServer instance.')
            self.fail('Error creating the AuthorizationServer instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the AuthorizationServer instance {0}'.format(self.))
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
            self.log('Error attempting to delete the AuthorizationServer instance.')
            self.fail('Error deleting the AuthorizationServer instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the AuthorizationServer instance {0} is present'.format(self.))
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
            # self.log("AuthorizationServer instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the AuthorizationServer instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMAuthorizationServer()


if __name__ == '__main__':
    main()
