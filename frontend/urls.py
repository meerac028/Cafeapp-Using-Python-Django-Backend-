from django.urls import path
from frontend import views

urlpatterns=[
    path('index_fro/',views.index_fro,name="index_fro"),
    path('about_fro/', views.about_fro, name="about_fro"),
    path('contact_fro/',views.contact_fro,name="contact_fro"),
    path('product_fro/<cat_name>/',views.product_fro,name="product_fro"),

]