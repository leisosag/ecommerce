from django.urls import path
from . import views

app_name = "JAGUARETE"
urlpatterns = [
    path('', views.index, name="index"),
    path('acercade', views.about, name="about"),
    path('contacto', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('registrar', views.register, name="register"),
    path('<int:product_id>', views.product, name="product"),
    path('product_add', views.product_add, name="product_add"),
    path('<int:product_id>/editar_producto', views.product_edit, name="product_edit"),
]