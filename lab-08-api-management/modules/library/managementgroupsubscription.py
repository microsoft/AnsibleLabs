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
module: managementgroupsubscription
version_added: '2.9'
short_description: Manage Azure ManagementGroupSubscription instance.
description:
  - 'Create, update and delete instance of Azure ManagementGroupSubscription.'
options:
  group_id:
    description:
      - Management Group ID.
    required: true
  state:
    description:
      - Assert the state of the ManagementGroupSubscription.
      - >-
        Use C(present) to create or update an ManagementGroupSubscription and
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
- name: AddSubscriptionToManagementGroup
  azure.rm.managementgroupsubscription:
    group_id: myManagementGroup
- name: DeleteSubscriptionFromManagementGroup
  azure.rm.managementgroupsubscription:
    group_id: myManagementGroup
    state: absent

'''

RETURN = '''
{}

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


class AzureRMManagementGroupSubscriptions(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            group_id=dict(
                type='str',
                updatable=False,
                disposition='groupId',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.group_id = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200, 201, 202]
        self.to_do = Actions.NoAction

        self.body = {}
        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-03-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        super(AzureRMManagementGroupSubscriptions, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.url = ('/providers' +
                    '/Microsoft.Management' +
                    '/managementGroups' +
                    '/{{ management_group_name }}' +
                    '/subscriptions' +
                    '/{{ subscription_id }}')
        self.url = self.url.replace('{{ management_group_name }}', self.group_id)
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("ManagementGroupSubscription instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('ManagementGroupSubscription instance already exists')

            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.log('Need to Create / Update the ManagementGroupSubscription instance')

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
            self.log('ManagementGroupSubscription instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('ManagementGroupSubscription instance unchanged')
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the ManagementGroupSubscription instance {0}'.format(self.))

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
            self.log('Error attempting to create the ManagementGroupSubscription instance.')
            self.fail('Error creating the ManagementGroupSubscription instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the ManagementGroupSubscription instance {0}'.format(self.))
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
            self.log('Error attempting to delete the ManagementGroupSubscription instance.')
            self.fail('Error deleting the ManagementGroupSubscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the ManagementGroupSubscription instance {0} is present'.format(self.))
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
            # self.log("ManagementGroupSubscription instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the ManagementGroupSubscription instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMManagementGroupSubscriptions()


if __name__ == '__main__':
    main()
