from django.test import TestCase

from CalorieCounter.accounts.models import CustomUser


class LoginTest(TestCase):

    def setUp(self):
        self.data = {
            'username': 'user',
            'password': '1234hello',
            'birthday': '1999-11-23',
            'gender': 'Male',
            'height': '189',
            'weight': 92,
        }
        CustomUser.objects.create_user(**self.data)

    def test_login__valid_data__expect_correct_result(self):
        self.credentials = {
            'username': 'user',
            'password': '1234hello',
        }

        response = self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        self.assertTrue(response)

    def test_login__invalid_data__expect_error(self):
        self.credentials = {
            'username': 'user',
            'password': '1234',
        }

        response = self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        self.assertFalse(response)

