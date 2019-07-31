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
module: apimanagementbackend
version_added: '2.9'
short_description: Manage Azure Backend instance.
description:
  - 'Create, update and delete instance of Azure Backend.'
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
  backend_id:
    description:
      - >-
        Identifier of the Backend entity. Must be unique in the current API
        Management service instance.
    required: true
    type: str
  title:
    description:
      - Backend Title.
    type: str
  description:
    description:
      - Backend Description.
    type: str
  resource_id:
    description:
      - >-
        Management Uri of the Resource in External System. This url can be the
        Arm Resource Id of Logic Apps, Function Apps or Api Apps.
    type: str
  service_fabric_cluster:
    description:
      - Backend Service Fabric Cluster Properties
    type: dict
    suboptions:
      client_certificatethumbprint:
        description:
          - The client certificate thumbprint for the management endpoint.
        required: true
        type: str
      max_partition_resolution_retries:
        description:
          - Maximum number of retries while attempting resolve the partition.
        type: str
      management_endpoints:
        description:
          - The cluster management endpoint.
        required: true
        type: list
      server_certificate_thumbprints:
        description:
          - >-
            Thumbprints of certificates cluster management service uses for tls
            communication
        type: list
      server_x509names:
        description:
          - Server X509 Certificate Names Collection
        type: list
        suboptions:
          name:
            description:
              - Common Name of the Certificate.
            type: str
          issuer_certificate_thumbprint:
            description:
              - Thumbprint for the Issuer of the Certificate.
            type: str
  credentials:
    description:
      - Backend Credentials Contract Properties
    type: dict
    suboptions:
      certificate:
        description:
          - List of Client Certificate Thumbprint.
        type: list
      query:
        description:
          - Query Parameter description.
        type: >-
          unknown[DictionaryType
          {"$id":"1845","$type":"DictionaryType","valueType":{"$id":"1846","$type":"SequenceType","elementType":{"$id":"1847","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"1848","fixed":false,"raw":"String"},"deprecated":false},"name":{"$id":"1849","fixed":false},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"1850","fixed":false},"deprecated":false}]
      header:
        description:
          - Header Parameter description.
        type: >-
          unknown[DictionaryType
          {"$id":"1855","$type":"DictionaryType","valueType":{"$id":"1856","$type":"SequenceType","elementType":{"$id":"1857","$type":"PrimaryType","knownPrimaryType":"string","name":{"$id":"1858","fixed":false,"raw":"String"},"deprecated":false},"name":{"$id":"1859","fixed":false},"deprecated":false},"supportsAdditionalProperties":false,"name":{"$id":"1860","fixed":false},"deprecated":false}]
      authorization:
        description:
          - Authorization header authentication
        type: dict
        suboptions:
          scheme:
            description:
              - Authentication Scheme name.
            required: true
            type: str
          parameter:
            description:
              - Authentication Parameter value.
            required: true
            type: str
  proxy:
    description:
      - Backend Proxy Contract Properties
    type: dict
    suboptions:
      url:
        description:
          - >-
            WebProxy Server AbsoluteUri property which includes the entire URI
            stored in the Uri instance, including all fragments and query
            strings.
        required: true
        type: str
      username:
        description:
          - Username to connect to the WebProxy server
        type: str
      password:
        description:
          - Password to connect to the WebProxy Server
        type: str
  tls:
    description:
      - Backend TLS Properties
    type: dict
    suboptions:
      validate_certificate_chain:
        description:
          - >-
            Flag indicating whether SSL certificate chain validation should be
            done when using self-signed certificates for this backend host.
        type: bool
      validate_certificate_name:
        description:
          - >-
            Flag indicating whether SSL certificate name validation should be
            done when using self-signed certificates for this backend host.
        type: bool
  url:
    description:
      - Runtime Url of the Backend.
    required: true
    type: str
  protocol:
    description:
      - Backend communication protocol.
    required: true
    type: str
  state:
    description:
      - Assert the state of the Backend.
      - >-
        Use C(present) to create or update an Backend and C(absent) to delete
        it.
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
- name: ApiManagementCreateBackendServiceFabric
  azure.rm.apimanagementbackend:
    resource_group: myResourceGroup
    service_name: myService
    backend_id: myBackend
    description: "Service Fabric Test App 1"
    service_fabric_cluster:
      client_certificatethumbprint: EBA029198AA3E76EF0D70482626E5BCF148594A6
      max_partition_resolution_retries: '5'
      management_endpoints:
        - 'https://somecluster.com'
      server_x509names:
        - name: ServerCommonName1
          issuer_certificate_thumbprint: IssuerCertificateThumbprint1
    url: 'fabric:/mytestapp/mytestservice'
    protocol: http
- name: ApiManagementCreateBackendProxyBackend
  azure.rm.apimanagementbackend:
    resource_group: myResourceGroup
    service_name: myService
    backend_id: myBackend
    description: description5308
    credentials:
      query:
        sv:
          - xx
          - bb
          - cc
      header:
        x-my-1:
          - val1
          - val2
      authorization:
        scheme: Basic
        parameter: opensesma
    proxy:
      url: 'http://192.168.1.1:8080'
      username: Contoso\admin
      password: opensesame
    tls:
      validate_certificate_chain: true
      validate_certificate_name: true
    url: 'https://backendname2644/'
    protocol: http
- name: ApiManagementUpdateBackend
  azure.rm.apimanagementbackend:
    resource_group: myResourceGroup
    service_name: myService
    backend_id: myBackend
    description: description5308
    tls:
      validate_certificate_chain: false
      validate_certificate_name: true
- name: ApiManagementDeleteBackend
  azure.rm.apimanagementbackend:
    resource_group: myResourceGroup
    service_name: myService
    backend_id: myBackend
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
    - Backend entity contract properties.
  returned: always
  type: dict
  sample: null
  contains:
    title:
      description:
        - Backend Title.
      returned: always
      type: str
      sample: null
    description:
      description:
        - Backend Description.
      returned: always
      type: str
      sample: null
    resource_id:
      description:
        - >-
          Management Uri of the Resource in External System. This url can be the
          Arm Resource Id of Logic Apps, Function Apps or Api Apps.
      returned: always
      type: str
      sample: null
    properties:
      description:
        - Backend Properties contract
      returned: always
      type: dict
      sample: null
      contains:
        service_fabric_cluster:
          description:
            - Backend Service Fabric Cluster Properties
          returned: always
          type: dict
          sample: null
          contains:
            client_certificatethumbprint:
              description:
                - The client certificate thumbprint for the management endpoint.
              returned: always
              type: str
              sample: null
            max_partition_resolution_retries:
              description:
                - >-
                  Maximum number of retries while attempting resolve the
                  partition.
              returned: always
              type: str
              sample: null
            management_endpoints:
              description:
                - The cluster management endpoint.
              returned: always
              type: str
              sample: null
            server_certificate_thumbprints:
              description:
                - >-
                  Thumbprints of certificates cluster management service uses
                  for tls communication
              returned: always
              type: str
              sample: null
            server_x509names:
              description:
                - Server X509 Certificate Names Collection
              returned: always
              type: dict
              sample: null
              contains:
                name:
                  description:
                    - Common Name of the Certificate.
                  returned: always
                  type: str
                  sample: null
                issuer_certificate_thumbprint:
                  description:
                    - Thumbprint for the Issuer of the Certificate.
                  returned: always
                  type: str
                  sample: null
    credentials:
      description:
        - Backend Credentials Contract Properties
      returned: always
      type: dict
      sample: null
      contains:
        certificate:
          description:
            - List of Client Certificate Thumbprint.
          returned: always
          type: str
          sample: null
        query:
          description:
            - Query Parameter description.
          returned: always
          type: str
          sample: null
        header:
          description:
            - Header Parameter description.
          returned: always
          type: str
          sample: null
        authorization:
          description:
            - Authorization header authentication
          returned: always
          type: dict
          sample: null
          contains:
            scheme:
              description:
                - Authentication Scheme name.
              returned: always
              type: str
              sample: null
            parameter:
              description:
                - Authentication Parameter value.
              returned: always
              type: str
              sample: null
    proxy:
      description:
        - Backend Proxy Contract Properties
      returned: always
      type: dict
      sample: null
      contains:
        url:
          description:
            - >-
              WebProxy Server AbsoluteUri property which includes the entire URI
              stored in the Uri instance, including all fragments and query
              strings.
          returned: always
          type: str
          sample: null
        username:
          description:
            - Username to connect to the WebProxy server
          returned: always
          type: str
          sample: null
        password:
          description:
            - Password to connect to the WebProxy Server
          returned: always
          type: str
          sample: null
    tls:
      description:
        - Backend TLS Properties
      returned: always
      type: dict
      sample: null
      contains:
        validate_certificate_chain:
          description:
            - >-
              Flag indicating whether SSL certificate chain validation should be
              done when using self-signed certificates for this backend host.
          returned: always
          type: bool
          sample: null
        validate_certificate_name:
          description:
            - >-
              Flag indicating whether SSL certificate name validation should be
              done when using self-signed certificates for this backend host.
          returned: always
          type: bool
          sample: null
    url:
      description:
        - Runtime Url of the Backend.
      returned: always
      type: str
      sample: null
    protocol:
      description:
        - Backend communication protocol.
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
try:
    from msrestazure.azure_exceptions import CloudError
except ImportError:
    # this is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMBackend(AzureRMModuleBaseExt):
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
            backend_id=dict(
                type='str',
                updatable=False,
                disposition='backendId',
                required=True
            ),
            title=dict(
                type='str',
                disposition='/properties/*'
            ),
            description=dict(
                type='str',
                disposition='/properties/*'
            ),
            resource_id=dict(
                type='str',
                disposition='/properties/resourceId'
            ),
            service_fabric_cluster=dict(
                type='dict',
                disposition='/properties/properties/serviceFabricCluster',
                options=dict(
                    client_certificatethumbprint=dict(
                        type='str',
                        disposition='clientCertificatethumbprint',
                        required=True
                    ),
                    max_partition_resolution_retries=dict(
                        type='str',
                        disposition='maxPartitionResolutionRetries'
                    ),
                    management_endpoints=dict(
                        type='list',
                        disposition='managementEndpoints',
                        required=True
                    ),
                    server_certificate_thumbprints=dict(
                        type='list',
                        disposition='serverCertificateThumbprints'
                    ),
                    server_x509names=dict(
                        type='list',
                        disposition='serverX509Names',
                        options=dict(
                            name=dict(
                                type='str'
                            ),
                            issuer_certificate_thumbprint=dict(
                                type='str',
                                disposition='issuerCertificateThumbprint'
                            )
                        )
                    )
                )
            ),
            credentials=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    certificate=dict(
                        type='list'
                    ),
                    query=dict(
                        type='dict'
                    ),
                    header=dict(
                        type='dict'
                    ),
                    authorization=dict(
                        type='dict',
                        options=dict(
                            scheme=dict(
                                type='str',
                                required=True
                            ),
                            parameter=dict(
                                type='str',
                                required=True
                            )
                        )
                    )
                )
            ),
            proxy=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    url=dict(
                        type='str',
                        required=True
                    ),
                    username=dict(
                        type='str'
                    ),
                    password=dict(
                        type='str',
                        no_log=True
                    )
                )
            ),
            tls=dict(
                type='dict',
                disposition='/properties/*',
                options=dict(
                    validate_certificate_chain=dict(
                        type='bool',
                        disposition='validateCertificateChain'
                    ),
                    validate_certificate_name=dict(
                        type='bool',
                        disposition='validateCertificateName'
                    )
                )
            ),
            url=dict(
                type='str',
                disposition='/properties/*',
                required=True
            ),
            protocol=dict(
                type='str',
                disposition='/properties/*',
                choices=['http',
                         'soap'],
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.service_name = None
        self.backend_id = None

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

        super(AzureRMBackend, self).__init__(derived_arg_spec=self.module_arg_spec,
                                             supports_check_mode=True,
                                             supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            # if hasattr(self, key):
                # setattr(self, key, kwargs[key])
            # elif kwargs[key] is not None:
                # self.body[key] = kwargs[key]
            if kwargs[key] is not None and not hasattr(self, key):
                self.body[key] = kwargs[key]

        self.resource_group = kwargs['resource_group']
        self.service_name = kwargs['service_name']
        self.backend_id = kwargs['backend_id']
        self.body['url'] = kwargs['url']
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
                    '/backends' +
                    '/{{ backend_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ service_name }}', self.service_name)
        self.url = self.url.replace('{{ backend_name }}', self.backend_id)

        old_response = self.get_resource()

        if not old_response:
            self.log("Backend instance doesn't exist")

            if self.state == 'absent':
                self.log("Old instance didn't exist")
            else:
                self.to_do = Actions.Create
        else:
            self.log('Backend instance already exists')

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
            self.log('Need to Create / Update the Backend instance')

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
            self.log('Backend instance deleted')
            self.results['changed'] = True

            if self.check_mode:
                return self.results

            self.delete_resource()

            # make sure instance is actually deleted, for some Azure resources, instance is hanging around
            # for some time after deletion -- this should be really fixed in Azure
            while self.get_resource():
                time.sleep(20)
        else:
            self.log('Backend instance unchanged')
            self.results['changed'] = False
            response = old_response

        if response:
           self.results["id"] = response["id"]
           self.results["name"] = response["name"]
           self.results["type"] = response["type"]
           self.results["properties"] = response["properties"]

        return self.results

    def create_update_resource(self):
        # self.log('Creating / Updating the Backend instance {0}'.format(self.))

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
            self.log('Error attempting to create the Backend instance.')
            self.fail('Error creating the Backend instance: {0}'.format(str(exc)))

        try:
            response = json.loads(response.text)
        except Exception:
            response = {'text': response.text}
            pass

        return response

    def delete_resource(self):
        # self.log('Deleting the Backend instance {0}'.format(self.))
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
            self.log('Error attempting to delete the Backend instance.')
            self.fail('Error deleting the Backend instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        # self.log('Checking if the Backend instance {0} is present'.format(self.))
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
            # self.log("Backend instance : {0} found".format(response.name))
        except CloudError as e:
            self.log('Did not find the Backend instance.')
        if found is True:
            return response

        return False


def main():
    AzureRMBackend()


if __name__ == '__main__':
    main()
