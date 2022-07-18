from mock import patch


class MyMock:
    def __init__(self, headers='', reason='', status_code=0, text={}, json={}, seconds=0.0, headers_get='', config={}):
        self.headers = headers
        self.reason = reason
        self.status_code = status_code
        self.text = text
        self.json = json
        self.seconds = seconds
        self.headers_get = headers_get
        self.config = config

    def setup(self):
        patcher = patch('requests.Response', headers=self.headers, reason=self.reason, status_code=self.status_code, text=self.text, **self.config)
        my_mock = patcher.start()
        return my_mock


