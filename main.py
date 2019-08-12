import logging

from microservice.httpbinrestclient import HTTPBINRESTClient

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


def main():
    httpbinclient = HTTPBINRESTClient()
    print("httpbin.org/ip returned origin as {}".format(httpbinclient.get_ip()))


if __name__ == "__main__":
    main()
