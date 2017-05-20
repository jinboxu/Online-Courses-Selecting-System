"""
import shelve

class Teacher(object):
    def __init__(self, name, age, sex, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
    def modify(self, salary):
        self.salary = salary

teacher1 = Teacher("Mr Wang", 43, 'M', 6500)
t1 = shelve.open("teacher1")
t1[teacher1.name] = teacher1
t1[teacher1.name].modify(7000)
t1.update(teacher1.modify(7000))
print(t1[teacher1.name].salary)
t1.close()
t2 = shelve.open("teacher1")
print(t2[teacher1.name].salary)
"""

print("\033[4;31;47m欢迎来到管理员视图\033[0m")
print("\033[1;31;47m欢迎来到管理员视图"
      "添加课程:\tcreate_course\n"
      "创建讲师:\tcreate_teacher\n"
      "增加班级:\tcreate_class\n"
      "查看校区信息:\tshow_info\n\033[0m\n")

class Student(object):
      def __init__(self, name):
            self.name = name

s = Student("Wang")
a = s
print(a.name)