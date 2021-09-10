from rest_framework import status
from rest_framework.generics import (
  ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from images.serializers import ImageSerializer, NoteSerializer
from .models import Image, Note

class ImageListView(ListCreateAPIView):
    '''List view for /images INDEX CREATE'''
    queryset = Image.objects.all()
    serializer_class= ImageSerializer


class ImageDetailView(RetrieveUpdateDestroyAPIView):
    '''Detail view from /images/id SHOW UPDATE DELETE'''
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class NoteCreateView(ListCreateAPIView):

    permission_classes = (IsAuthenticated, )

    '''List view for <int:user_pk>/notes/ CREATE note'''
    def post(self, request, user_pk):
        request.data['owner'] = user_pk
        created_note = NoteSerializer(data=request.data)
        if created_note.is_valid():
            created_note.save()
            return Response(
              created_note.data,status=status.HTTP_201_CREATED)
        return Response(created_note.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class NoteDetailView(APIView):

    def delete(self, _request, **kwargs):
        print(kwargs)
        return Response({'hello': 'world'})
