import jwt
from django.conf import settings
from ninja.errors import HttpError
from django.contrib.auth.models import User

chave = settings.CHAVE_KEMU

def usuario_do_token(auth: str) -> User:
    if not auth:
        raise HttpError(401, 'Token não fornecido')

    try:
        token = auth.split(" ")[1]
    except IndexError:
        raise HttpError(401, 'Erro no cabeçalho da requisição')

    try:
        payload = jwt.decode(token, chave, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise HttpError(401, 'Token expirado, faça login novamente')
    except jwt.InvalidTokenError:
        raise HttpError(401, 'Token inválido')
    except Exception as e:
        raise HttpError(500, f'Erro no servidor: {str(e)}')

    try:
        user = User.objects.get(id=payload['id'])
    except User.DoesNotExist:
        raise HttpError(404, 'Usuário não encontrado')

    return user
