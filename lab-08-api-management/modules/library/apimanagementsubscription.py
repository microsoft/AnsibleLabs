#!/usr/bin/python
# -*- coding: utf-8 -*- 
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
module: apimanagementsubscription
version_added: '2.9'
short_description: Manage Azure Subscription instance.
description:
  - 'Create, update and delete instance of Azure Subscription.'
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
  sid:
    description:
      - >-
        Subscription entity Identifier. The entity represents the association
        between a user and a product in API Management.
    required: true
    type: str
  owner_id:
    description:
      - >-
        User (user id path) for whom subscription is being created in form
        /users/{userId}
    type: str
  scope:
    description:
      - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
    required: true
    type: str
  display_name:
    description:
      - Subscription name.
    required: true
    type: str
  primary_key:
    description:
      - >-
        Primary subscription key. If not specified during request key will be
        generated automatically.
    type: str
  secondary_key:
    description:
      - >-
        Secondary subscription key. If not specified during request key will be
        generated automatically.
    type: str
  state:
    description:
      - Assert the state of the Subscription.
      - >-
        Use C(present) to create or update an Subscription and C(absent) to
        delete it.
    default: present
    choices:
      - absent
      - present
  allow_tracing:
    description:
      - Determines whether tracing can be enabled
    type: boolean
  created_date:
    description:
      - >-
        Subscription creation date. The date conforms to the following format:
        `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
    type: datetime
  start_date:
    description:
      - >-
        Subscription activation date. The setting is for audit purposes only and
        the subscription is not automatically activated. The subscription
        lifecycle can be managed by using the `state` property. The date
        conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
        the ISO 8601 standard.<br>
    type: datetime
  expiration_date:
    description:
      - >-
        Subscription expiration date. The setting is for audit purposes only and
        the subscription is not automatically expired. The subscription
        lifecycle can be managed by using the `state` property. The date
        conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by
        the ISO 8601 standard.<br>
    type: datetime
  end_date:
    description:
      - >-
        Date when subscription was cancelled or expired. The setting is for
        audit purposes only and the subscription is not automatically cancelled.
        The subscription lifecycle can be managed by using the `state` property.
        The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as
        specified by the ISO 8601 standard.<br>
    type: datetime
  notification_date:
    description:
      - >-
        Upcoming subscription expiration notification date. The date conforms to
        the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
        8601 standard.<br>
    type: datetime
  state_comment:
    description:
      - Optional subscription comment added by an administrator.
    type: str
  notify:
    description:
      - >-
        Notify change in Subscription State. <br> - If false, do not send any
        email notification for change of state of subscription <br> - If true,
        send email notification of change of state of subscription 
    type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementCreateSubscription
  azure.rm.apimanagementsubscription:
    resource_group: myResourceGroup
    service_name: myService
    sid: testsub
    owner_id: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name }}/users/{{
      user_name }}
    scope: >-
      /subscriptions/{{ subscription_id }}/resourceGroups/{{ resource_group
      }}/providers/Microsoft.ApiManagement/service/{{ service_name
      }}/products/{{ product_name }}
    display_name: testsub
- name: ApiManagementUpdateSubscription
  azure.rm.apimanagementsubscription:
    resource_group: myResourceGroup
    service_name: myService
    sid: testsub
    display_name: testsub
- name: ApiManagementDeleteSubscription
  azure.rm.apimanagementsubscription:
    resource_group: myResourceGroup
    service_name: myService
    sid: testsub
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
    - Subscription contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    owner_id:
      description:
        - >-
          The user resource identifier of the subscription owner. The value is a
          valid relative URL in the format of /users/{userId} where {userId} is
          a user identifier.
      returned: always
      type: str
      sample: null
    scope:
      description:
        - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
      returned: always
      type: str
      sample: null
    display_name:
      description:
        - 'The name of the subscription, or null if the subscription has no name.'
      returned: always
      type: str
      sample: null
    state:
      description:
        - >-
          Subscription state. Possible states are * active – the subscription is
          active, * suspended – the subscription is blocked, and the subscriber
          cannot call any APIs of the product, * submitted – the subscription
          request has been made by the developer, but has not yet been approved
          or rejected, * rejected – the subscription request has been denied by
          an administrator, * cancelled – the subscription has been cancelled by
          the developer or administrator, * expired – the subscription reached
          its expiration date and was deactivated.
      returned: always
      type: str
      sample: null
    created_date:
      description:
        - >-
          Subscription creation date. The date conforms to the following format:
          `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    start_date:
      description:
        - >-
          Subscription activation date. The setting is for audit purposes only
          and the subscription is not automatically activated. The subscription
          lifecycle can be managed by using the `state` property. The date
          conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
          by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    expiration_date:
      description:
        - >-
          Subscription expiration date. The setting is for audit purposes only
          and the subscription is not automatically expired. The subscription
          lifecycle can be managed by using the `state` property. The date
          conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified
          by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    end_date:
      description:
        - >-
          Date when subscription was cancelled or expired. The setting is for
          audit purposes only and the subscription is not automatically
          cancelled. The subscription lifecycle can be managed by using the
          `state` property. The date conforms to the following format:
          `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    notification_date:
      description:
        - >-
          Upcoming subscription expiration notification date. The date conforms
          to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the
          ISO 8601 standard.<br>
      returned: always
      type: datetime
      sample: null
    primary_key:
      description:
        - Subscription primary key.
      returned: always
      type: str
      sample: null
    secondary_key:
      description:
        - Subscription secondary key.
      returned: always
      type: str
      sample: null
    state_comment:
      description:
        - Optional subscription comment added by an administrator.
      returned: always
      type: str
      sample: null
    allow_tracing:
      description:
        - Determines whether tracing is enabled
      returned: always
      type: boolean
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


class AzureRMSubscription(AzureRMModuleBaseExt):
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
            sid=dict(
                type='str',
                updatable=False,
                required=True
            ),
            owner_id=dict(
                type='str',
                disposition='/properties/ownerId'
            ),
            scope=dict(
                type='str',
                disposition='/properties/*'
            ),
            display_name=dict(
                type='str',
                disposition='/properties/displayName',
                required=True
            ),
            primary_key=dict(
                type='str',
                disposition='/properties/primaryKey'
            ),
            secondary_key=dict(
                type='str',
                disposition='/properties/secondaryKey'
            ),
            pstate=dict(
                type='str',
                disposition='/properties/*',
                choices=['suspended',
                         'active',
                         'expired',
                         'submitted',
                         'rejected',
                         'cancelled']
            ),
            allow_tracing=dict(
                type='boolean',
                disposition='/properties/allowTracing'
            ),
            notify=dict(
                type='boolean',
                updatable=False
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.sid = None

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

        super(AzureRMSubscription, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                  supports_check_mode=True,
                                                  supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.body['scope'] = kwargs['scope']
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
                    '/subscriptions' +
                    '/{{ subscription_id }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ subscription_id }}', self.sid)

        old_response = self.get_resource()

        if not old_response:
            self.log("Subscription instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Subscription instance already exists')

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
            self.log('Need to Create / Update the Subscription instance')

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
            self.log('Subscription instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Subscription instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Subscription instance {0}'.format(self.))

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
            self.log('Error attempting to create the Subscription instance.')
            self.fail('Error creating the Subscription instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Subscription instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Subscription instance.')
            self.fail('Error deleting the Subscription instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Subscription instance {0} is present'.format(self.))
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
            # self.log("Subscription instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Subscription instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMSubscription()


if __name__ == '__main__':
    main()
