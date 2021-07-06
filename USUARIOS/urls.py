from django.urls import path
from .views import UserRegisterView

app_name = "USUARIOS"
urlpatterns = [
    path('registrarse/', UserRegisterView.as_view(), name="register"),
    # path('iniciar_sesion/', UserLoginView.as_view(), name="login"),
]