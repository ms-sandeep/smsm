from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.dept_name

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='instructors')
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    credits = models.IntegerField(default=3)
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, related_name='courses')
    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course  = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    grade = models.CharField(max_length=4, blank=True)
    semester = models.CharField(max_length=20, blank=True)
    year = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'semester', 'year')  # optional

    def __str__(self):
        return f"{self.student} - {self.course}"
