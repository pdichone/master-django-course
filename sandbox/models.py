from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    satisfaction = models.CharField(max_length=10)

    def __str__(self):
        return self.name
