from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import jwt
import datetime
from rest_framework.permissions import AllowAny


# "Banco de dados" em memória
USERS_DB = {}

class RegisterView(APIView):
    permission_classes = [AllowAny]  # Permite acesso não autenticado
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username e password são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        if username in USERS_DB:
            return Response({'message': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

        # Hash da senha
        hashed_password = make_password(password)
        USERS_DB[username] = hashed_password

        return Response({'message': f'Usuário {username} registrado com sucesso'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'message': 'Username e password são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = USERS_DB.get(username)
        if not hashed_password or not check_password(password, hashed_password):
            return Response({'message': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Gerar JWT manualmente
        payload = {
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return Response({'access': token})


class ProtectedView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return Response({'message': 'Token ausente ou mal formatado'}, status=status.HTTP_401_UNAUTHORIZED)

        token = auth_header.split(" ")[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Token expirado'}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({'message': 'Token inválido'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'message': f"Bem-vindo, {payload['username']}! Acesso autorizado."})