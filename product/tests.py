from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from user.models import Account
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from .models import Product

# Create your tests here.


class ProductViewTests(APITestCase):
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

    def create_product(self):
        seller = Account.objects.create_user(**self.seller)
        token = Token.objects.get_or_create(user=seller)[0]

        print("+" * 100)
        print(token)

        response = self.client.post("/api/products/", self.product, format="json")

        self.assertEqual(response.status_code, 400)
