from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    roll=models.IntegerField()
    email=models.EmailField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.first_name}"

class Subject(models.Model):
    subject_name=models.CharField(max_length=20,unique=True)
    
    def __str__(self) -> str:
        return self.subject_name


class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.student} {self.subject.subject_name}"
    
    class Meta:
        unique_together=('student','subject')

# stprofile()
# fk -->stu
# field = many
