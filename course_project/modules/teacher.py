class Teacher(object):
    def __init__(self, name, passwd, sex, age, salary):
        self.name = name
        self.passwd = passwd
        self.sex = sex
        self.age = age
        self.salary = salary
        self.class_list = []
    # def add_class(self, class_name, class_obj):
    #     self.class_dic[class_name] = class_obj
    def show_student(self, class_name):
        print("\033[32;1m班级%S的学生有：%s\033[0m" %(class_name, ','.join(self.class_dic[class_name])))
    def take_class(self):
        pass
    # def change_score(self, new_score):




