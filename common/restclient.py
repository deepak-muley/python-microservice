import logging
import requests

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

# https://2.python-requests.org/en/master/


class RESTClient(object):
    def __init__(self, host, port, timeout=5):
        #self.session = requests.Session()
        self.host = host
        self.port = port
        self.timeout = timeout

        if self.port == 443:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

    def _url(self, path):
        return '{}://{}:{}'.format(self.protocol, self.host, self.port) + path

    def get(self, path, headers={}):
        url = self._url(path)
        log.info("[GET] {}".format(url))
        #resp = self.session.get(url, headers=headers, timeout=self.timeout)
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()

    def post(self, path, body, headers={}):
        url = self._url(path)
        log.info("[POST] {}.".format(url))
        # resp = self.session.post(
        #     url, json=body, headers=headers, timeout=self.timeout)
        resp = requests.post(
            url, json=body)
        resp.raise_for_status()
        return resp.json()
