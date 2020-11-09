from django.db import models

# Create your models here.

class Student(models.Model):

    GENDER = (
        ('M','Male'),
        ('F','Female'),
        ('U','Undisclosed')
    )

    name = models.CharField(max_length=30)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1,choices=GENDER)
    percentage = models.FloatField()

    institute = models.ForeignKey('Institute',on_delete= models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.name

class Institute(models.Model):
    TYPE = (
        ('c','college'),
        ('h','highSchool')
    ) 

    name = models.CharField(max_length=200)
    type_of_institute = models.CharField(max_length=1, choices=TYPE)

    def __str__(self):
        return self.name