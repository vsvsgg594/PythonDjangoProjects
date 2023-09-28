from faker import Faker
fake=Faker()
import random
from .models import *

def create_students_mark(n):
    try:
        student_objs=Student.objects.all()
        for students in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                subjectsmark=SubjectMark.objects.create(
                    student=students,
                    subject=subject,
                    mark=random.randint(0,100)

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


            students_id_objs=StudentID.objects.create(student_id=student_id)
            student_obj=Student.objects.create(
                department=department,
                student_id=students_id_objs,
                student_name=student_name,
                student_email=student_email,

            )


    except Exception as e:
        print(e)    