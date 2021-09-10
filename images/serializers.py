
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Image, Mood, Note
User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
        'username',
        'email',
        'profile_image',
        'liked_images')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    mood = MoodSerializer(read_only=True)
    liked_by = NestedUserSerializer(many=True, read_only=True)
    class Meta:
        model = Image
        fields = '__all__'
