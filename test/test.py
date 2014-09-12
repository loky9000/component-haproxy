import os

import requests

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values

@environment({
    "default": {},
    "AmazonEC2_CentOS_64": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-bf5021d6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    },
    "AmazonEC2_CentOS_53": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-beda31d7"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    },
    "AmazonEC2_Ubuntu_1204": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-967edcff"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    },
    "AmazonEC2_Ubuntu_1004": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-9f3906f6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    }
})
class HAProxyComponentTestCase(BaseComponentTestCase):
    name = "Load Balancer"
    meta = "https://raw.githubusercontent.com/qubell-bazaar/component-haproxy/master/meta.yml"    
    apps = [{
        "name": name,
    }]


    @instance(byApplication=name)
    @values({"lb-statistics-url": "url", "stats-user": "user", "stats-pass": "password"})
    def test_admin_page(self, instance, url, user, password):
        resp = requests.get(url, auth=(user, password), verify=False)

        assert resp.status_code == 200
