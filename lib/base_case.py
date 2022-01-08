from requests import Response

class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find cookie with name {headers_name} in the last response"
        return response.headers[headers_name]

