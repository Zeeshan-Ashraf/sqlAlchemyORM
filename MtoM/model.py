from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from dataclasses import dataclass

MYSQL_DB_CONNECT_URI = 'mysql+pymysql://root:@127.0.0.1:3306/data_db?charset=utf8mb4'  # use 'sqlite:///data.db' for local file storage
mysqlEngine = create_engine(MYSQL_DB_CONNECT_URI, echo=True)
mysqlSession = sessionmaker(bind=mysqlEngine)()
Base = declarative_base()


@dataclass
class Student(Base):
    __tablename__ = 'student'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255))
    courses = relationship('Course', secondary='student_course_association', back_populates='students')

    # back_populates=anotherTable.relatedColRelatiohsipVar tells sqlAlchemy that when User.Addresses changes it should also reflect
    # the updates in other table
    # details: https://stackoverflow.com/questions/39869793/when-do-i-need-to-use-sqlalchemy-back-populates

    def __repr__(self):
        return 'id={}, name={}, courses[]={}'.format(self.id, self.name, [course.title for course in self.courses])


@dataclass
class Course(Base):
    __tablename__ = 'course'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255))
    students = relationship('Student', secondary='student_course_association', back_populates='courses')

    # back_populates=anotherTable.relatedColRelatiohsipVar tells sqlAlchemy that when User.Addresses changes it should also reflect
    # the updates in other table
    # details: https://stackoverflow.com/questions/39869793/when-do-i-need-to-use-sqlalchemy-back-populates

    def __repr__(self):
        return 'id={}, title={}, students[]={}'.format(self.id, self.title, [student.name for student in self.students])


@dataclass
class StudentCourse(Base):
    __tablename__ = 'student_course_association'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))

    def __repr__(self):
        return 'id={}, student={}, course={}'.format(self.id, self.student_id, self.course_id)


Base.metadata.create_all(mysqlEngine)  # order of table class (or import) doesn't matter
