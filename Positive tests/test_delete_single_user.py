import logging
import pytest
import requests
from Basic import Basic
from variables import PositiveTestsVariables as Vars

BaseUrl = f"https://reqres.in/api/users/{Vars.baseID}"
payload = {}
headers = Vars.baseHeaders
timeout = Vars.baseTimeout


class TestGetListUsers:
    @pytest.fixture(scope="class", autouse=True)
    def req(self):
        try:
            response = requests.request("DELETE", BaseUrl, headers=headers, data=payload, timeout=timeout)
            request = Basic(response)
            return request
        except:
            logging.exception("Failed to setup")
            pytest.skip("Failed to setup", allow_module_level=True)

    def test_status_code(self, req):
        code = 204
        assert req.is_status_code_right(code), "Status code " + \
                                               str(req.response.status_code) + " presented, instead of " + str(code)

    def test_response_time(self, req):
        sec = Vars.baseResponseTime
        assert req.is_response_are_in_time(sec), f"Response was more  then {sec} ms"

    def test_message_for_status_code(self, req):
        message = "No Content"
        assert req.is_message_for_status_code_are_correct(message), \
            f"Response message was {req.response.reason}, not {message}"

    def test_is_header_present(self, req):
        header = 'Connection'
        assert req.is_header_present(header), f"Header {header} is not presented"

    def test_is_header_have_current_value(self, req):
        header_key = 'Connection'
        header_value = 'keep-alive'
        assert req.is_header_have_current_value(header_key, header_value), \
            f"This '{header_value}' not in this '{header_key}'"

    def test_is_response_havent_body(self, req):
        assert not req.is_response_have_body(), "Response have body"

