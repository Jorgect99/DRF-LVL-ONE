from django.urls import path
from news.api.views import ArticleListCreateAPIView, ArticleDetailAPIView, JournalistListCreateAPIView

urlpatterns = [
    path("Articles/", ArticleListCreateAPIView.as_view(), name="Articles-list"),
    path("Articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="Articles-detail"),
    path("journalist/", JournalistListCreateAPIView.as_view(), name="journalist-list"),
]
