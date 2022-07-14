from requests import Response
from jsonpath_ng import parse


class Basic:
    response: Response

    def __init__(self, response: Response):
        self.response = response

    # Проверка кода ответа
    def is_status_code_right(self, code: int):
        return self.response.status_code == code

    # Проверка времени ответа от сервера
    def is_response_are_in_time(self, sec: float):
        return self.response.elapsed.total_seconds() < sec

    # Проверка сообщения/текста статус кода
    def is_message_for_status_code_are_correct(self, message: str):
        return self.response.reason == message

    # Проверка наличия определенного хедера в ответе
    def is_header_present(self, header: str):
        return header in self.response.headers

    # Проверка значения определенного хедера в ответе
    def is_header_have_current_value(self, header_key: str, header_value: str):
        return header_value in self.response.headers.get(header_key)

    # Проверка наличия тела в ответе
    def is_response_have_body(self):
        return any(self.response.text)

    # Проверка наличия jsonpath в ответе
    def is_path_present_in_body(self, path):
        path_expression = parse(path)
        return len(path_expression.find(self.response.json())) > 0

    # Проверка наличия значения у jsonpath в ответе
    def is_key_and_value_in_body(self, path, value):
        path_expression = parse(path)
        try:
            searching_value = path_expression.find(self.response.json())[0].value
        except IndexError as e:
            return False
        else:
            return searching_value == value
