from rest_framework import serializers

from .models import Image, Mood

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    mood = MoodSerializer(read_only=True)
    class Meta:
        model = Image
        fields = '__all__'

