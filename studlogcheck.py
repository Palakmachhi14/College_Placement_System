from django.db.models import models

class Student(models.Model):
    enrollment_no = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    # Add other profile information fields
