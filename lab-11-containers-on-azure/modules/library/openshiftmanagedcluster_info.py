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
module: openshiftmanagedcluster_info
version_added: '2.9'
short_description: Get OpenShiftManagedCluster info.
description:
  - Get info of OpenShiftManagedCluster.
options:
  resource_group:
    description:
      - The name of the resource group.
    type: str
  name:
    description:
      - Resource name
    type: str
  id:
    description:
      - Resource Id
    type: str
  type:
    description:
      - Resource type
    type: str
  location:
    description:
      - Resource location
    type: str
  plan:
    description:
      - Define the resource plan as required by ARM for billing purposes
    type: dict
    suboptions:
      name:
        description:
          - The plan ID.
        type: str
      product:
        description:
          - >-
            Specifies the product of the image from the marketplace. This is the
            same value as Offer under the imageReference element.
        type: str
      promotion_code:
        description:
          - The promotion code.
        type: str
      publisher:
        description:
          - The plan ID.
        type: str
  provisioning_state:
    description:
      - >-
        The current deployment or provisioning state, which only appears in the
        response.
    type: str
  open_shift_version:
    description:
      - Version of OpenShift specified when creating the cluster.
    required: true
    type: str
  cluster_version:
    description:
      - Version of OpenShift specified when creating the cluster.
    type: str
  public_hostname:
    description:
      - Service generated FQDN for OpenShift API server.
    type: str
  fqdn:
    description:
      - >-
        Service generated FQDN for OpenShift API server loadbalancer internal
        hostname.
    type: str
  network_profile:
    description:
      - Configuration for OpenShift networking.
    type: dict
    suboptions:
      vnet_cidr:
        description:
          - CIDR for the OpenShift Vnet.
        type: str
      peer_vnet_id:
        description:
          - CIDR of the Vnet to peer.
        type: str
      vnet_id:
        description:
          - ID of the Vnet created for OSA cluster.
        type: str
  router_profiles:
    description:
      - Configuration for OpenShift router(s).
    type: list
    suboptions:
      name:
        description:
          - Name of the router profile.
        type: str
      public_subdomain:
        description:
          - DNS subdomain for OpenShift router.
        type: str
      fqdn:
        description:
          - Auto-allocated FQDN for the OpenShift router.
        type: str
  master_pool_profile:
    description:
      - Configuration for OpenShift master VMs.
    type: dict
    suboptions:
      name:
        description:
          - >-
            Unique name of the master pool profile in the context of the
            subscription and resource group.
        type: str
      count:
        description:
          - >-
            Number of masters (VMs) to host docker containers. The default value
            is 3.
        required: true
        type: number
      vm_size:
        description:
          - Size of agent VMs.
        required: true
        type: str
      subnet_cidr:
        description:
          - Subnet CIDR for the peering.
        type: str
      os_type:
        description:
          - >-
            OsType to be used to specify os type. Choose from Linux and Windows.
            Default to Linux.
        type: str
  agent_pool_profiles:
    description:
      - Configuration of OpenShift cluster VMs.
    type: list
    suboptions:
      name:
        description:
          - >-
            Unique name of the pool profile in the context of the subscription
            and resource group.
        required: true
        type: str
      count:
        description:
          - Number of agents (VMs) to host docker containers.
        required: true
        type: number
      vm_size:
        description:
          - Size of agent VMs.
        required: true
        type: str
      subnet_cidr:
        description:
          - Subnet CIDR for the peering.
        type: str
      os_type:
        description:
          - >-
            OsType to be used to specify os type. Choose from Linux and Windows.
            Default to Linux.
        type: str
      role:
        description:
          - Define the role of the AgentPoolProfile.
        type: str
  auth_profile:
    description:
      - Configures OpenShift authentication.
    type: dict
    suboptions:
      identity_providers:
        description:
          - Type of authentication profile to use.
        type: list
        suboptions:
          name:
            description:
              - Name of the provider.
            type: str
          provider:
            description:
              - Configuration of the provider.
            type: dict
extends_documentation_fragment:
  - azure
author:
  - Zim Kalinowski (@zikalino)

'''

EXAMPLES = '''
- name: List Managed Clusters
  azure.rm.openshiftmanagedcluster_info:
- name: Get Managed Clusters by Resource Group
  azure.rm.openshiftmanagedcluster_info:
    resource_group: myResourceGroup
- name: Get OpenShift Managed Cluster
  azure.rm.openshiftmanagedcluster_info:
    resource_group: myResourceGroup
    name: myOpenShiftManagedCluster

'''

RETURN = '''
open_shift_managed_clusters:
  description: >-
    A list of dict results where the key is the name of the
    OpenShiftManagedCluster and the values are the facts for that
    OpenShiftManagedCluster.
  returned: always
  type: complex
  contains:
    openshiftmanagedcluster_name:
      description: The key is the name of the server that the values relate to.
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
          type: str
          sample: null
        location:
          description:
            - Resource location
          returned: always
          type: str
          sample: null
        tags:
          description:
            - Resource tags
          returned: always
          type: str
          sample: null
        plan:
          description:
            - Define the resource plan as required by ARM for billing purposes
          returned: always
          type: dict
          sample: null
          contains:
            name:
              description:
                - The plan ID.
              returned: always
              type: str
              sample: null
            product:
              description:
                - >-
                  Specifies the product of the image from the marketplace. This
                  is the same value as Offer under the imageReference element.
              returned: always
              type: str
              sample: null
            promotion_code:
              description:
                - The promotion code.
              returned: always
              type: str
              sample: null
            publisher:
              description:
                - The plan ID.
              returned: always
              type: str
              sample: null
        properties:
          description:
            - Properties of a OpenShift managed cluster.
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
    # this is handled in azure_rm_common
    pass


class AzureRMOpenShiftManagedClustersInfo(AzureRMModuleBase):
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
        self.location = None
        self.tags = None
        self.plan = None
        self.properties = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-04-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOpenShiftManagedClustersInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(GenericRestClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager)

        if (self.resource_group is not None and
            self.name is not None):
            self.results['open_shift_managed_clusters'] = self.get()
        elif (self.resource_group is not None):
            self.results['open_shift_managed_clusters'] = self.listbyresourcegroup()
        else:
            self.results['open_shift_managed_clusters'] = self.list()
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
                    '/Microsoft.ContainerService' +
                    '/openShiftManagedClusters' +
                    '/{{ open_shift_managed_cluster_name }}')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ open_shift_managed_cluster_name }}', self.name)

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
                    '/Microsoft.ContainerService' +
                    '/openShiftManagedClusters')
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
                    '/Microsoft.ContainerService' +
                    '/openShiftManagedClusters')
        self.url = self.url.replace('{{ subscription_id }}', self.subscription_id)
        self.url = self.url.replace('{{ resource_group }}', self.resource_group)
        self.url = self.url.replace('{{ open_shift_managed_cluster_name }}', self.name)

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
            'location': item['location'],
            'tags': item.get('tags'),
            'properties': item['properties']
        }
        return d


def main():
    AzureRMOpenShiftManagedClustersInfo()


if __name__ == '__main__':
    main()
