
from django.contrib.auth.models import AbstractUser
from django.db import models
from .helpers import StatusChoices

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add this related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Add this related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )





class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)


class Teacher(User):

    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'



class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)





class Modules(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)




class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    modules = models.ForeignKey(Modules, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)



class Tasks(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)



class Student(User):
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)


class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=StatusChoices.choices,default=StatusChoices.Published)
    created_at = models.DateTimeField(auto_now_add=True)










