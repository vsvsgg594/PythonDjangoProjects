from faker import Faker 
fake=Faker()
from .models import *
import random

def create_subject_mark(n):
    try:
        student_objs=StudentsData.objects.all()
        for student in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMark.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0,100)

                )
    except Exception as e:
        print(e)



def seed_db(n=10)->None:
    try:
        for i in range(n):
            
            department_objs=Department.objects.all()
            random_index=random.randint(0,len(department_objs)-1)
            department=department_objs[random_index]
            student_id=f'STU-0{random.randint(100,999)}'
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(18,30)
            address=fake.address()


       

            student_id_objs=StudentID.objects.create(student_id=student_id)

            student_objs=StudentsData.objects.create(
                   department=department,
                   student_id=student_id_objs,
                   student_name=student_name,
                   student_email=student_email,
                   student_age=student_age,
                   address=address,
    )
        
    except Exception as e:
        print(e)    