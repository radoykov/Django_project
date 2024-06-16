from django.urls import path
from . import views;
from . import views_comments;

urlpatterns = [
    path('vacations/', views.vacations_list, name="vacations_list"),
    path('vacations/<int:pk>/', views.vacation_detail, name="vacation_detail"),
    
    
    path('categories/', views.categories_list, name="categories_list"),
    path('categories/<int:pk>/', views.category_detail, name="category_detail"),
    
    path('vacations/<int:vacation_id>/comments/', views_comments.all_comments_for_vacation, name="comments_list"),
    path('vacations/<int:vacation_id>/comments/<int:comment_id>', views_comments.comment_detail, name="comment_detail"),

]