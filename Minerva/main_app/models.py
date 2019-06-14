from django.db import models


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    parents = models.ForeignKey(Parent, on_delete=models.CASCADE, default=None)
    courses = M2M
    teachers = M2M
    assignments = M2M


class Teacher(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField(min_length=10)
    courses = 
    students = M2M


class Parent(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField(min_length=10)
    students = 

class Assignments(models.model):
    due_date = models.DateField()
    classroom = M2M
    description = models.TextField(max_length=300)
    title = models.CharField(max_length=50)
    document = models.FileField()


class Classroom(models.model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    students = M2M
    time = models.TimeField()


class Courses(models.model):
    title = models.CharField()
    CATEGORIES = (
        (ENG, 'English'),
        (MATH, 'Mathematics'),
        (LANG, 'Foreign Language'),
        (HIST, 'History'),
        (SCI, 'Science')
    )
    category = models.CharField(
        choices=CATEGORIES,
        default=None,
    )
    course_number = models.IntegerField()
    classroom = 