from django.urls import path
from .views import delete_post, home , post , post_detail , add_comment, add_post , delete_post, user_logout , register , add_like

urlpatterns = [
    path('', post , name='post'),
    path('post/', post , name='post'),
    path('detail/<int:id>', post_detail , name='detail'),
    path('add/<int:id>', add_comment , name='add'),
    path('addpost/', add_post , name='addpost'),
    path('delete/<int:id> ', delete_post , name='delete'),
    path('logout/', user_logout , name='logout'),
    path('register/', register , name='register'),
    path('addlike/<int:id>', add_like , name='addlike'),
    
]