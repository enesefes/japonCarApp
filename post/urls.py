from django.urls import path
from post.views import post_index, post_detail, post_create,post_update, post_delete

app_name= 'post'
urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    path('<slug:postTitleSlug>/', post_detail, name='detail'),
    path('<slug:postTitleSlug>/update/', post_update, name='update'),
    path('<slug:postTitleSlug>/delete/', post_delete, name='delete'),
]
