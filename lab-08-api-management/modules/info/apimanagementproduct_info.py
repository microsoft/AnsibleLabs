# -*- coding: utf-8 -*
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
module: apimanagementproduct_info
version_added: '2.9'
short_description: Get Product info.
description:
  - Get info of Product.
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
  expand_groups:
    description:
      - >-
        When set to true, the response contains an array of groups that have
        visibility to the product. The default is false.
    type: boolean
  include_not_tagged_products:
    description:
      - Include not tagged Products.
    type: boolean
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
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
  description:
    description:
      - Product description. May include HTML formatting tags.
    type: str
  terms:
    description:
      - >-
        Product terms of use. Developers trying to subscribe to the product will
        be presented and required to accept these terms before they can complete
        the subscription process.
    type: str
  subscription_required:
    description:
      - >-
        Whether a product subscription is required for accessing APIs included
        in this product. If true, the product is referred to as "protected" and
        a valid subscription key is required for a request to an API included in
        the product to succeed. If false, the product is referred to as "open"
        and requests to an API included in the product can be made without a
        subscription key. If property is omitted when creating a new product
        it's value is assumed to be true.
    type: boolean
  approval_required:
    description:
      - >-
        whether subscription approval is required. If false, new subscriptions
        will be approved automatically enabling developers to call the product’s
        APIs immediately after subscribing. If true, administrators must
        manually approve the subscription before the developer can any of the
        product’s APIs. Can be present only if subscriptionRequired property is
        present and has a value of false.
    type: boolean
  subscriptions_limit:
    description:
      - >-
        Whether the number of subscriptions a user can have to this product at
        the same time. Set to null or omit to allow unlimited per user
        subscriptions. Can be present only if subscriptionRequired property is
        present and has a value of false.
    type: number
  state:
    description:
      - >-
        whether product is published or not. Published products are discoverable
        by users of developer portal. Non published products are visible only to
        administrators. Default state of Product is notPublished.
    type: str
  display_name:
    description:
      - Product name.
    required: true
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListProducts
  azure.rm.apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementListProductsByTags
  azure.rm.apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
- name: ApiManagementGetProduct
  azure.rm.apimanagementproduct_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct

'''

RETURN = '''
product:
  description: >-
    A list of dict results where the key is the name of the Product and the
    values are the facts for that Product.
  returned: always
  type: complex
  contains:
    product_name:
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
            - Product entity contract properties.
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


class AzureRMProductInfo(AzureRMModuleBase):
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
            expand_groups=dict(
                type='bool'
            ),
            include_not_tagged_products=dict(
                type='bool'
            ),
            product_id=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.service_name = None
        self.expand_groups = None
        self.tags = None
        self.include_not_tagged_products = None
        self.product_id = None

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
        super(AzureRMProductInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None):
            self.results['product'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['product'] = self.format_item(self.listbytags())
        elif (self.resource_group is not None and
              self.service_name is not None):
            self.results['product'] = self.format_item(self.listbyservice())
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
                    '/products' +
                    '/{{ product_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ product_name }}', self.product_id)

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

    def listbytags(self):
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
                    '/productsByTags')
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
                    '/products')
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
    AzureRMProductInfo()


if __name__ == '__main__':
    main()
