import ipdb
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView, Response, status

from .models import Post
from .serializers import UploadSerializer


class FormCNAB(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        uploaded_file = Post.objects.all()
        serializer = UploadSerializer(uploaded_file, many=True)
        return Response({'serializer': serializer, 'uploaded_file': uploaded_file})

    def post(self, request):
        uploaded_file = request.FILES
        serializer = UploadSerializer(data=uploaded_file)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer.is_valid(raise_exception=True)

class DocumentationList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'doc.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'file_uploaded': queryset})
