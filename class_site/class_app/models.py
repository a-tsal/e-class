from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{User.objects.filter(pk=self.user.id)[0].username}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    interests = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    residence = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{User.objects.filter(pk=self.user.id)[0].username}'


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    lesson_code = models.CharField(max_length=5)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'


class StudentAttendLesson(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    @property
    def student_name(self):
        return User.objects.filter(pk=self.student.id)[0].username

    @property
    def lesson_name(self):
        return Lesson.objects.filter(pk=self.lesson.id)[0].name

    def __str__(self):
        return f'{Lesson.objects.filter(pk=self.lesson.id)[0].name} - ' \
               f'{Lesson.objects.filter(pk=self.lesson.id)[0].name}'


class Assignment(models.Model):

    assignment_file = models.FileField(upload_to='assignment_files/')
    upload_date_time = models.DateTimeField(auto_now=True)
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Assignment-{self.id} for lesson {Lesson.objects.filter(pk=self.lesson.id)[0].name}'


