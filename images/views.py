from rest_framework.generics import (
  ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from images.serializers import ImageSerializer
from .models import Image

class ImageListView(ListCreateAPIView):
    '''List view for /images INDEX CREATE'''
    queryset = Image.objects.all()
    serializer_class= ImageSerializer


class ImageDetailView(RetrieveUpdateDestroyAPIView):
    '''Detail view from /images/id SHOW UPDATE DELETE'''
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
