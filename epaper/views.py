from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import EPaper
from .serializers import EPaperSerializer


class EPaperView(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = EPaper.objects.all()
    serializer_class = EPaperSerializer
    
    def perform_create(self, serializer):
        author = get_object_or_404(EPaper, id=self.request.data.get('id'))
        return serializer.save(author=author)
    
    # def put(self, request, pk):
    #     saved_article = get_object_or_404(Article.objects.all(), pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
    
    # def delete(self, request, pk):
    #     # Get object with this pk
    #     article = get_object_or_404(Article.objects.all(), pk=pk)
    #     article.delete()
    #     return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)

