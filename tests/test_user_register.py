import requests
import pytest
from lib.base_case import BaseCase


class TestUserRegistration(BaseCase):
    null_var = None
    data = [
        (
            null_var,
            'august_salimov',
            'august',
            'salimov',
            'augustsalimov@example.com'
        ),
        (
            '123',
            null_var,
            'august',
            'salimov',
            'augustsalimov@example.com'
        ),
        (
            '123',
            'august_salimov',
            null_var,
            'salimov',
            'augustsalimov@example.com'
        ),
        (
            '123',
            'august_salimov',
            'august',
            null_var,
            'augustsalimov@example.com'
        ),
        (
            '123',
            'august_salimov',
            'august',
            'salimov',
            null_var
        )
    ]

    def setup(self):
        self.url = 'https://playground.learnqa.ru/api/user/'

    def test_user_with_invalid_email(self):
        data = {
            'password': '123',
            'username': 'august_salimov',
            'firstName': 'august',
            'lastName': 'salimov',
            'email': 'augustsalimovexample.com'
        }
        response = requests.post(self.url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == "Invalid email format", f"Unexpected"

    @pytest.mark.parametrize('password, username, firstName, lastName, email', data)
    def test_user_wo_field(self, password, username, firstName, lastName, email):
        data = {
            'password': password,
            'username': username,
            'firstName': firstName,
            'lastName': lastName,
            'email': email
        }
        response = requests.post(self.url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"

    def test_user_with_short_username(self):
        data = {
            'password': '123',
            'username': 'a',
            'firstName': 'august',
            'lastName': 'salimov',
            'email': 'augustsalimove@example.com'
        }
        response = requests.post(self.url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == "The value of 'username' field is too short", f"Unexpected"

    def test_user_with_long_username(self):
        data = {
            'password': '123',
            'username': 'pbepnqtrhloraljtdgrpxuypcbxvnlwppoxpbbuhnzzviquzvsnwimvnpnkujuyvchagcfvbjndwyowubmfzwpa'
                        'vlbjrqjyvqjlvqledjaimaqnvyjhccnbgmdcowrubdutljtfnscccnnhnuqhycrvswtsbratjrqpmtufygytjaq'
                        'iplwckrgpffnxnqlpynbhojufciezcnhvukwntzkfhhcecdniodtemrnedsihnkycnsaklutkrrlzrwgh',
            'firstName': 'august',
            'lastName': 'salimov',
            'email': 'augustsalimove@example.com'
        }
        response = requests.post(self.url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == "The value of 'username' field is too long", f"Unexpected"
