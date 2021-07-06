from django.urls import path
from . import views

app_name = "JAGUARETE"
urlpatterns = [
    path('', views.index, name="index"),
    path('acercade', views.about, name="about"),
    path('contacto', views.contact, name="contact"),
    path('categorias', views.categories, name="categories"),
    path('<int:product_id>', views.product, name="product"),
    path('product_add', views.product_add, name="product_add"),
    path('<int:product_id>/editar_producto', views.product_edit, name="product_edit"),
    path('<int:product_id>/eliminar_producto', views.product_delete, name="product_delete"),
    path('buscar', views.search_results, name="search_results"),
    path('buscar_categoria', views.search_category, name="search_category"),
    path('carrito', views.cart, name="cart"),
]