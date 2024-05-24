from django.urls import path
from . import views

urlpatterns = [
    path('vacations/', views.vacations_list, name="vacations_list"),
    
    path('categories/', views.categories_list, name="categories_list"),
    path('categories/<int:pk>/', views.category_detail, name="category_detail"),

]