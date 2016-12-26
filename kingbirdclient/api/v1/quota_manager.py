# Copyright (c) 2016 Ericsson AB.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from kingbirdclient.api import base


class Quota(base.Resource):
    resource_name = 'os-quota-sets'


class quota_manager(base.ResourceManager):
    resource_class = Quota

    def list_defaults(self):
        tenant = self.http_client.project_id
        url = '/%s/os-quota-sets/defaults' % tenant
        return self._list(url)

    def global_limits(self, target_tenant_id=None):
        tenant = self.http_client.project_id
        if not target_tenant_id:
            target_tenant_id = tenant
        url = '/%s/os-quota-sets/%s' % (tenant, target_tenant_id)
        return self._list(url)
