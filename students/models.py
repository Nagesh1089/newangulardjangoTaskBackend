from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.TextField()
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
