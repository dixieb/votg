from django.db import models
from django.urls import reverse
from django.utils import timezone

# If making changes in code,
# Step 1: in terminal, type py manage.py makemigrations criminals
# Step 2: in terminal, type py manage.py migrate

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    photo = models.CharField(max_length=1000)
    dob = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    permit = models.CharField(max_length=10)
    notes = models.CharField(max_length=2000)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' - ' + self.permit

class Offence(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    offence = models.CharField(max_length=255)

    def __str__(self):
        return self.person.firstName + " " + self.person.lastName + " - " + self.offence

class Desc(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    height = models.CharField(max_length=50)
    build = models.CharField(max_length=20)
    hair = models.CharField(max_length=20)
    eyes = models.CharField(max_length=20)
    teeth = models.CharField(max_length=20)
    weight = models.CharField(max_length=3)
    complexion = models.CharField(max_length=20)
    facial_hair = models.CharField(max_length=20)
    tattoo = models.CharField(max_length=20)
    scars = models.CharField(max_length=20)
    face_shape = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('criminals:detail', kwargs={'pk': self})

    def __str__(self):
        return self.person.firstName + ' ' + self.person.lastName + ": " + self.person.permit


class Report(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('criminals:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.person.permit + ' - ' + self.person.firstName + ' ' + self.person.lastName
