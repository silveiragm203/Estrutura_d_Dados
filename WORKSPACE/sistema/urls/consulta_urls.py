from django.urls import path
from sistema.views import consulta_view

urlpatterns = [
    path('consulta/', consulta_view), # vollmed.com/consulta
    path('consulta/novo/'), # vollmed.com/consulta/novo/
    path('consulta/perfil/<int:consulta_id>'), # vollmed.com/consulta/<int:consulta_id>/
    path('consulta/listagem'), # vollmed.com/consulta/listagem
]
