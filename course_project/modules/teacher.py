class Teacher(object):
    def __init__(self, name, sex, age, salary):
        self.name = name
        self.sex = sex
        self.age = age
        self.salary = salary
        self.class_list = []
    def add_class(self, class_obj):
        self.class_list.append(class_obj.teacher_obj.name)