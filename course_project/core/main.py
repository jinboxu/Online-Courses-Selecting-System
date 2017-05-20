import os
import pickle
from modules.school import School
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_dir_path = base_dir + os.sep + "database" + os.sep
print(database_dir_path)

class Manager_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print("\n欢迎进入CLASS_SYSTEM系统\n"
                  "1 学生视图\n"
                  "2 教师视图\n"
                  "3 学校视图\n"
                  "q 退出管理系统\n")
            choice = input("请选择： ").strip()
            if choice == '1':
                Student_manager()
            elif choice == '2':
                pass
            elif choice == '3':
                School_manager()
            elif choice == 'q':
                break
            else:
                print("你的输入不存在，请重新输入...")
                continue

class School_manager(object):
    def __init__(self):
        if os.path.exists(database_dir_path+"pickle_beijing"):
            with open(database_dir_path+"pickle_beijing", "rb") as f:
                self.school_beijing = pickle.load(f)
            with open(database_dir_path+"pickle_shanghai", "rb") as f:
                self.school_shanghai = pickle.load(f)
            self.run()
        elif not os.path.exists(database_dir_path+"pickle_beijing"):
            self.school_beijing = School("老男孩北京","北京")
            self.school_beijing.create_course("linux", 5000, 5)
            self.school_beijing.create_course("python", 8000, 8)
            self.school_shanghai = School("老男孩上海", "上海")
            self.school_shanghai.create_course("go", 7000 , 7)
            with open(database_dir_path + "pickle_beijing", "wb") as f:
                pickle.dump(self.school_beijing, f)
            with open(database_dir_path + "pickle_shanghai", "wb") as f:
                pickle.dump(self.school_shanghai, f)
            self.run()
    def run(self):
        while True:
            def operate():
                while True:
                    print("\033[1;31;47m欢迎来到管理员视图"
                          "添加课程:\tcreate_course\n"
                          "创建讲师:\tcreate_teacher\n"
                          "增加班级:\tcreate_class\n"
                          "查看校区信息:\tshow_info\n"
                          "保存，退出程序:\texit\033[0m\n")
                    choice = input(">>: ").strip()
                    if hasattr(self, choice):
                        getattr(self, choice)()
                    elif choice == "exit":
                        pass
                    else:
                        print("无此方法，请重新输入")
                        continue

            choice_school = input("\033[34;0m输入选择管理的学校名:\033[0m(北京\上海)")
            if choice_school == "北京":
                self.school_obj = self.school_beijing
                operate()
                with open(database_dir_path + "pickle_beijing", "wb") as f:
                    pickle.dump(self.school_obj, f)
            elif choice_school == "上海":
                self.school_obj = self.school_shanghai
                operate()
                with open(database_dir_path + "pickle_shanghai", "wb") as f:
                    pickle.dump(self.school_obj, f)
            else:
                print("输出错误，请重新输入")
    def add_course(self):
        course_name = input("\033[34;0m输入添加课程的名称：\033[0m").strip()
        course_price = input("\033[34;0m输入添加课程的价格：\033[0m").strip()
        course_time = input("\033[34;0m输入添加课程的周期：\033[0m").strip()
        if course_name in self.school_obj.school_course:
            print("课程存在")
            self.school_obj.school_course[course_name].price = course_price
            self.school_obj.school_course[course_name].time = course_time
            print("\033[32;1m课程更新完成\033[0m")
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print("\033[32;1m课程添加成功\033[0m")

    def create_teacher(self):
        teacher_name = input("\033[34;0m输入创建讲师的姓名：\033[0m").strip()
        teacher_sex = input("\033[34;0m输入创建讲师的性别：\033[0m").strip()
        teacher_age = input("\033[34;0m输入创建讲师的年龄：\033[0m").strip()
        teacher_salary = input("\033[34;0m输入创建讲师的工资：\033[0m").strip()
        if teacher_name in self.school_obj.school_teacher:
            print("讲师存在")
            self.school_obj.school_teacher[teacher_name].sex = teacher_sex
            self.school_obj.school_teacher[teacher_name].age = teacher_age
            self.school_obj.school_teacher[teacher_name].salary = teacher_salary
            print("\033[32;1m讲师更新完成\033[0m")
        else:
            self.school_obj.create_teacher(teacher_name, teacher_sex, teacher_age, teacher_salary)

    def create_class(self):
        class_name = input("\033[34;0m输入创建班级的名称：\033[0m").strip()
        while True:
            class_course = input("\033[34;0m输入创建班级关联的课程：\033[0m").strip()
            if class_course in self.school_obj.school_course:
                break
            print("\033[31;47m你输入的课程不存在，请重新输入\033[0m")
            continue
        class_course_obj = self.school_obj.school_course[class_course]
        while True:
            class_teacher = input("\033[34;0m输入创建班级关联的讲师：\033[0m").strip()
            if class_teacher in self.school_obj.school_teacher:
                break
            print("\033[31;47m你输入的讲师不存在，请重新输入\033[0m")
            continue
        class_teacher_obj = self.school_obj.school_teacher[class_teacher]
        self.school_obj.create_class(class_name, class_course_obj, class_teacher_obj)

    def show_info(self):
        print("\033[32;1m学校名称：%s\033[0m" %self.school_obj.name)
        for key in self.school_obj.school_course:
            course_obj = self.school_obj.school_course[key]
            print("\033[32;1m课程：%s\t价格：%s\t周期：%s\033[0m" %(course_obj.name, course_obj.price, course_obj.course_time))
        for key in self.school_obj.school_class:
            class_obj = self.school_obj.school_class[key]
            print("\033[32;1m班级：%s\t讲师：%s\033[0m" %(class_obj.name, class_obj.teacher_obj.name))

class Student_manager(School_manager):
    def __init__(self):
        pass
    def run(self):
        while True:
            student_name = input("输入学生名： ").strip()
            if student_name in self.school_obj:
                pass         #....。。。。



