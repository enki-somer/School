from django.db import models
from users.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher_profile")
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
