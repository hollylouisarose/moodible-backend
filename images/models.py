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
    liked_by = models.ManyToManyField(
      'jwt_auth.User',
      related_name='liked_images',
      blank=True
    )

    def __str__(self):
        return f'{self.description}'

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='notes_made',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.title}'
