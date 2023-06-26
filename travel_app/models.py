from django.db import models

# Create your models here.
class Traveler(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    re_password=models.CharField(max_length=100)

    def __str__(selfself):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Career(models.Model):
    designation=models.CharField(max_length=100)
    salary = models.IntegerField()
    qualification=models.CharField(max_length=100)

    def __str__(self):
        return self.designation

class Apply(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    cv = models.CharField(max_length=100)

    def __str__(self):
        return self.name



