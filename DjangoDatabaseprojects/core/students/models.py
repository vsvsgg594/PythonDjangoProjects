from django.db import models

# Create your models here.
class StudentID(models.Model):
    student_id=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.student_id


class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class Student(models.Model):
    student_id=models.OneToOneField(StudentID,related_name="studentsid",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
   
    student_email=models.EmailField(unique=True)
    department=models.ForeignKey(Department,related_name="depatment",on_delete=models.CASCADE)

class Subject(models.Model):
    subject=models.CharField(max_length=100)


    
    
    
class SubjectMark(models.Model):
    student=models.ForeignKey(Student,related_name="studentsmark",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    mark=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} and {self.subject.subject}'

    class Meta:
        unique_together=['student','subject']    
