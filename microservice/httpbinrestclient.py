import os
import logging

from common.restclient import RESTClient

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


class HTTPBINRESTClient(RESTClient):
    def __init__(self):
        super(HTTPBINRESTClient, self).__init__("httpbin.org", 80)

    def get_ip(self):
        try:
            resp = self.get("/ip")
            return resp['origin']
        except Exception as e:
            print("API Failed: {}".format(e))
        return None
