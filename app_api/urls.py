from django.urls import path
from ninja import NinjaAPI
from .api_auth import rotas_auth
from .api_home import rotas_home
from .api_create import rotas_create
from .api_delete import rotas_delete
from .api_put import rotas_put

nucleo = NinjaAPI()
nucleo.add_router('auth/', rotas_auth)
nucleo.add_router('home/', rotas_home)
nucleo.add_router('create/', rotas_create)
nucleo.add_router('delete/', rotas_delete)
nucleo.add_router('put/', rotas_put)

urlpatterns = [
    path('api/', nucleo.urls)
]

