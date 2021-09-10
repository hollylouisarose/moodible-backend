from django.urls import path
from .views import (
ImageListView, ImageDetailView, NoteCreateView)

urlpatterns = [
  path('', ImageListView.as_view()),
  path('<int:pk>', ImageDetailView.as_view()),
  path('<int:user_pk>/notes/', NoteCreateView.as_view())
]
