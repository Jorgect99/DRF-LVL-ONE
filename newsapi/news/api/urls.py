from django.urls import path
from news.api.views import ArticleListCreateAPIView, ArticleDetailAPIView

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="articles-list"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="articles-detail")
]
