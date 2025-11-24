from ninja import Router
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from ninja.errors import HttpError
from typing import List
from .schemas import Materia_valid, Assunto_valid_post, Resumo_valid_post, Perfil_valid
from .models import Materia,Assunto,Resumo,Perfil
from .get_user import usuario_do_token

rotas_create = Router()

chave = settings.CHAVE_KEMU

@rotas_create.post('create_materia/')
def do_materia(request, dados: Materia_valid):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    
    save = Materia(
        usuario = token_user,
        titulo = dados.titulo
    )
    save.save()
    return {'resposta': "materia criada"}
    


@rotas_create.post('create_assunto/')
def do_assunto(request, dados: Assunto_valid_post):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        materia = Materia.objects.get(id = dados.materia_id, usuario  = token_user)
    except Materia.DoesNotExist:
        raise HttpError(404, 'materia nao existe')
    
    save = Assunto(
        materia = materia,
        titulo = dados.titulo
    )
    save.save()
    return {'resposta': "assunto criada"}
    
@rotas_create.post('create_resumo/')
def do_resumo(request, dados: Resumo_valid_post):
    token_user = usuario_do_token(request.headers.get('Authorization'))

    try:
        assunto_no_banco = Assunto.objects.get(id = dados.assunto_id,materia__usuario= token_user )
    except Assunto.DoesNotExist:
        raise HttpError(404, 'Assunto nao encontrado')
    
    save = Resumo.objects.create(
        assunto = assunto_no_banco,
        titulo = dados.titulo,
        texto = dados.texto,
    )
    return {'resposta': 'resumo criado'}

