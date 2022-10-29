from django.shortcuts import render
from rest_framework import generics

from user.models import Account
from user.serializer import AccountSerializer, LoginSerializer
from rest_framework.views import Response, Request, status, APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class AccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        print(serializer.validated_data)

        if not user:
            return Response(
                {"detail": "Invalid username or password"}, status.HTTP_401_UNAUTHORIZED
            )

        token = Token.objects.get_or_create(user=user)[0]

        return Response({"token": token.key, "user_id": user.id}, status.HTTP_200_OK)


class AccountsNewest(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        accounts = self.kwargs["num"]
        ordered_accounts = self.queryset.order_by("-date_joined")[0:accounts]
        return ordered_accounts
