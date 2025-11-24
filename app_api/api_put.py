from ninja import Router
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from ninja.errors import HttpError
from typing import List
from .schemas import Put_assunto,Put_materia,Put_resumo
from .models import Materia,Assunto,Resumo,Perfil
from .get_user import usuario_do_token

rotas_put = Router()



@rotas_put.patch('put_materia/{id}')
def put_materia(request, dados: Put_materia):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Materia.objects.get(id = dados.id,usuario = token_user)
    except Materia.DoesNotExist:
        raise HttpError(404, 'materia nao encontrada')
    
    busca.titulo = dados.titulo
    busca.save()
    return {'resposta': "materia atualizada"}
@rotas_put.patch('put_assunto/{id}')
def put_assunto(request, dados: Put_assunto):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Assunto.objects.get(id = dados.id,materia__usuario = token_user)
    except Assunto.DoesNotExist:
        raise HttpError(404, 'assunto nao encontrado')
    
    busca.titulo = dados.titulo
    busca.save()
    return {'resposta': "assunto atualizado"}
@rotas_put.patch('put_resumo/{id}')
def put_resumo(request,dados: Put_resumo):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Resumo.objects.get(id = dados.id,assunto__materia__usuario = token_user)
    except Resumo.DoesNotExist:
        raise HttpError(404, 'resumo nao encontrada')
    
    busca.titulo = dados.titulo
    busca.texto = dados.texto
    busca.save()
    return {'resposta': "resumo atualizado"}