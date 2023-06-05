from jwt import ImmatureSignatureError, DecodeError
from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from rest_framework.exceptions import
from customer.models import Customer
from utils.api_response import APIResponse

class JwtAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.Meta.get('HTTP_token')
        try:
            payload = jwt.decode(token, key=settings.SECRET_KEY)

        except(DecodeError, ImmatureSignatureError):
            raise ImmatureSignatureError("Invalid token")
        email = payload['email']
        customer = Customer.objects.filter(email=email).first()

        if not customer:
           raise ImmatureSignatureError("Invalid token")
        return APIResponse(code="200", message="认证成功", token=token)