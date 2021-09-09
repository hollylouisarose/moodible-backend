from django.db import models

class Mood(models.Model):
    MOOD_CHOICES = [
      ('Calm', 'Calm'),
      ('Playful', 'Playful'),
      ('Adventurous', 'Adventurous'),
    ]
    choice = models.CharField(max_length=20, choices=MOOD_CHOICES)

    def __str__(self):
        return f'{self.choice}'

class Image(models.Model):
    source = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, related_name='moods', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description}'
