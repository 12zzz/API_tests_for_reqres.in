import logging
import pytest
import requests
from Basic import Basic
from variables import PositiveTestsVariables as Vars


BaseUrl = "https://reqres.in/api/register"
payload = {
    "email": f'{Vars.baseEmail}',
    "password": f'{Vars.basePassword}'
}
headers = Vars.baseHeaders
timeout = Vars.baseTimeout


class TestGetListUsers:
    @pytest.fixture(scope="class", autouse=True)
    def req(self):
        try:
            response = requests.request("POST", BaseUrl, headers=headers, data=payload, timeout=timeout)
            request = Basic(response)
            return request
        except:
            logging.exception("Failed to setup")
            pytest.skip("Failed to setup", allow_module_level=True)

    def test_status_code(self, req):
        code = 200
        assert req.is_status_code_right(code), "Status code " + \
                                               str(req.response.status_code) + " presented, instead of " + str(code)

    def test_response_time(self, req):
        sec = Vars.baseResponseTime
        assert req.is_response_are_in_time(sec), f"Response was more  then {sec} ms"

    def test_message_for_status_code(self, req):
        message = "OK"
        assert req.is_message_for_status_code_are_correct(message), \
            f"Response message was {req.response.reason}, not {message}"

    def test_is_header_present(self, req):
        header = 'Content-Type'
        header2 = 'Date'
        assert req.is_header_present(header), f"Header {header} is not presented"
        assert req.is_header_present(header2), f"Header {header2} is not presented"

    def test_is_header_have_current_value(self, req):
        header_key = 'Content-Type'
        header_value = 'application/json'
        assert req.is_header_have_current_value(header_key, header_value), \
            f"This '{header_value}' not in this '{header_key}'"

    def test_is_response_have_body(self, req):
        assert req.is_response_have_body(), "Response don't have body"

    def test_is_path_present_in_body(self, req):
        path1 = '$.id'
        assert req.is_path_present_in_body(path1), f"Path \'{path1}\' not presented in body"
        path2 = '$.token'
        assert req.is_path_present_in_body(path2), f"Path \'{path2}\' not presented in body"

