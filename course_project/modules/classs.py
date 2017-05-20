class Classes(object):
    def __init__(self, name, course_obj, teacher_obj):
        self.name = name
        self.class_course = course_obj
        self.teacher_obj = teacher_obj
        self.class_student = []      #当此对象有多个的时候，用字典或列表（列表一般只记录简单的info）的方式记录