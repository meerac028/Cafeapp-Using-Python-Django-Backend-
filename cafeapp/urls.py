from django.urls import path
from cafeapp import views

urlpatterns=[
    path('cafe/',views.cafe,name="cafe"),
    path('add_category/',views.add_category,name="add_category"),
    path('category_save/', views. category_save, name="category_save"),
    path('dis_category/', views.dis_category, name="dis_category"),
    path('edit_cat/<int:d_id>/', views.edit_cat, name="edit_cat"),
    path('update_cat/<int:d_id>/', views.update_cat, name="update_cat"),
    path('delete_cat/<int:d_id>/', views.delete_cat, name="delete_cat"),
    path('add_product/', views.add_product, name="add_product"),
    path('product_save/', views.product_save, name="product_save"),
    path('dis_product/', views.dis_product, name="dis_product"),
    path('edit_product/<int:d_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:d_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:d_id>/', views.delete_product, name="delete_product"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('login_save/', views.login_save, name="login_save"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
]