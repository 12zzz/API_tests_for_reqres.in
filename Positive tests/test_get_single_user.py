import logging
import pytest
from Basic import Basic
from variables import PositiveTestsVariables as Vars
from variables import GetSingleUserMockVariables as MV
from MyMock import MyMock


BaseUrl = f"https://reqres.in/api/users/{Vars.baseID}"
payload = {}
headers = Vars.baseHeaders
timeout = Vars.baseTimeout

class TestGetListUsers:
    @pytest.fixture(autouse=True)
    def req(self):
        try:
            # Замена настоящего реквеста на мок
            my_mock = MyMock(MV.mock_headers, MV.reason, MV.status_code, MV.text, MV.json, MV.response_seconds, MV.headers_get, MV.config)
            #response = requests.request("GET", BaseUrl, headers=headers, data=payload, timeout=timeout)
            mock_response = my_mock.setup()
            request = Basic(mock_response)
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
        assert req.is_header_present(header), f"Header {header} is not presented"

    def test_is_header_have_current_value(self, req):
        header_key = 'Content-Type'
        header_value = 'application/json'
        assert req.is_header_have_current_value(header_key, header_value), \
            f"This '{header_value}' not in this '{header_key}'"

    def test_is_response_have_body(self, req):
        assert req.is_response_have_body(), "Response don't have body"

    def test_is_path_present_in_body(self, req):
        path = '$.data'
        assert req.is_path_present_in_body(path), f"Path \'{path}\' not presented in body"

    def test_is_key_and_value_in_body(self, req):
        path = '$.data.id'
        value = Vars.baseID
        assert req.is_key_and_value_in_body(path, value), f"Key|value pair not found"
