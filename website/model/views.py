from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import BSIArticle
from .serializer import BSIArticleSerializer

# Lists all BSI catalog
# BSIArticle/
class BSIArticleList(APIView):
    def get(self, request):
        bsi_arts = BSIArticle.objects.all()
        serializer = BSIArticleSerializer(bsi_arts, many=True)