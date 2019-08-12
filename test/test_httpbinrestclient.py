from microservice.httpbinrestclient import HTTPBINRESTClient
import unittest
from unittest import mock
from requests import Session
from unittest.mock import patch
from requests.exceptions import HTTPError


class mock_get():
    def __init__(self, url):
        self.ok = True
        self.raise_for_status = mock.Mock()

    def json(self):
        return {'origin': '1.2.3.4'}


class mock_get_invalid_type():
    def __init__(self, url):
        self.ok = True
        self.raise_for_status = mock.Mock()

    def json(self):
        return {'origin': 100}


class TestHTTPBINRESTClient(unittest.TestCase):
    def setUp(self):
        self.ip_grabber = HTTPBINRESTClient()

    def test_ip_grabber(self):
        ip = self.ip_grabber.get_ip()
        print("ip: {}".format(ip))
        self.assertIsInstance(ip, str, "IP should be a string")

    @mock.patch('common.restclient.requests.get', side_effect=mock_get)
    def test_ip_grabber_mock(self, mock_get):
        ip = self.ip_grabber.get_ip()
        print("ip: {}".format(ip))
        self.assertIsInstance(ip, str, "IP should be a string")

    @mock.patch('common.restclient.requests.get', side_effect=mock_get_invalid_type)
    def test_ip_grabber_mock_invalid_type(self, mock_get_invalid_type):
        ip = self.ip_grabber.get_ip()
        print("ip: {}".format(ip))
        self.assertIsInstance(ip, str, "IP should be a string")

    # https: // gist.github.com/evansde77/45467f5a7af84d2a2d34f3fcb357449c

    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        since we typically test a bunch of different
        requests calls for a service, we are going to do
        a lot of mock responses, so its usually a good idea
        to have a helper function that builds these things
        """
        mock_resp = mock.Mock()
        # mock raise_for_status call w/optional error
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status
        # set status code and content
        mock_resp.status_code = status
        mock_resp.content = content
        # add json data if provided
        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @mock.patch('common.restclient.requests.get')
    def test_get_query(self, mock_resp_get):
        mock_resp = self._mock_response(content="{'origin': 200}")
        mock_resp_get.return_value = mock_resp

        ip = self.ip_grabber.get_ip()
        print("ip: {}".format(ip))

        self.assertEqual(ip, "{'origin': 200}")
        self.assertTrue(mock_resp.raise_for_status.called)


if __name__ == '__main__':
    unittest.main()
