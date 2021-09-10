from django.urls import path
from .views import (
ImageListView, ImageDetailView, NoteCreateView,
NoteDetailView)

urlpatterns = [
  path('', ImageListView.as_view()),
  path('<int:pk>', ImageDetailView.as_view()),
  path('<int:user_pk>/notes/', NoteCreateView.as_view()),
  path('<int:user_pk>/notes/<int:note_pk>/', NoteDetailView.as_view())
]
