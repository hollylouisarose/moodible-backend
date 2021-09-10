from django.urls import path
from .views import (
ImageListView,
ImageDetailView,
NoteCreateView,
NoteDetailView,
ImageLikeView)

urlpatterns = [
  path('', ImageListView.as_view()),
  path('<int:pk>', ImageDetailView.as_view()),
  path('<int:user_pk>/notes/', NoteCreateView.as_view()),
  path('<int:user_pk>/notes/<int:note_pk>/', NoteDetailView.as_view()),
  path('<int:image_pk>/like/', ImageLikeView.as_view())
]
