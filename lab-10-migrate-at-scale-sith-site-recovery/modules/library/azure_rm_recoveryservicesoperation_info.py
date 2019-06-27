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
module: azure_rm_recoveryservicesoperation_info
version_added: '2.9'
short_description: Get Operation info.
description:
  - Get info of Operation.
options:
  name:
    description:
      - >-
        The name of the resource group where the recovery services vault is
        present.
    required: true
  value:
    description:
      - The ClientDiscovery details.
    type: list
    suboptions:
      name:
        description:
          - >-
            Name of the API. The name of the operation being performed on this
            particular object. It should match the action name that appears in
            RBAC / the event service. Examples of operations include: *
            Microsoft.Compute/virtualMachine/capture/action *
            Microsoft.Compute/virtualMachine/restart/action *
            Microsoft.Compute/virtualMachine/write *
            Microsoft.Compute/virtualMachine/read *
            Microsoft.Compute/virtualMachine/delete Each action should include,
            in order: (1) Resource Provider Namespace (2) Type hierarchy for
            which the action applies (e.g. server/databases for a SQL Azure
            database) (3) Read, Write, Action or Delete indicating which type
            applies. If it is a PUT/PATCH on a collection or named value, Write
            should be used. If it is a GET, Read should be used. If it is a
            DELETE, Delete should be used. If it is a POST, Action should be
            used. As a note: all resource providers would need to include the
            "{Resource Provider Namespace}/register/action" operation in their
            response. This API is used to register for their service, and should
            include details about the operation (e.g. a localized name for the
            resource provider + any special considerations like PII release)
      display:
        description:
          - Object type
        suboptions:
          provider:
            description:
              - >-
                The provider. The localized friendly form of the resource
                provider name – it is expected to also include the
                publisher/company responsible. It should use Title Casing and
                begin with "Microsoft" for 1st party services. e.g. "Microsoft
                Monitoring Insights" or "Microsoft Compute."
          resource:
            description:
              - >-
                The resource. The localized friendly form of the resource
                related to this action/operation – it should match the public
                documentation for the resource provider. It should use Title
                Casing. This value should be unique for a particular URL type
                (e.g. nested types should *not* reuse their parent’s
                display.resource field). e.g. "Virtual Machines" or "Scheduler
                Job Collections", or "Virtual Machine VM Sizes" or "Scheduler
                Jobs"
          operation:
            description:
              - >-
                The operation. The localized friendly name for the operation, as
                it should be shown to the user. It should be concise (to fit in
                drop downs) but clear (i.e. self-documenting). It should use
                Title Casing. Prescriptive guidance: Read Create or Update
                Delete 'ActionName'
          description:
            description:
              - >-
                The description. The localized friendly description for the
                operation, as it should be shown to the user. It should be
                thorough, yet concise – it will be used in tool tips and
                detailed views. Prescriptive guidance for namespaces: Read any
                'display.provider' resource Create or Update any
                'display.provider' resource Delete any 'display.provider'
                resource Perform any other action on any 'display.provider'
                resource Prescriptive guidance for namespaces: Read any
                'display.resource' Create or Update any 'display.resource'
                Delete any 'display.resource' 'ActionName' any
                'display.resources'
      origin:
        description:
          - >-
            Origin. The intended executor of the operation; governs the display
            of the operation in the RBAC UX and the audit logs UX. Default value
            is "user,system"
  next_link:
    description:
      - The value of next link.
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: Returns the list of available operations.
  azure_rm_recoveryservicesoperation_info:
    name: myResourceGroup

'''

RETURN = '''
operations:
  description: >-
    A list of dict results where the key is the name of the Operation and the
    values are the facts for that Operation.
  returned: always
  type: complex
  contains:
    operation_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - The ClientDiscovery details.
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - >-
                  Name of the API. The name of the operation being performed on
                  this particular object. It should match the action name that
                  appears in RBAC / the event service. Examples of operations
                  include: * Microsoft.Compute/virtualMachine/capture/action *
                  Microsoft.Compute/virtualMachine/restart/action *
                  Microsoft.Compute/virtualMachine/write *
                  Microsoft.Compute/virtualMachine/read *
                  Microsoft.Compute/virtualMachine/delete Each action should
                  include, in order: (1) Resource Provider Namespace (2) Type
                  hierarchy for which the action applies (e.g. server/databases
                  for a SQL Azure database) (3) Read, Write, Action or Delete
                  indicating which type applies. If it is a PUT/PATCH on a
                  collection or named value, Write should be used. If it is a
                  GET, Read should be used. If it is a DELETE, Delete should be
                  used. If it is a POST, Action should be used. As a note: all
                  resource providers would need to include the "{Resource
                  Provider Namespace}/register/action" operation in their
                  response. This API is used to register for their service, and
                  should include details about the operation (e.g. a localized
                  name for the resource provider + any special considerations
                  like PII release)
              returned: always
              type: str
              sample: null
            display:
              description:
                - Object type
              returned: always
              type: dict
              sample: null
              contains:
                provider:
                  description:
                    - >-
                      The provider. The localized friendly form of the resource
                      provider name – it is expected to also include the
                      publisher/company responsible. It should use Title Casing
                      and begin with "Microsoft" for 1st party services. e.g.
                      "Microsoft Monitoring Insights" or "Microsoft Compute."
                  returned: always
                  type: str
                  sample: null
                resource:
                  description:
                    - >-
                      The resource. The localized friendly form of the resource
                      related to this action/operation – it should match the
                      public documentation for the resource provider. It should
                      use Title Casing. This value should be unique for a
                      particular URL type (e.g. nested types should *not* reuse
                      their parent’s display.resource field). e.g. "Virtual
                      Machines" or "Scheduler Job Collections", or "Virtual
                      Machine VM Sizes" or "Scheduler Jobs"
                  returned: always
                  type: str
                  sample: null
                operation:
                  description:
                    - >-
                      The operation. The localized friendly name for the
                      operation, as it should be shown to the user. It should be
                      concise (to fit in drop downs) but clear (i.e.
                      self-documenting). It should use Title Casing.
                      Prescriptive guidance: Read Create or Update Delete
                      'ActionName'
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - >-
                      The description. The localized friendly description for
                      the operation, as it should be shown to the user. It
                      should be thorough, yet concise – it will be used in tool
                      tips and detailed views. Prescriptive guidance for
                      namespaces: Read any 'display.provider' resource Create or
                      Update any 'display.provider' resource Delete any
                      'display.provider' resource Perform any other action on
                      any 'display.provider' resource Prescriptive guidance for
                      namespaces: Read any 'display.resource' Create or Update
                      any 'display.resource' Delete any 'display.resource'
                      'ActionName' any 'display.resources'
                  returned: always
                  type: str
                  sample: null
            origin:
              description:
                - >-
                  Origin. The intended executor of the operation; governs the
                  display of the operation in the RBAC UX and the audit logs UX.
                  Default value is "user,system"
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Properties. Reserved for future use.
              returned: always
              type: 'unknown-primary[object]'
              sample: null
        next_link:
          description:
            - The value of next link.
          returned: always
          type: str
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
from msrestazure.azure_exceptions import CloudError


class AzureRMOperationsInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(
                type='str',
                required=true
            )
        )

        self.name = None
        self.value = None
        self.next_link = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2018-07-10'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationsInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.name is not None):
            self.results['operations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/Subscriptions' +
                    '/{{ subscription_name }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.RecoveryServices' +
                    '/operations')
        self.url = self.url.replace('{{ subscription_name }}', self.subscription_name)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)

        try:
            response = self.mgmt_client.query(self.url,
                                              'GET',
                                              self.query_parameters,
                                              self.header_parameters,
                                              None,
                                              self.status_code,
                                              600,
                                              30)
            results['temp_item'] = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return results

    def format_item(item):
        return item


def main():
    AzureRMOperationsInfo()


if __name__ == '__main__':
    main()
