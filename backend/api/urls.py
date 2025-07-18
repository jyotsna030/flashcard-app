from django.urls import path
from .views import FlashcardListCreate, FlashcardDelete

urlpatterns = [
    path('flashcards/', FlashcardListCreate.as_view(), name='flashcard-list-create'),
    path('flashcards/<int:pk>/', FlashcardDelete.as_view(), name='flashcard-delete'),
]