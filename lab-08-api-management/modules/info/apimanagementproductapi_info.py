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
module: apimanagementproductapi_info
version_added: '2.9'
short_description: Get ProductApi info.
description:
  - Get info of ProductApi.
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
  product_id:
    description:
      - >-
        Product identifier. Must be unique in the current API Management service
        instance.
    required: true
    type: str
  value:
    description:
      - Page values.
    type: list
    suboptions:
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
          - Type of API.
        type: str
      description:
        description:
          - Description of the API. May include HTML formatting tags.
        type: str
      authentication_settings:
        description:
          - Collection of authentication settings included into this API.
        type: dict
        suboptions:
          o_auth2:
            description:
              - OAuth2 Authentication settings
            type: dict
            suboptions:
              authorization_server_id:
                description:
                  - OAuth authorization server identifier.
                type: str
              scope:
                description:
                  - operations scope.
                type: str
          openid:
            description:
              - OpenID Connect Authentication Settings
            type: dict
            suboptions:
              openid_provider_id:
                description:
                  - OAuth authorization server identifier.
                type: str
              bearer_token_sending_methods:
                description:
                  - How to send token to the server.
                type: list
          subscription_key_required:
            description:
              - >-
                Specifies whether subscription key is required during call to
                this API, true - API is included into closed products only,
                false - API is included into open products alone, null - there
                is a mix of products.
            type: boolean
      subscription_key_parameter_names:
        description:
          - Protocols over which API is made available.
        type: dict
        suboptions:
          header:
            description:
              - Subscription key header name.
            type: str
          query:
            description:
              - Subscription key query string parameter name.
            type: str
      api_revision:
        description:
          - >-
            Describes the Revision of the Api. If no value is provided, default
            revision 1 is created
        type: str
      api_version:
        description:
          - Indicates the Version identifier of the API if the API is versioned
        type: str
      is_current:
        description:
          - Indicates if API revision is current api revision.
        type: boolean
      is_online:
        description:
          - Indicates if API revision is accessible via the gateway.
        type: boolean
      api_revision_description:
        description:
          - Description of the Api Revision.
        type: str
      api_version_description:
        description:
          - Description of the Api Version.
        type: str
      api_version_set_id:
        description:
          - A resource identifier for the related ApiVersionSet.
        type: str
      subscription_required:
        description:
          - >-
            Specifies whether an API or Product subscription is required for
            accessing the API.
        type: boolean
      source_api_id:
        description:
          - API identifier of the source API.
        type: str
      display_name:
        description:
          - API name. Must be 1 to 300 characters long.
        type: str
      service_url:
        description:
          - >-
            Absolute URL of the backend service implementing this API. Cannot be
            more than 2000 characters long.
        type: str
      path:
        description:
          - >-
            Relative URL uniquely identifying this API and all of its resource
            paths within the API Management service instance. It is appended to
            the API endpoint base URL specified during the service instance
            creation to form a public URL for this API.
        required: true
        type: str
      protocols:
        description:
          - >-
            Describes on which protocols the operations in this API can be
            invoked.
        type: list
      api_version_set:
        description:
          - Version set details
        type: dict
        suboptions:
          id:
            description:
              - >-
                Identifier for existing API Version Set. Omit this value to
                create a new Version Set.
            type: str
          name:
            description:
              - The display Name of the API Version Set.
            type: str
          description:
            description:
              - Description of API Version Set.
            type: str
          versioning_scheme:
            description:
              - >-
                An value that determines where the API Version identifer will be
                located in a HTTP request.
            type: str
          version_query_name:
            description:
              - >-
                Name of query parameter that indicates the API Version if
                versioningScheme is set to `query`.
            type: str
          version_header_name:
            description:
              - >-
                Name of HTTP header parameter that indicates the API Version if
                versioningScheme is set to `header`.
            type: str
  next_link:
    description:
      - Next page link if any.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListProductApis
  azure.rm.apimanagementproductapi_info:
    resource_group: myResourceGroup
    service_name: myService
    product_id: myProduct

'''

RETURN = '''
product_api:
  description: >-
    A list of dict results where the key is the name of the ProductApi and the
    values are the facts for that ProductApi.
  returned: always
  type: complex
  contains:
    productapi_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        value:
          description:
            - Page values.
          returned: always
          type: dict
          sample: null
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
                - Type of API.
              returned: always
              type: str
              sample: null
            properties:
              description:
                - Api entity contract properties.
              returned: always
              type: dict
              sample: null
            description:
              description:
                - Description of the API. May include HTML formatting tags.
              returned: always
              type: str
              sample: null
            authentication_settings:
              description:
                - Collection of authentication settings included into this API.
              returned: always
              type: dict
              sample: null
              contains:
                o_auth2:
                  description:
                    - OAuth2 Authentication settings
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    authorization_server_id:
                      description:
                        - OAuth authorization server identifier.
                      returned: always
                      type: str
                      sample: null
                    scope:
                      description:
                        - operations scope.
                      returned: always
                      type: str
                      sample: null
                openid:
                  description:
                    - OpenID Connect Authentication Settings
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    openid_provider_id:
                      description:
                        - OAuth authorization server identifier.
                      returned: always
                      type: str
                      sample: null
                    bearer_token_sending_methods:
                      description:
                        - How to send token to the server.
                      returned: always
                      type: str
                      sample: null
                subscription_key_required:
                  description:
                    - >-
                      Specifies whether subscription key is required during call
                      to this API, true - API is included into closed products
                      only, false - API is included into open products alone,
                      null - there is a mix of products.
                  returned: always
                  type: boolean
                  sample: null
            subscription_key_parameter_names:
              description:
                - Protocols over which API is made available.
              returned: always
              type: dict
              sample: null
              contains:
                header:
                  description:
                    - Subscription key header name.
                  returned: always
                  type: str
                  sample: null
                query:
                  description:
                    - Subscription key query string parameter name.
                  returned: always
                  type: str
                  sample: null
            api_revision:
              description:
                - >-
                  Describes the Revision of the Api. If no value is provided,
                  default revision 1 is created
              returned: always
              type: str
              sample: null
            api_version:
              description:
                - >-
                  Indicates the Version identifier of the API if the API is
                  versioned
              returned: always
              type: str
              sample: null
            is_current:
              description:
                - Indicates if API revision is current api revision.
              returned: always
              type: boolean
              sample: null
            is_online:
              description:
                - Indicates if API revision is accessible via the gateway.
              returned: always
              type: boolean
              sample: null
            api_revision_description:
              description:
                - Description of the Api Revision.
              returned: always
              type: str
              sample: null
            api_version_description:
              description:
                - Description of the Api Version.
              returned: always
              type: str
              sample: null
            api_version_set_id:
              description:
                - A resource identifier for the related ApiVersionSet.
              returned: always
              type: str
              sample: null
            subscription_required:
              description:
                - >-
                  Specifies whether an API or Product subscription is required
                  for accessing the API.
              returned: always
              type: boolean
              sample: null
            source_api_id:
              description:
                - API identifier of the source API.
              returned: always
              type: str
              sample: null
            display_name:
              description:
                - API name. Must be 1 to 300 characters long.
              returned: always
              type: str
              sample: null
            service_url:
              description:
                - >-
                  Absolute URL of the backend service implementing this API.
                  Cannot be more than 2000 characters long.
              returned: always
              type: str
              sample: null
            path:
              description:
                - >-
                  Relative URL uniquely identifying this API and all of its
                  resource paths within the API Management service instance. It
                  is appended to the API endpoint base URL specified during the
                  service instance creation to form a public URL for this API.
              returned: always
              type: str
              sample: null
            protocols:
              description:
                - >-
                  Describes on which protocols the operations in this API can be
                  invoked.
              returned: always
              type: str
              sample: null
            api_version_set:
              description:
                - Version set details
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - >-
                      Identifier for existing API Version Set. Omit this value
                      to create a new Version Set.
                  returned: always
                  type: str
                  sample: null
                name:
                  description:
                    - The display Name of the API Version Set.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - Description of API Version Set.
                  returned: always
                  type: str
                  sample: null
                versioning_scheme:
                  description:
                    - >-
                      An value that determines where the API Version identifer
                      will be located in a HTTP request.
                  returned: always
                  type: str
                  sample: null
                version_query_name:
                  description:
                    - >-
                      Name of query parameter that indicates the API Version if
                      versioningScheme is set to `query`.
                  returned: always
                  type: str
                  sample: null
                version_header_name:
                  description:
                    - >-
                      Name of HTTP header parameter that indicates the API
                      Version if versioningScheme is set to `header`.
                  returned: always
                  type: str
                  sample: null
        next_link:
          description:
            - Next page link if any.
          returned: always
          type: str
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


class AzureRMProductApiInfo(AzureRMModuleBase):
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
            product_id=dict(
                type='str',
                required=True
            )
        )

        self.resource_group = None
        self.service_name = None
        self.product_id = None
        self.value = None
        self.next_link = None

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
        super(AzureRMProductApiInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.service_name is not None and
            self.product_id is not None):
            self.results['product_api'] = self.listbyproduct()
        return self.results

    def listbyproduct(self):
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
                    '/{{ product_name }}' +
                    '/apis')
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
    AzureRMProductApiInfo()


if __name__ == '__main__':
    main()
