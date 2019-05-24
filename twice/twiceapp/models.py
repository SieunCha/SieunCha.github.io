from django.db import models
from Django.db import models

# Create your models here.
class Twice(models.Model):
    CHOICES = (
        ('KR', '한국'),
        ('JP', '일본'),
        ('TW', '대만'),
    )
    name = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    birth = models.DateTimeField(default = now)
    nationality = models.CharField(max_length = 20, choices = CHOICES)
    position = models.CharField(max_length = 20)


    def __str__(self):
        return self.name