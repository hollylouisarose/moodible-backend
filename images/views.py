
from rest_framework import status
from rest_framework.generics import (
  ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

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

    permission_classes = (IsAuthenticated, )

    '''Delete view for <int:user_pk>/notes/<int:note_pk>/ DELETE note'''

    def delete(self, _request, **kwargs):
        note_pk= kwargs['note_pk']
        try:
            note_to_delete = Note.objects.get(pk=note_pk)
            note_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            raise NotFound()

    '''Update view for <int:user_pk>/notes/<int:note_pk>/ DELETE note'''

    def put(self, request, **kwargs):
        note_pk= kwargs['note_pk']
        request.data['owner'] = request.user.id
        note_to_edit = Note.objects.get(pk=note_pk)
        edited_note = NoteSerializer(note_to_edit, data=request.data)
        if edited_note.is_valid():
            edited_note.save()
            return Response(
            edited_note.data, status=status.HTTP_202_ACCEPTED
          )
        return Response(edited_note.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ImageLikeView(APIView):
    ''' Adds likes to images, removes if already liked'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, image_pk):
        try:
            image_to_like = Image.objects.get(pk=image_pk)
        except Image.DoesNotExist:
            raise NotFound()

        if request.user in image_to_like.liked_by.all():
            image_to_like.liked_by.remove(request.user.id)
        else:
            image_to_like.liked_by.add(request.user.id)

        serialized_image = ImageSerializer(image_to_like)

        return Response(serialized_image.data, status=status.HTTP_202_ACCEPTED)
