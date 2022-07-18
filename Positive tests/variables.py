
class PositiveTestsVariables:
    baseTimeout = 10
    basePageNumber = 1
    baseHeaders = {
        'Connection': 'keep-alive'
    }
    baseResponseTime = 1.0
    baseID = 2
    baseEmail = 'eve.holt@reqres.in'
    basePassword = 'basePassword'

class GetSingleUserMockVariables:
    mock_headers = {'Date': 'Mon, 18 Jul 2022 10:51:05 GMT', 'Content-Type': 'application/json; charset=utf-8',
                    'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'X-Powered-By': 'Express',
                    'Access-Control-Allow-Origin': '*', 'Etag': 'W/"118-pbdwwFo9SKNhD3Lx5iHJyngpq00"',
                    'Via': '1.1 vegur',
                    'Cache-Control': 'max-age=14400', 'CF-Cache-Status': 'HIT', 'Age': '280',
                    'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"',
                    'Report-To': '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=vGdxSflrU8CDtwBDEMoz4iFJ%2BBeXO1cxAVpM4yW8PE1nMa8AgBrvuDkoF0ckIFQKDtoe2EVR8TGsQ8OF3B4OnhJkSAf62HeJ14iGPZuPdsgRFVnisViGUMQQpg%3D%3D"}],"group":"cf-nel","max_age":604800}',
                    'NEL': '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}', 'Vary': 'Accept-Encoding',
                    'Server': 'cloudflare', 'CF-RAY': '72caa900ecd6be35-CPH', 'Content-Encoding': 'gzip'}
    reason = 'OK'
    status_code = 200
    text = {"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                     "avatar": "https://reqres.in/img/faces/2-image.jpg"},
            "support": {"url": "https://reqres.in/#support-heading",
                        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}
    json = {'data': {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver',
                     'avatar': 'https://reqres.in/img/faces/2-image.jpg'},
            'support': {'url': 'https://reqres.in/#support-heading',
                        'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'}}
    response_seconds = 0.144171
    headers_get = 'application/json; charset=utf-8'
    config = {'json.return_value': json, 'elapsed.total_seconds.return_value': response_seconds,
              'get.return_value': headers_get}
