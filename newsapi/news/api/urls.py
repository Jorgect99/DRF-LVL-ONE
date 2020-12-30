from django.urls import path
from news.api.views import article_list_create_api_view, article_detail_api_view

urlpatterns = [
    path("articles/", article_list_create_api_view, name="articles-list"),
    path("articles/<int:pk>/", article_detail_api_view, name="articles-detail")
]
