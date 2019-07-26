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
module: apimanagementgroup
version_added: '2.9'
short_description: Manage Azure Group instance.
description:
  - 'Create, update and delete instance of Azure Group.'
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
  group_id:
    description:
      - >-
        Group identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  display_name:
    description:
      - Group name.
    required: true
    type: str
  description:
    description:
      - Group description.
    type: str
  external_id:
    description:
      - >-
        Identifier of the external groups, this property contains the id of the
        group from the external identity provider, e.g. for Azure Active
        Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`;
        otherwise the value is null.
    type: str
  built_in:
    description:
      - >-
        true if the group is one of the three system groups (Administrators,
        Developers, or Guests); otherwise false.
    type: boolean
  state:
    description:
      - Assert the state of the Group.
      - Use C(present) to create or update an Group and C(absent) to delete it.
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
- name: ApiManagementCreateGroup
  azure.rm.apimanagementgroup:
    resource_group: myResourceGroup
    service_name: myService
    group_id: myGroup
    display_name: temp group
- name: ApiManagementCreateGroupExternal
  azure.rm.apimanagementgroup:
    resource_group: myResourceGroup
    service_name: myService
    group_id: myGroup
    display_name: NewGroup (samiraad.onmicrosoft.com)
    description: new group to test
    type: external
    external_id: 'aad://samiraad.onmicrosoft.com/groups/83cf2753-5831-4675-bc0e-2f8dc067c58d'
- name: ApiManagementUpdateGroup
  azure.rm.apimanagementgroup:
    resource_group: myResourceGroup
    service_name: myService
    group_id: myGroup
    display_name: temp group
- name: ApiManagementDeleteGroup
  azure.rm.apimanagementgroup:
    resource_group: myResourceGroup
    service_name: myService
    group_id: myGroup
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
    - Group entity contract properties.
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
          true if the group is one of the three system groups (Administrators,
          Developers, or Guests); otherwise false.
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
          For external groups, this property contains the id of the group from
          the external identity provider, e.g. for Azure Active Directory
          `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise
          the value is null.
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


class AzureRMGroup(AzureRMModuleBaseExt):
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
            group_id=dict(
                type='str',
                updatable=False,
                disposition='groupId',
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
            type=dict(
                type='str',
                disposition='/properties/*',
                choices=['custom',
                         'system',
                         'external']
            ),
            external_id=dict(
                type='str',
                disposition='/properties/externalId'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.group_id = None

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

        super(AzureRMGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                    '/groups' +
                    '/{{ group_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ group_name }}', self.group_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("Group instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Group instance already exists')

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
            self.log('Need to Create / Update the Group instance')

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
            self.log('Group instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Group instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Group instance {0}'.format(self.))

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
            self.log('Error attempting to create the Group instance.')
            self.fail('Error creating the Group instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Group instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Group instance.')
            self.fail('Error deleting the Group instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Group instance {0} is present'.format(self.))
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
            # self.log("Group instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Group instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMGroup()


if __name__ == '__main__':
    main()
