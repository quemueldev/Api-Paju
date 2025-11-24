from ninja import Router
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from ninja.errors import HttpError
from typing import List
from .schemas import Materia_valid, Resumo_valid, Perfil_valid
from .models import Materia,Assunto,Resumo,Perfil
from .get_user import usuario_do_token

rotas_delete = Router()



@rotas_delete.delete('delete_materia/{id}')
def dell_materia(request, id:int):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Materia.objects.get(id = id,usuario = token_user)
    except Materia.DoesNotExist:
        raise HttpError(404, 'materia nao encontrada')
    
    busca.delete()
    return {'resposta': "materia deletada"}
@rotas_delete.delete('delete_assunto/{id}')
def dell_assunto(request, id:int):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Assunto.objects.get(id = id,materia__usuario = token_user)
    except Assunto.DoesNotExist:
        raise HttpError(404, 'assunto nao encontrado')
    
    busca.delete()
    return {'resposta': "assunto deletada"}
@rotas_delete.delete('delete_resumo/{id}')
def dell_resumo(request, id: int):
    token_user = usuario_do_token(request.headers.get('Authorization'))
    try:
        busca = Resumo.objects.get(id = id,assunto__materia__usuario = token_user)
    except Resumo.DoesNotExist:
        raise HttpError(404, 'resumo nao encontrado')
    
    busca.delete()
    return {'resposta': "resumo deletada"}