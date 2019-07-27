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
module: managementgroup
version_added: '2.9'
short_description: Manage Azure ManagementGroup instance.
description:
  - 'Create, update and delete instance of Azure ManagementGroup.'
options:
  name:
    description:
      - >-
        The name of the management group. For example,
        00000000-0000-0000-0000-000000000000
  id:
    description:
      - >-
        The fully qualified ID for the management group.  For example,
        /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
  type:
    description:
      - >-
        The type of the resource.  For example,
        /providers/Microsoft.Management/managementGroups
  tenant_id:
    description:
      - >-
        The AAD Tenant ID associated with the management group. For example,
        00000000-0000-0000-0000-000000000000
    returned: always
    type: str
  display_name:
    description:
      - The friendly name of the management group.
    returned: always
    type: str
  details:
    description:
      - The details of the management group.
    returned: always
    type: dict
    contains:
      version:
        description:
          - The version number of the object.
        returned: always
        type: number
      updated_time:
        description:
          - The date and time when this object was last updated.
        returned: always
        type: datetime
      updated_by:
        description:
          - The identity of the principal or process that updated the object.
        returned: always
        type: str
      parent:
        description:
          - The parent of the management group.
        returned: always
        type: dict
        contains:
          id:
            description:
              - >-
                The fully qualified ID for the parent management group.  For example,
                /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
            returned: always
            type: str
          name:
            description:
               - The name of the parent management group
            returned: always
            type: str
          display_name:
            description:
              - The friendly name of the parent management group.
            returned: always
            type: str
  state:
    description:
      - Assert the state of the ManagementGroup.
      - >-
        Use C(present) to create or update an ManagementGroup and C(absent) to
        delete it.
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
- name: PutManagementGroup
  azure.rm.managementgroup:
    id: /providers/Microsoft.Management/managementGroups/ChildGroup
    type: /providers/Microsoft.Management/managementGroups/
    name: ChildGroup
    tenant_id: 20000000-0000-0000-0000-000000000000
    display_name: ChildGroup
    details:
      parent:
        id: /providers/Microsoft.Management/managementGroups/RootGroup
- name: PatchManagementGroup
  azure.rm.managementgroup:
    group_id: ChildGroup
- name: DeleteManagementGroup
  azure.rm.managementgroup:
    group_id: ChildGroup
    state: absent

'''

RETURN = '''
id:
  description:
    - >-
      The fully qualified ID for the management group.  For example,
      /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
  returned: always
  type: str

'''

import time
import json
import re
from ansible.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMManagementGroups(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
          name=dict(type='str',updatable=False),
          id=dict(type='str'),
          type=dict(type='str'),
          tenant_id=dict(type='str', disposition="/properties/tenantId"),
          display_name=dict(type='str', disposition="/properties/displayName"),
          details=dict(
            type='dict',
            disposition="/properties/details",
            options=dict(
              parent=dict(
                type='dict',
                options=dict(
                  id=dict(type='str',disposition="id")
                )
              )
            )
          ),
          state=dict(type='str', default='present', choices=['present', 'absent']),  
        )

        self.name = None
        self.state = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction
        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMManagementGroups, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                      supports_check_mode=True,
                                                      supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)
        self.body['name'] = self.name

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        self.url = ('/providers' +
                    '/Microsoft.Management' +
                    '/managementGroups' +
                    '/{{ management_group_name }}')
        self.url = self.url.replace('{{ management_group_name }}', self.name)

        old_response = self.get_resource()

        if not old_response:
            self.log("ManagementGroup instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ManagementGroup instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ManagementGroup instance')

            if self.check_mode:
                self.results['changed'] = True
                return self.results

            response = self.create_update_resource()

            self.results['body'] = self.body
            # if not old_response:
            self.results['changed'] = True
            # else:
            #     self.results['changed'] = old_response.__ne__(response)
            self.log('Creation / Update done')
        elif self.to_do == Actions.Delete:
            self.log('ManagementGroup instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ManagementGroup instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ManagementGroup instance {0}'.format(self.))

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
            self.log('Error attempting to create the ManagementGroup instance.')
            self.fail('Error creating the ManagementGroup instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ManagementGroup instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ManagementGroup instance.')
            self.fail('Error deleting the ManagementGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ManagementGroup instance {0} is present'.format(self.))
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
            # self.log("ManagementGroup instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ManagementGroup instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMManagementGroups()


if __name__ == '__main__':
    main()
