from ninja import ModelSchema, Schema
from django.contrib.auth.models import User
from .models import Materia, Assunto, Resumo, Perfil

class Cadastro_valid(Schema):
    username: str
    first_name: str
    password: str
class Login_valid(ModelSchema):
    class Meta:
        model = User
        fields = [
            'username', 'password'
        ]
class Materia_valid(ModelSchema):
    class Meta:
        model = Materia
        fields = [
            'titulo','id'
        ]

class Assunto_valid_get(Schema):
    id: int
    titulo: str
    materia_id: int
class Assunto_valid_post(Schema):
    titulo: str
    materia_id: int


class Resumo_valid(Schema):
    id:int
    titulo:str
    texto:str
    assunto_id: int
class Resumo_valid_post(Schema):
    titulo:str
    texto:str
    assunto_id: int
    
class Perfil_valid(ModelSchema):
    class Meta:
        model = Perfil
        fields = [
            'bio'
        ]

        
class Put_materia(Schema):
    id:int
    titulo:str
class Put_assunto(Schema):
    id:int
    titulo:str
class Put_resumo(Schema):
    id:int
    titulo:str
    texto:str