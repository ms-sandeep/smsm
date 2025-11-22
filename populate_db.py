
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms_project.settings')
django.setup()

from core.models import Department, Instructor, Student, Course, Enrollment

def run():
    Enrollment.objects.all().delete()
    Course.objects.all().delete()
    Instructor.objects.all().delete()
    Student.objects.all().delete()
    Department.objects.all().delete()

    depts = [
        ("Computer Science","Block A"),("Mathematics","Block B"),("Physics","Block C"),
        ("Chemistry","Block D"),("Biology","Block E"),("English","Block F"),
        ("History","Block G"),("Economics","Block H"),("Psychology","Block I"),
        ("Business","Block J")
    ]
    dept_objs = [Department.objects.create(dept_name=n, location=l) for n,l in depts]

    instr_data = [
        ("Alice Kumar","alice.k@example.com",dept_objs[0]),
        ("Bob Singh","bob.s@example.com",dept_objs[1]),
        ("Carol Rao","carol.r@example.com",dept_objs[0]),
        ("David Lee","david.l@example.com",dept_objs[2]),
        ("Esha Patel","esha.p@example.com",dept_objs[3]),
        ("Farhan Khan","farhan.k@example.com",dept_objs[4]),
        ("Grace Liu","grace.l@example.com",dept_objs[5]),
        ("Hiro Tanaka","hiro.t@example.com",dept_objs[6]),
        ("Indira Das","indira.d@example.com",dept_objs[7]),
        ("John Paul","john.p@example.com",dept_objs[8]),
    ]
    instr_objs = [Instructor.objects.create(name=n,email=e,dept=d) for n,e,d in instr_data]

    student_data = [
        ("Sandeep Sai","2002-05-10","sandeep@example.com","123 Main St"),
        ("Anita Verma","2001-08-20","anita.v@example.com","45 Park Ave"),
        ("Ravi Kumar","2003-01-15","ravi.k@example.com","78 Oak Street"),
        ("Maya Nair","2002-11-30","maya.n@example.com","22 Garden Rd"),
        ("Vikram Joshi","2001-03-22","vikram.j@example.com","56 Lake View"),
        ("Priya Sharma","2003-07-07","priya.s@example.com","89 River St"),
        ("Karan Mehta","2002-12-12","karan.m@example.com","34 Hilltop"),
        ("Neha Gupta","2001-09-09","neha.g@example.com","12 Elm St"),
        ("Amit Roy","2003-04-04","amit.r@example.com","90 Sunset Blvd"),
        ("Richa Bansal","2002-02-02","richa.b@example.com","11 Maple Ave"),
    ]
    student_objs = [Student.objects.create(name=n, dob=dob, email=em, address=addr) for n,dob,em,addr in student_data]

    course_data = [
        ("Intro to Programming",3,instr_objs[0]),
        ("Data Structures",4,instr_objs[2]),
        ("Discrete Math",3,instr_objs[1]),
        ("Physics I",4,instr_objs[3]),
        ("Chemistry I",4,instr_objs[4]),
        ("Biology I",3,instr_objs[5]),
        ("English Lit",2,instr_objs[6]),
        ("World History",3,instr_objs[7]),
        ("Microeconomics",3,instr_objs[8]),
        ("Marketing Basics",2,instr_objs[9]),
    ]
    course_objs = [Course.objects.create(course_name=n, credits=c, instructor=i) for n,c,i in course_data]

    enrollments = [
        (student_objs[0], course_objs[0], 'A','Fall',2024),
        (student_objs[1], course_objs[0], 'B+','Fall',2024),
        (student_objs[2], course_objs[1], 'A-','Fall',2024),
        (student_objs[3], course_objs[2], 'B','Fall',2024),
        (student_objs[4], course_objs[3], 'A','Fall',2024),
        (student_objs[5], course_objs[4], 'B-','Fall',2024),
        (student_objs[6], course_objs[1], 'B+','Fall',2024),
        (student_objs[7], course_objs[5], 'A','Fall',2024),
        (student_objs[8], course_objs[6], 'A-','Fall',2024),
        (student_objs[9], course_objs[7], 'B+','Fall',2024),
        (student_objs[0], course_objs[1], 'A-','Spring',2025),
        (student_objs[1], course_objs[2], 'B','Spring',2025),
        (student_objs[2], course_objs[0], 'B+','Spring',2025),
        (student_objs[3], course_objs[3], 'A','Spring',2025),
        (student_objs[4], course_objs[4], 'B+','Spring',2025),
        (student_objs[5], course_objs[1], 'C','Spring',2025),
        (student_objs[6], course_objs[2], 'B-','Spring',2025),
        (student_objs[7], course_objs[3], 'A','Spring',2025),
        (student_objs[8], course_objs[4], 'B+','Spring',2025),
        (student_objs[9], course_objs[5], 'A-','Spring',2025),
    ]
    for s,c,g,sem,y in enrollments:
        Enrollment.objects.create(student=s, course=c, grade=g, semester=sem, year=y)

    print("Done. Database populated.")

if __name__ == '__main__':
    run()
