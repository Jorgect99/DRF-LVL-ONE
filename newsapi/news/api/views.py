from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from news.models import Article, Journalist
from news.api.serializers import ArticleSerializer, JournalistSerializer

class ArticleListCreateAPIView(APIView):

    #serializer_class = ArticleSerializer

    def get(self, request):
        Articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(Articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):

    def get_object(self, pk):
        Article = get_object_or_404(Article, pk=pk)
        return Article
    
    def get(self, request, pk):
        Article = self.get_object(pk)
        serializer = ArticleSerializer(Article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        Article = self.get_object(pk)
        serializer = ArticleSerializer(Article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        Article = self.get_object(pk)
        Article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalistListCreateAPIView(APIView):

    def get(self, request):
        journalist = Journalist.objects.all()
        serializer = JournalistSerializer(journalist, many=True, context={"request":request})
        return Response(serializer.data)

    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
# def Article_list_create_api_view(request):

#     if request.method == "GET":
#         Articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(Articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET", "PUT", "DELETE"])
# def Article_detail_api_view(request, pk):
#     try:
#         Article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response({"error":{
#                             "code": 404,
#                             "message":"Article not found!"
#                         }}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(Article)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = ArticleSerializer(Article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         Article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)