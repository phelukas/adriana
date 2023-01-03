from django.urls import include, path, re_path
from django.contrib import admin
from core.views import UserView, SolicitacaoView

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),

    # urls about users
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),

    # urls about users
    path('solicitacoes/', SolicitacaoView.as_view()),
    path('solicitacoes/<int:pk>', SolicitacaoView.as_view()),

]
