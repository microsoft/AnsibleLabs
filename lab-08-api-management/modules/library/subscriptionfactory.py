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
module: subscriptionfactory
version_added: '2.9'
short_description: Manage Azure SubscriptionFactory instance.
description:
  - 'Create, update and delete instance of Azure SubscriptionFactory.'
options:
  enrollment_account_name:
    description:
      - >-
        The name of the enrollment account to which the subscription will be
        billed.
    required: true
  display_name:
    description:
      - The display name of the subscription.
  owners:
    description:
      - >-
        The list of principals that should be granted Owner access on the
        subscription. Principals should be of type User, Service Principal or
        Security Group.
    type: list
    suboptions:
      object_id:
        description:
          - Object id of the Principal
        required: true
  offer_type:
    description:
      - >-
        The offer type of the subscription. For example, MS-AZR-0017P
        (EnterpriseAgreement) and MS-AZR-0148P (EnterpriseAgreement devTest) are
        available. Only valid when creating a subscription in a enrollment
        account scope.
  additional_parameters:
    description:
      - >-
        Additional, untyped parameters to support custom subscription creation
        scenarios.
  subscription_link:
    description:
      - The link to the new subscription.
  state:
    description:
      - Assert the state of the SubscriptionFactory.
      - >-
        Use C(present) to create or update an SubscriptionFactory and C(absent)
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
- name: Create Subscription
  azure.rm.subscriptionfactory:
    enrollment_account_name: myEnrollmentAccount
    body:
      offerType: MS-AZR-0017P
      displayName: Test Ea Azure Sub
      owners:
        - objectId: 973034ff-acb7-409c-b731-e789672c7b31
        - objectId: 67439a9e-8519-4016-a630-f5f805eba567
      additionalParameters:
        customData:
          key1: value1
          key2: true
'''

RETURN = '''
subscription_link:
  description:
    - The link to the new subscription.
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
from msrestazure.azure_exceptions import CloudError


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMSubscriptionFactory(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            enrollment_account_name=dict(
                type='str',
                updatable=False,
                disposition='enrollmentAccountName',
                required=True
            ),
            display_name=dict(
                type='str',
                updatable=False,
                disposition='/displayName'
            ),
            owners=dict(
                type='list',
                disposition='/',
                options=dict(
                    object_id=dict(
                        type='str',
                        disposition='objectId',
                        required=True
                    )
                )
            ),
            offer_type=dict(
                type='str',
                updatable=False,
                disposition='/offerType',
                choices=['MS-AZR-0017P',
                         'MS-AZR-0148P']
            ),
            additional_parameters=dict(
                type='raw',
                updatable=False,
                disposition='/additionalParameters'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.enrollment_account_name = None
        self.subscription_link = None

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

        super(AzureRMSubscriptionFactory, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                         supports_check_mode=True,
                                                         supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        response = None

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        self.url = ('/providers' +
                    '/Microsoft.Billing' +
                    '/enrollmentAccounts' +
                    '/{{ enrollment_account_name }}' +
                    '/providers' +
                    '/Microsoft.Subscription' +
                    '/createSubscription')
        self.url = self.url.replace('{{ enrollment_account_name }}', self.enrollment_account_name)

        if self.check_mode:
            self.results['changed'] = True
            return self.results

        response = self.create_update_resource()

        if response:
            self.results['changed'] = True
            self.results["subscription_link"] = response["subscription_link"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the SubscriptionFactory instance {0}'.format(self.))

        try:
            response = self.mgmt_client.query(self.url,
                                              'POST',
                                              self.query_parameters,
                                              self.header_parameters,
                                              self.body,
                                              self.status_code,
                                              600,
                                              30)
        except CloudError as exc:
            self.log('Error attempting to create the SubscriptionFactory instance.')
            self.fail('Error creating the SubscriptionFactory instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response


def main():
    AzureRMSubscriptionFactory()


if __name__ == '__main__':
    main()
