# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make a copy of this file named 'secrets.py' and add your credentials there.
# Note you can run unit tests without setting your credentials.

BLUEBOX_PARAMS = ('customer_id', 'api_key')
BRIGHTBOX_PARAMS = ('client_id', 'client_secret')
DREAMHOST_PARAMS = ('key',)
EC2_PARAMS = ('access_id', 'secret')
ECP_PARAMS = ('user_name', 'password')
GANDI_PARAMS = ('user',)
HOSTINGCOM_PARAMS = ('user', 'secret')
IBM_PARAMS = ('user', 'secret')
# OPENSTACK_PARAMS = ('user_name', 'api_key', secure_bool, 'host', port_int)
OPENSTACK_PARAMS = ('user_name', 'api_key', False, 'host', 8774)
OPENNEBULA_PARAMS = ('user', 'key')
OPSOURCE_PARAMS = ('user', 'password')
RACKSPACE_PARAMS = ('user', 'key')
RACKSPACE_NOVA_PARAMS = ('user_name', 'api_key', False, 'host', 8774)
SLICEHOST_PARAMS = ('key',)
SOFTLAYER_PARAMS = ('user', 'api_key')
VCLOUD_PARAMS = ('user', 'secret')
VOXEL_PARAMS = ('key', 'secret')
VPSNET_PARAMS = ('user', 'key')
JOYENT_PARAMS = ('user', 'key')
VCL_PARAMS = ('user', 'pass', True, 'foo.bar.com')
GRIDSPOT_PARAMS = ('key',)
HOSTVIRTUAL_PARAMS = ('key',)
DIGITAL_OCEAN_PARAMS = ('user', 'key')

# Storage
STORAGE_S3_PARAMS = ('key', 'secret')
STORAGE_GOOGLE_STORAGE_PARAMS = ('key', 'secret')

# Azure key is b64 encoded and must be decoded before signing requests
STORAGE_AZURE_BLOBS_PARAMS = ('account', 'cGFzc3dvcmQ=')

# Loadbalancer
LB_BRIGHTBOX_PARAMS = ('user', 'key')
LB_ELB_PARAMS = ('access_id', 'secret', 'region')

# DNS
DNS_PARAMS_LINODE = ('user', 'key')
DNS_PARAMS_ZERIGO = ('email', 'api token')
DNS_PARAMS_RACKSPACE = ('user', 'key')
DNS_PARAMS_HOSTVIRTUAL = ('key',)
DNS_PARAMS_ROUTE53 = ('access_id', 'secret')
DNS_GANDI = ('user', )
