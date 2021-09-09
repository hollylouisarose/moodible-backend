from rest_framework.views import APIView
from rest_framework.response import Response
from images.serializers import ImageSerializer
from .models import Image




class ImageListView(APIView):
    def get(self, _request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)

        return Response(serializer.data)
