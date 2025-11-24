from ninja import Router
from django.contrib.auth.models import User
import jwt
from django.conf import settings
from ninja.errors import HttpError
from typing import List
from .schemas import Materia_valid, Assunto_valid_get, Resumo_valid, Perfil_valid
from .models import Materia,Assunto,Resumo,Perfil
from .get_user import usuario_do_token


chave = settings.CHAVE_KEMU

rotas_home = Router()

@rotas_home.get('materia/', response=List[Materia_valid])
def ver_materia(request):
    verificacao = usuario_do_token(request.headers.get('Authorization'))
    materia = Materia.objects.filter(usuario = verificacao)
    return materia
    

@rotas_home.get('assunto/', response=List[Assunto_valid_get])
def ver_assunto(request):
    verificacao = usuario_do_token(request.headers.get('Authorization'))
    assunto = Assunto.objects.filter(materia__usuario = verificacao)
    return assunto
    

@rotas_home.get('resumo/', response=List[Resumo_valid])
def ver_resumo(request):
    verificacao = usuario_do_token(request.headers.get('Authorization'))
    resumo = Resumo.objects.filter(assunto__materia__usuario = verificacao)
    
    return resumo