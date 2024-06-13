from django.urls import path
from . import views #make sure you have views imported

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'), #ensure this line exists
]