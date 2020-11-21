from django.urls import path 
from . import views 
urlpatterns=[
    path('products',views.products,name='products'),
    path('<int:pro_id>',views.product,name='product'),
    path('search',views.search,name='search'),



 ]