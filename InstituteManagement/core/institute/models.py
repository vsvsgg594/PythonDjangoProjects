from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    standard=models.CharField(max_length=100)

class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department    
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)    

class StudentsData(models.Model):
    department=models.ForeignKey(Department ,related_name="depatment" ,on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID ,on_delete=models.CASCADE)    
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    address=models.TextField()

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering=['student_name']
class SubjectMark(models.Model):
    student=models.ForeignKey(StudentsData,related_name="studentmakr",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()


    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name}'

    class Meta:
         unique_together=['student','subject']       