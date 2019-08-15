# -*- coding: utf-8 -*- 
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
module: apimanagementsubscription_info
version_added: '2.9'
short_description: Get Subscription info.
description:
  - Get info of Subscription.
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
  owner_id:
    description:
      - >-
        The user resource identifier of the subscription owner. The value is a
        valid relative URL in the format of /users/{userId} where {userId} is a
        user identifier.
    type: str
  scope:
    description:
      - 'Scope like /products/{productId} or /apis or /apis/{apiId}.'
    required: true
    type: str
  display_name:
    description:
      - 'The name of the subscription, or null if the subscription has no name.'
    type: str
  state:
    description:
      - >-
        Subscription state. Possible states are * active – the subscription is
        active, * suspended – the subscription is blocked, and the subscriber
        cannot call any APIs of the product, * submitted – the subscription
        request has been made by the developer, but has not yet been approved or
        rejected, * rejected – the subscription request has been denied by an
        administrator, * cancelled – the subscription has been cancelled by the
        developer or administrator, * expired – the subscription reached its
        expiration date and was deactivated.
    required: true
    type: str
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
  primary_key:
    description:
      - Subscription primary key.
    required: true
    type: str
  secondary_key:
    description:
      - Subscription secondary key.
    required: true
    type: str
  state_comment:
    description:
      - Optional subscription comment added by an administrator.
    type: str
  allow_tracing:
    description:
      - Determines whether tracing is enabled
    type: boolean
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListSubscriptions
  azure.rm.apimanagementsubscription_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetSubscription
  azure.rm.apimanagementsubscription_info:
    resource_group: myResourceGroup
    service_name: myService
    sid: 5931a769d8d14f0ad8ce13b8

'''

RETURN = '''
subscription:
  description: >-
    A list of dict results where the key is the name of the Subscription and the
    values are the facts for that Subscription.
  returned: always
  type: complex
  contains:
    subscription_name:
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
            - Subscription contract properties.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMSubscriptionInfo(AzureRMModuleBase):
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
            sid=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.sid = None

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
        super(AzureRMSubscriptionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.sid is not None):
            self.results['subscription'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['subscription'] = self.list()
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
                    '/subscriptions' +
                    '/{{ s_id }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ s_id }}', self.sid)

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

        return results

    def list(self):
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
                    '/{{ service_name }}'+
                    '/subscriptions')
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
    AzureRMSubscriptionInfo()


if __name__ == '__main__':
    main()
