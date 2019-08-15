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
module: apimanagementapiissueattachment_info
version_added: '2.9'
short_description: Get ApiIssueAttachment info.
description:
  - Get info of ApiIssueAttachment.
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
  api_id:
    description:
      - >-
        API identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  issue_id:
    description:
      - >-
        Issue identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  attachment_id:
    description:
      - >-
        Attachment identifier within an Issue. Must be unique in the current
        Issue.
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
  title:
    description:
      - Filename by which the binary data will be saved.
    required: true
    type: str
  content_format:
    description:
      - >-
        Either 'link' if content is provided via an HTTP link or the MIME type
        of the Base64-encoded binary data provided in the 'content' property.
    required: true
    type: str
  content:
    description:
      - An HTTP link or Base64-encoded binary data.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListApiIssueAttachments
  azure.rm.apimanagementapiissueattachment_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
- name: ApiManagementGetApiIssueAttachment
  azure.rm.apimanagementapiissueattachment_info:
    resource_group: myResourceGroup
    service_name: myService
    api_id: myApi
    issue_id: myIssue
    attachment_id: myAttachment

'''

RETURN = '''
api_issue_attachment:
  description: >-
    A list of dict results where the key is the name of the ApiIssueAttachment
    and the values are the facts for that ApiIssueAttachment.
  returned: always
  type: complex
  contains:
    apiissueattachment_name:
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
            - Properties of the Issue Attachment.
          returned: always
          type: dict
          sample: null

'''

import time
import json
from ansible.module_utils.azure_rm_common import AzureRMModuleBase
from ansible.module_utils.azure_rm_common_rest import GenericRestClient
from copy import deepcopy
try:
  from msrestazure.azure_exceptions import CloudError
except ImportError:
  # This is handled in azure_rm_common
  pass


class AzureRMApiIssueAttachmentInfo(AzureRMModuleBase):
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
            api_id=dict(
                type='str',
                required=True
            ),
            issue_id=dict(
                type='str',
                required=True
            ),
            attachment_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.api_id = None
        self.issue_id = None
        self.attachment_id = None

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
        super(AzureRMApiIssueAttachmentInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.api_id is not None and
            self.issue_id is not None and
            self.attachment_id is not None):
            self.results['api_issue_attachment'] = self.get()
        elif (self.resource_group is not None and
              self.service_name is not None and
              self.api_id is not None and
              self.issue_id is not None):
            self.results['api_issue_attachment'] = self.listbyservice()
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
                    '/apis' +
                    '/{{ api_name }}' +
                    '/issues' +
                    '/{{ issue_name }}' +
                    '/attachments' +
                    '/{{ attachment_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_id)
        self.url = self.url.replace('{{ issue_name }}', self.issue_id)
        self.url = self.url.replace('{{ attachment_name }}', self.attachment_id)

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

        return self.format_item(results)

    def listbyservice(self):
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
                    '/apis' +
                    '/{{ api_name }}' +
                    '/issues' +
                    '/{{ issue_name }}' +
                    '/attachments')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ api_name }}', self.api_id)
        self.url = self.url.replace('{{ issue_name }}', self.issue_id)

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
    AzureRMApiIssueAttachmentInfo()


if __name__ == '__main__':
    main()
