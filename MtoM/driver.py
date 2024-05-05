from MtoM.model import Student, Course, mysqlSession, StudentCourse

s1 = Student(name='Z')
s2 = Student(name='A')
c1 = Course(title='Math')
c2 = Course(title='English')
s1.courses = [c1, c2]
s2.courses = [c1]

mysqlSession.add_all([s1, s2])
mysqlSession.flush()
mysqlSession.commit()

students = mysqlSession.query(Student).all()
courses = mysqlSession.query(Course).all()
students_courses = mysqlSession.query(StudentCourse).all()
mysqlSession.flush()
mysqlSession.commit()

for student in students:
    print(student.__repr__())

for course in courses:
    print(course.__repr__())

for s_c in students_courses:
    print(s_c.__repr__())

mysqlSession.close()