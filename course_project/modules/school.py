from modules.course import Course
from modules.classs import Classes
from modules.teacher import Teacher
from modules.student import Student

class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.school_course = {}
        self.school_class = {}
        self.school_teacher = {}
        self.school_student = {}
    def create_course(self, course_name, course_price, course_time):
        """创建课程"""
        course_obj = Course(course_name, course_price, course_time)
        self.school_course[course_name] = course_obj
    def show_course(self):
        """查看课程信息"""
        # for k,v in self.school_course.items():
        #     print("\33[1;42,43m 课程：%s\t价格：%s\t周期：%s月\033[0m]") %(k, v.price, v.course_time)
        for k in self.school_course:
            course_obj = self.school_course[k]
            print("\033[1;42;43m 课程：%s\t价格：%s\t周期：%s月\033[0m" %(course_obj.name, course_obj.price, course_obj.course_time))
    def create_teacher(self, teacher_name, teacher_passwd, teacher_sex, teacher_age, teacher_salary):
        """创建老师"""
        teacher_obj = Teacher(teacher_name, teacher_passwd, teacher_sex, teacher_age, teacher_salary)
        self.school_teacher[teacher_name] = teacher_obj
    def update_teacher(self, teacher_name, class_obj):
        """更新老师信息"""
        teacher_obj = self.school_teacher[teacher_name]
        teacher_obj.add_class(class_obj)
        self.school_teacher[teacher_name] = teacher_obj
    def show_teacher(self):
        """查看老师信息"""
        for key in self.school_teacher:
            teacher_obj = self.school_teacher[key]
            print("\033[1;34;42m讲师：%s\t性别：%s\t薪资：%s\t关联班级：%s\033[0m" %(teacher_obj.name, teacher_obj.sex,\
                                                                         teacher_obj.salary, ','.join(teacher_obj.class_list)))
    def create_class(self, class_name, course_obj, teacher_obj):
        class_obj = Classes(class_name, course_obj, teacher_obj )
        self.school_class[class_name] = class_obj
    def show_class(self):
        for key in self.school_class:
            class_obj = self.school_class[key]
            course_obj = class_obj.class_course
            print("\033[32;1m班级：%s\t关联课程：%s\t讲师：%s\t学生：%s\t\033[0m" %(class_obj.name, class_obj.class_course.name, class_obj.teacher_obj.name,\
                                                                        class_obj.class_student))
    def eroll_student(self, name, passwd, sex, age, class_obj):
        student_obj = Student(name, passwd, sex, age, class_obj)
        self.school_student[name] = student_obj
        self.school_class[class_obj.name].class_student.append(name)

"""
a = School("feihuang", "beijing")
a.create_course("linux", 5000, 5)
a.create_course("python", 8000, 8)
a.create_teacher("Mr Xu", "M", 26, 9000)
a.create_teacher("Mr Zhang", "M", 26, 8000)
a.create_class("python1", a.school_course["python"], a.school_teacher["Mr Xu"])
a.create_class("linux1", a.school_course["linux"], a.school_teacher["Mr Zhang"])
a.eroll_student("xiaoxu", "flzx3qc", "M", 26, a.school_class["python1"])
a.eroll_student("xiaoming", "123456", "M", 25, a.school_class["linux1"])
a.show_course()
a.show_teacher()
a.show_class()
"""