
from django.urls import path
from . import views
# URLs para o aplicativo de autenticação
# Essas URLs serão acessíveis em /api/register/, /api/login/ e /api/protected/
# Certifique-se de que o prefixo 'api/' esteja configurado corretamente no arquivo principal

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('protected/', views.ProtectedView.as_view()),
]
