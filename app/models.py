from django.db import models

# Create your models here.
class List(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.text
