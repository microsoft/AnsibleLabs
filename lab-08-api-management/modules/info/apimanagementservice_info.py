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
module: apimanagementservice_info
version_added: '2.9'
short_description: Get ApiManagementService info.
description:
  - Get info of ApiManagementService.
options:
  resource_group:
    description:
      - The name of the resource group.
    type: str
  name:
    description:
      - Resource name.
    type: str
  id:
    description:
      - Resource ID.
    type: str
  type:
    description:
      - >-
        Resource type for API Management resource is set to
        Microsoft.ApiManagement.
    type: str
  notification_sender_email:
    description:
      - Email address from which the notification will be sent.
    type: str
  provisioning_state:
    description:
      - >-
        The current provisioning state of the API Management service which can
        be one of the following:
        Created/Activating/Succeeded/Updating/Failed/Stopped/Terminating/TerminationFailed/Deleted.
    type: str
  target_provisioning_state:
    description:
      - >-
        The provisioning state of the API Management service, which is targeted
        by the long running operation started on the service.
    type: str
  created_at_utc:
    description:
      - >-
        Creation UTC date of the API Management service.The date conforms to the
        following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601
        standard.
    type: datetime
  gateway_url:
    description:
      - Gateway URL of the API Management service.
    type: str
  gateway_regional_url:
    description:
      - Gateway URL of the API Management service in the Default Region.
    type: str
  portal_url:
    description:
      - Publisher portal endpoint Url of the API Management service.
    type: str
  management_api_url:
    description:
      - Management API endpoint URL of the API Management service.
    type: str
  scm_url:
    description:
      - SCM endpoint URL of the API Management service.
    type: str
  hostname_configurations:
    description:
      - Custom hostname configuration of the API Management service.
    type: list
    suboptions:
      type:
        description:
          - Hostname type.
        required: true
        type: str
      host_name:
        description:
          - Hostname to configure on the Api Management service.
        required: true
        type: str
      key_vault_id:
        description:
          - >-
            Url to the KeyVault Secret containing the Ssl Certificate. If
            absolute Url containing version is provided, auto-update of ssl
            certificate will not work. This requires Api Management service to
            be configured with MSI. The secret should be of type
            *application/x-pkcs12*
        type: str
      encoded_certificate:
        description:
          - Base64 Encoded certificate.
        type: str
      certificate_password:
        description:
          - Certificate Password.
        type: str
      default_ssl_binding:
        description:
          - >-
            Specify true to setup the certificate associated with this Hostname
            as the Default SSL Certificate. If a client does not send the SNI
            header, then this will be the certificate that will be challenged.
            The property is useful if a service has multiple custom hostname
            enabled and it needs to decide on the default ssl certificate. The
            setting only applied to Proxy Hostname Type.
        type: boolean
      negotiate_client_certificate:
        description:
          - >-
            Specify true to always negotiate client certificate on the hostname.
            Default Value is false.
        type: boolean
      certificate:
        description:
          - Certificate information.
        type: dict
        suboptions:
          expiry:
            description:
              - >-
                Expiration date of the certificate. The date conforms to the
                following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
                8601 standard.
            required: true
            type: datetime
          thumbprint:
            description:
              - Thumbprint of the certificate.
            required: true
            type: str
          subject:
            description:
              - Subject of the certificate.
            required: true
            type: str
  public_ip_addresses:
    description:
      - >-
        Public Static Load Balanced IP addresses of the API Management service
        in Primary region. Available only for Basic, Standard and Premium SKU.
    type: list
  private_ip_addresses:
    description:
      - >-
        Private Static Load Balanced IP addresses of the API Management service
        in Primary region which is deployed in an Internal Virtual Network.
        Available only for Basic, Standard and Premium SKU.
    type: list
  virtual_network_configuration:
    description:
      - Virtual network configuration of the API Management service.
    type: dict
    suboptions:
      vnetid:
        description:
          - >-
            The virtual network ID. This is typically a GUID. Expect a null GUID
            by default.
        type: str
      subnetname:
        description:
          - The name of the subnet.
        type: str
      subnet_resource_id:
        description:
          - >-
            The full resource ID of a subnet in a virtual network to deploy the
            API Management service in.
        type: str
  additional_locations:
    description:
      - Additional datacenter locations of the API Management service.
    type: list
    suboptions:
      location:
        description:
          - >-
            The location name of the additional region among Azure Data center
            regions.
        required: true
        type: str
      sku:
        description:
          - SKU properties of the API Management service.
        required: true
        type: dict
        suboptions:
          name:
            description:
              - Name of the Sku.
            required: true
            type: str
          capacity:
            description:
              - Capacity of the SKU (number of deployed units of the SKU).
            type: number
      public_ip_addresses:
        description:
          - >-
            Public Static Load Balanced IP addresses of the API Management
            service in the additional location. Available only for Basic,
            Standard and Premium SKU.
        type: list
      private_ip_addresses:
        description:
          - >-
            Private Static Load Balanced IP addresses of the API Management
            service which is deployed in an Internal Virtual Network in a
            particular additional location. Available only for Basic, Standard
            and Premium SKU.
        type: list
      virtual_network_configuration:
        description:
          - Virtual network configuration for the location.
        type: dict
        suboptions:
          vnetid:
            description:
              - >-
                The virtual network ID. This is typically a GUID. Expect a null
                GUID by default.
            type: str
          subnetname:
            description:
              - The name of the subnet.
            type: str
          subnet_resource_id:
            description:
              - >-
                The full resource ID of a subnet in a virtual network to deploy
                the API Management service in.
            type: str
      gateway_regional_url:
        description:
          - Gateway URL of the API Management service in the Region.
        type: str
  custom_properties:
    description:
      - >-
        Custom properties of the API Management service.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TripleDes168`
        will disable the cipher TLS_RSA_WITH_3DES_EDE_CBC_SHA for all TLS(1.0,
        1.1 and 1.2).</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls11`
        can be used to disable just TLS 1.1.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Protocols.Tls10`
        can be used to disable TLS 1.0 on an API Management service.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls11`
        can be used to disable just TLS 1.1 for communications with
        backends.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Backend.Protocols.Tls10`
        can be used to disable TLS 1.0 for communications with
        backends.</br>Setting
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Protocols.Server.Http2`
        can be used to enable HTTP2 protocol on an API Management
        service.</br>Not specifying any of these properties on PATCH operation
        will reset omitted properties' values to their defaults. For all the
        settings except Http2 the default value is `True` if the service was
        created on or before April 1st 2018 and `False` otherwise. Http2
        setting's default value is `False`.</br></br>You can disable any of next
        ciphers by using settings
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.[cipher_name]`:
        TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA,
        TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA,
        TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA,
        TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256,
        TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA,
        TLS_RSA_WITH_AES_128_CBC_SHA. For example,
        `Microsoft.WindowsAzure.ApiManagement.Gateway.Security.Ciphers.TLS_RSA_WITH_AES_128_CBC_SHA256`:`false`.
        The default value is `true` for them.
    type: str
  certificates:
    description:
      - >-
        List of Certificates that need to be installed in the API Management
        service. Max supported certificates that can be installed is 10.
    type: list
    suboptions:
      encoded_certificate:
        description:
          - Base64 Encoded certificate.
        type: str
      certificate_password:
        description:
          - Certificate Password.
        type: str
      store_name:
        description:
          - >-
            The System.Security.Cryptography.x509certificates.StoreName
            certificate store location. Only Root and CertificateAuthority are
            valid locations.
        required: true
        type: str
      certificate:
        description:
          - Certificate information.
        type: dict
        suboptions:
          expiry:
            description:
              - >-
                Expiration date of the certificate. The date conforms to the
                following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO
                8601 standard.
            required: true
            type: datetime
          thumbprint:
            description:
              - Thumbprint of the certificate.
            required: true
            type: str
          subject:
            description:
              - Subject of the certificate.
            required: true
            type: str
  enable_client_certificate:
    description:
      - >-
        Property only meant to be used for Consumption SKU Service. This
        enforces a client certificate to be presented on each request to the
        gateway. This also enables the ability to authenticate the certificate
        in the policy on the gateway.
    type: boolean
  virtual_network_type:
    description:
      - >-
        The type of VPN in which API Management service needs to be configured
        in. None (Default Value) means the API Management service is not part of
        any Virtual Network, External means the API Management deployment is set
        up inside a Virtual Network having an Internet Facing Endpoint, and
        Internal means that API Management deployment is setup inside a Virtual
        Network having an Intranet Facing Endpoint only.
    type: str
  publisher_email:
    description:
      - Publisher email.
    required: true
    type: str
  publisher_name:
    description:
      - Publisher name.
    required: true
    type: str
  sku_name:
    description:
      - Name of the Sku.
    required: true
    type: str
  sku_capacity:
    description:
      - Capacity of the SKU (number of deployed units of the SKU).
    type: number
  identity:
    description:
      - Managed service identity of the Api Management service.
    type: dict
    suboptions:
      type:
        description:
          - >-
            The identity type. Currently the only supported type is
            'SystemAssigned'.
        required: true
        type: str
      principal_id:
        description:
          - The principal id of the identity.
        type: 'unknown-primary[uuid]'
      tenant_id:
        description:
          - The client tenant id of the identity.
        type: 'unknown-primary[uuid]'
  location:
    description:
      - Resource location.
    type: str
  etag:
    description:
      - ETag of the resource.
    type: str
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: ApiManagementListServiceBySubscription
  azure.rm.apimanagementservice_info:
- name: ApiManagementListServiceBySubscriptionAndResourceGroup
  azure.rm.apimanagementservice_info:
    resource_group: myResourceGroup
- name: ApiManagementServiceGetService
  azure.rm.apimanagementservice_info:
    resource_group: myResourceGroup
    name: myService

'''

RETURN = '''
api_management_service:
  description: >-
    A list of dict results where the key is the name of the ApiManagementService
    and the values are the facts for that ApiManagementService.
  returned: always
  type: complex
  contains:
    apimanagementservice_name:
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
            - >-
              Resource type for API Management resource is set to
              Microsoft.ApiManagement.
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags.
          returned: always
          type: str
          sample: null
        properties:
          description:
            - Properties of the API Management service.
          returned: always
          type: dict
          sample: null
        sku:
          description:
            - SKU properties of the API Management service.
          returned: always
          type: dict
          sample: null
        identity:
          description:
            - Managed service identity of the Api Management service.
          returned: always
          type: dict
          sample: null
          contains:
            type:
              description:
                - >-
                  The identity type. Currently the only supported type is
                  'SystemAssigned'.
              returned: always
              type: str
              sample: null
            principal_id:
              description:
                - The principal id of the identity.
              returned: always
              type: 'unknown-primary[uuid]'
              sample: null
            tenant_id:
              description:
                - The client tenant id of the identity.
              returned: always
              type: 'unknown-primary[uuid]'
              sample: null
        location:
          description:
            - Resource location.
          returned: always
          type: str
          sample: null
        etag:
          description:
            - ETag of the resource.
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


class AzureRMApiManagementServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None
       
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
        super(AzureRMApiManagementServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['api_management_service'] = self.get()
        elif (self.resource_group is not None):
            self.results['api_management_service'] = self.listbyresourcegroup()
        else:
            self.results['api_management_service'] = self.list()
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
                    '/{{ service_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.name)

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

    def listbyresourcegroup(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/resourceGroups' +
                    '/{{ resource_group }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
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
            results = json.loads(response.text)
            # self.log('Response : {0}'.format(response))
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return [self.format_item(x) for x in results['value']] if results['value'] else []

    def list(self):
        response = None
        results = {}
        # prepare url
        self.url = ('/subscriptions' +
                    '/{{ subscription_id }}' +
                    '/providers' +
                    '/Microsoft.ApiManagement' +
                    '/service')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
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
            'sku_name': item['sku']['name'],
            'properties': item['properties']
        }
        return d

def main():
    AzureRMApiManagementServiceInfo()


if __name__ == '__main__':
    main()
