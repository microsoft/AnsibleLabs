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
module: apimanagementuser
version_added: '2.9'
short_description: Manage Azure User instance.
description:
  - 'Create, update and delete instance of Azure User.'
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
  user_id:
    description:
      - >-
        User identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  ustate:
    description:
      - Assert the state of the User.
      - Use C(present) to create or update an User and C(absent) to delete it.
    default: present
    choices:
      - absent
      - present
  note:
    description:
      - Optional note about a user set by the administrator.
    type: str
  identities:
    description:
      - Collection of user identities.
    type: list
    suboptions:
      provider:
        description:
          - Identity provider name.
        type: str
      id:
        description:
          - Identifier value within provider.
        type: str
  email:
    description:
      - >-
        Email address. Must not be empty and must be unique within the service
        instance.
    required: true
    type: str
  first_name:
    description:
      - First name.
    required: true
    type: str
  last_name:
    description:
      - Last name.
    required: true
    type: str
  password:
    description:
      - 'User Password. If no value is provided, a default password is generated.'
    type: str
  confirmation:
    description:
      - >-
        Determines the type of confirmation e-mail that will be sent to the
        newly created user.
    type: str
  registration_date:
    description:
      - >-
        Date of user registration. The date conforms to the following format:
        `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
    type: datetime
  groups:
    description:
      - Collection of groups user is part of.
    type: list
    suboptions:
      display_name:
        description:
          - Group name.
        required: true
        type: str
      description:
        description:
          - Group description. Can contain HTML formatting tags.
        type: str
      built_in:
        description:
          - >-
            true if the group is one of the three system groups (Administrators,
            Developers, or Guests); otherwise false.
        type: boolean
      type:
        description:
          - Group type.
        type: str
      external_id:
        description:
          - >-
            For external groups, this property contains the id of the group from
            the external identity provider, e.g. for Azure Active Directory
            `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise
            the value is null.
        type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateUser
  azure.rm.apimanagementuser:
    resource_group: myResourceGroup
    service_name: myService
    user_id: myUser
    email: foobar@outlook.com
    first_name: foo
    last_name: bar
    confirmation: signup
- name: ApiManagementUpdateUser
  azure.rm.apimanagementuser:
    resource_group: myResourceGroup
    service_name: myService
    user_id: myUser
    email: foobar@outlook.com
    first_name: foo
    last_name: bar
- name: ApiManagementDeleteUser
  azure.rm.apimanagementuser:
    resource_group: myResourceGroup
    service_name: myService
    user_id: myUser
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
    - User entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    state:
      description:
        - >-
          Account state. Specifies whether the user is active or not. Blocked
          users are unable to sign into the developer portal or call any APIs of
          subscribed products. Default state is Active.
      returned: always
      type: str
      sample: null
    note:
      description:
        - Optional note about a user set by the administrator.
      returned: always
      type: str
      sample: null
    identities:
      description:
        - Collection of user identities.
      returned: always
      type: dict
      sample: null
      contains:
        provider:
          description:
            - Identity provider name.
          returned: always
          type: str
          sample: null
        id:
          description:
            - Identifier value within provider.
          returned: always
          type: str
          sample: null
    first_name:
      description:
        - First name.
      returned: always
      type: str
      sample: null
    last_name:
      description:
        - Last name.
      returned: always
      type: str
      sample: null
    email:
      description:
        - Email address.
      returned: always
      type: str
      sample: null
    registration_date:
      description:
        - >-
          Date of user registration. The date conforms to the following format:
          `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    groups:
      description:
        - Collection of groups user is part of.
      returned: always
      type: dict
      sample: null
      contains:
        display_name:
          description:
            - Group name.
          returned: always
          type: str
          sample: null
        description:
          description:
            - Group description. Can contain HTML formatting tags.
          returned: always
          type: str
          sample: null
        built_in:
          description:
            - >-
              true if the group is one of the three system groups
              (Administrators, Developers, or Guests); otherwise false.
          returned: always
          type: boolean
          sample: null
        type:
          description:
            - Group type.
          returned: always
          type: str
          sample: null
        external_id:
          description:
            - >-
              For external groups, this property contains the id of the group
              from the external identity provider, e.g. for Azure Active
              Directory `aad://<tenant>.onmicrosoft.com/groups/<group object
              id>`; otherwise the value is null.
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


class AzureRMUser(AzureRMModuleBaseExt):
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
            user_id=dict(
                type='str',
                updatable=False,
                disposition='userId',
                required=True
            ),
            ustate=dict(
                type='str',
                disposition='/properties/state',
                choices=['active',
                         'blocked',
                         'pending',
                         'deleted']
            ),
            note=dict(
                type='str',
                disposition='/properties/*'
            ),
            identities=dict(
                type='list',
                disposition='/properties/*',
                options=dict(
                    provider=dict(
                        type='str'
                    ),
                    id=dict(
                        type='str'
                    )
                )
            ),
            email=dict(
                type='str',
                disposition='/properties/*',
                required=True
            ),
            first_name=dict(
                type='str',
                disposition='/properties/firstName',
                required=True
            ),
            last_name=dict(
                type='str',
                disposition='/properties/lastName',
                required=True
            ),
            password=dict(
                type='str',
                no_log=True,
                disposition='/properties/*'
            ),
            confirmation=dict(
                type='str',
                disposition='/properties/*',
                choices=['signup',
                         'invite']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.user_id = None

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

        super(AzureRMUser, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/users' +
                    '/{{ user_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ user_name }}', self.user_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("User instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('User instance already exists')

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
            self.log('Need to Create / Update the User instance')

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
            self.log('User instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('User instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the User instance {0}'.format(self.))

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
            self.log('Error attempting to create the User instance.')
            self.fail('Error creating the User instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the User instance {0}'.format(self.))
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
            self.log('Error attempting to delete the User instance.')
            self.fail('Error deleting the User instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the User instance {0} is present'.format(self.))
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
            # self.log("User instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the User instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMUser()


if __name__ == '__main__':
    main()
