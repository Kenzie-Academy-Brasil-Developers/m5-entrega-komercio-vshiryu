from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from user.models import Account
from rest_framework.views import status
from rest_framework.authtoken.models import Token

# Create your tests here.


class UserViewsTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.seller = {
            "username": "ale",
            "password": "abcd",
            "first_name": "alexandre",
            "last_name": "alves",
            "is_seller": True,
        }
        cls.wrong_seller = {
            "username": "",
            "password": "",
            "first_name": "",
            "is_seller": True,
        }
        cls.buyer = {
            "username": "barney",
            "password": "abcd",
            "first_name": "barney",
            "last_name": "hagio",
            "is_seller": False,
        }
        cls.wrong_buyer = {
            "username": "",
            "password": "",
            "last_name": "hagio",
            "is_seller": False,
        }
        cls.seller_login = {
            "username": "ale",
            "password": "abcd",
        }
        cls.product = {
            "description": "Smartband XYZ 3.0",
            "price": 100.99,
            "quantity": 15,
        }

    def test_creating_seller(self):
        response = self.client.post("/api/accounts/", self.seller, format="json")

        self.assertEqual(response.status_code, 201)

    def test_creating_buyer(self):
        response = self.client.post("/api/accounts/", self.buyer, format="json")

        self.assertEqual(response.status_code, 201)

    def test_creating_wrong_seller(self):
        response = self.client.post("/api/accounts/", self.wrong_seller, format="json")

        self.assertEqual(response.status_code, 400)

    def test_creating_wrong_buyer(self):
        response = self.client.post("/api/accounts/", self.wrong_buyer, format="json")

        self.assertEqual(response.status_code, 400)

    def test_login(self):
        Account.objects.create_user(**self.seller)

        response = self.client.post("/api/login/", self.seller_login, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)

    def test_login_wrong(self):
        response = self.client.post(
            "/api/login/", {"username": "abc", "password": "132"}, format="json"
        )

        self.assertEqual(response.status_code, 401)

    def test_list(self):
        Account.objects.create_user(**self.seller)

        response = self.client.get("/api/accounts/")
        # print(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_list(self):
        Account.objects.create_user(**self.seller)

        response = self.client.get("/api/accounts/")
        # print(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
