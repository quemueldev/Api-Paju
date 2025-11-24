from ninja import Router
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from datetime import timedelta, datetime
from django.utils import timezone
from ninja.errors import HttpError
from .schemas import Cadastro_valid, Login_valid
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

rotas_auth = Router()
chave = settings.CHAVE_KEMU

@rotas_auth.post('cadastro/')
def cadastro(request, dados: Cadastro_valid):
    print(dados.dict())
    try:
        validate_email(dados.username)
        email_valido = True
    except ValidationError:
        email_valido = False
    if email_valido:
        user = User.objects.filter(username=dados.username).exists()
        if not user:
            try:
                User.objects.create_user(
                    username= dados.username,
                    first_name=dados.first_name,
                    password=dados.password
                )
                return {"resposta": "usuario cadastrado"}
            except Exception as e:
                raise HttpError(500, f'erro ao criar usuario {e}')
        return {"resposta": "usuario ja existente"}
    return {'resposta': 'email invalido'}

@rotas_auth.post('login/')
def login(request, dados: Login_valid):
    print(dados.dict())
    try:
        validate_email(dados.username)
        email_valido = True
    except ValidationError:
        email_valido = False
    if email_valido:
        user = authenticate(username = dados.username, password = dados.password)
        if user:
            payload = {
                'id': user.id,
                "email": user.username,
                "nome": user.first_name,
                "exp": timezone.now() + timedelta(days=30)
            }
            token = jwt.encode(payload, chave, algorithm='HS256')
            return {'resposta': token, "status": "sucesso"}
        else:
            return {"resposta": "senha invalida"}
    else:
        return {'resposta': 'email invalido'}