from django.db import models

# Create your models here.
class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    tag = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.question[:50]
