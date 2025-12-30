from django.urls import path
from .views import *


urlpatterns = [
    path("create_category/", create_category, name="create_category"),
    path("create_post/", create_post, name="create_post"),
    path("update_post/<str:id>/", post_update, name="update_post"),
    path("delete_post/<int:id>/", delete_post, name="delete_post"),
    path("user_post/", user_post, name="user_post"),
    path("read_post/", read_post, name="read_post"),
    path("search/", search, name="search"),
    path("comment/<int:post_id>/", comment, name="comment"),
    path("comment_edit/<int:id>/", comment_edit, name="comment_edit"),
    path("comment_read/<str:post_id>/", comment_read, name="comment_read"),
    path("comment_delete/<int:id>/", comment_delete, name="comment_delete")
]