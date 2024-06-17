from django.urls import path, include
from . import views
from . import views_comments
from . import views_likes

urlpatterns = [
    path('vacations/', views.vacations_list, name="vacations_list"),
    path('vacations/<int:pk>/', views.vacation_detail, name="vacation_detail"),
    
    
    path('categories/', views.categories_list, name="categories_list"),
    path('categories/<int:pk>/', views.category_detail, name="category_detail"),
    
    path('vacations/<int:vacation_id>/comments/', views_comments.all_comments_for_vacation, name="comments_list"),
    path('vacations/<int:vacation_id>/comments/<int:comment_id>', views_comments.comment_detail, name="comment_detail"),
    
    path('vacations/<int:vacation_id>/likes/',views_likes.get_likes , name="likes_list"),
    path('vacations/<int:vacation_id>/like',views_likes.like_vacation , name="like_vacation"),
    path('vacations/<int:vacation_id>/dislike',views_likes.dislike_vacation , name="dislike_vacation"),
    
    path('auth/', include('rest_framework.urls')),

]