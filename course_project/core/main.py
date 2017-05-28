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
                Teacher_manager()
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
            choice_school = input("\033[34;0m输入选择管理的学校名:\033[0m(北京\上海)")
            if choice_school == "北京":
                self.school_obj = self.school_beijing
                self.operate()
                with open(database_dir_path + "pickle_beijing", "wb") as f:
                    pickle.dump(self.school_obj, f)
                    print("数据已保存")
                exit()
            elif choice_school == "上海":
                self.school_obj = self.school_shanghai
                self.operate()
                with open(database_dir_path + "pickle_shanghai", "wb") as f:
                    pickle.dump(self.school_obj, f)
                    print("数据已保存")
                exit()
            else:
                print("输出错误，请重新输入")

    def operate(self):
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
                break
            else:
                print("无此方法，请重新输入")
                continue
        pass

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
        teacher_passwd=input("\033[34;0m输入创建讲师的密码：\033[0m").strip()
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
            self.school_obj.create_teacher(teacher_name, teacher_passwd, teacher_sex, teacher_age, teacher_salary)

    def create_class(self):
        """创建课程，关联一个老师，同时老师也关联了这个课程对象。注意：一个老师可以关联多个课程对象"""
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
        # class_obj = self.school_obj.school_class[class_name]
        self.school_obj.school_teacher[class_teacher].class_list.append(class_name)    #同时关联这个课程对象

    def show_info(self):
        print("\033[32;1m学校名称：%s\033[0m" %self.school_obj.name)
        for key in self.school_obj.school_course:
            course_obj = self.school_obj.school_course[key]
            print("\033[32;1m课程：%s\t价格：%s\t周期：%s\033[0m" %(course_obj.name, course_obj.price, course_obj.course_time))
        for key in self.school_obj.school_class:
            class_obj = self.school_obj.school_class[key]
            print("\033[32;1m班级：%s\t讲师：%s\033[0m" %(class_obj.name, class_obj.teacher_obj.name))

class Student_manager(School_manager):
    def operate(self):
        while True:
            choice1 = input("\033[1;31;47m登陆(login)或注册(eroll)\033[0m").strip()
            if choice1 == "login" or choice1 == "eroll":
                break
        if hasattr(self, choice1):
            getattr(self, choice1)()
        choice2 = input("是否查看你当前的分数y/n,保存，退出程序:\texit\033[0m\n")
        if choice2 == "y":
            print("你的分数为%s" %self.school_obj.school_student[self.student_name].score)
        elif choice2 == "exit":
            pass

    def login(self):
        while True:
            while True:
                student_name = input("名称： ").strip()
                if student_name:
                    break
            self.student_name = student_name
            while True:
                passwd = input("密码： ").strip()
                if passwd:
                    break
            if student_name in self.school_obj.school_student and passwd == self.school_obj.school_student[student_name].passwd:
                print("欢迎你，%s" %student_name)
                break
            else:
                print("用户名或密码错误，请重新登陆")
                continue
    def eroll(self):
        while True:
            student_name = input("名称： ").strip()
            if student_name:
                break
        self.student_name = student_name
        while True:
            passwd = input("密码： ").strip()
            if passwd:
                break
        while True:
            sex = input("性别(男\女)： ").strip()
            if sex == "男" or sex == "女":
                break
            else:
                print("你输入的不和规范")
        while True:
            age = input("年龄： ").strip()
            if age.isdigit():
                age = int(age)
                if age < 15:
                    print("年龄不能这么小吧...")
                    continue
                elif age > 30:
                    print("一个学生，年龄不可能这么大吧...")
                    continue
                else:
                    break
            else:
                print("你输入的不符合规范")
        while True:
            self.school_obj.show_class()
            class_name = input("以上是各个班级和同学，选择哪个班级？").strip()
            if class_name in self.school_obj.school_class:
                break
            else:
                print("你输入的班级不存在，请重新选择")
        class_obj = self.school_obj.school_class[class_name]
        self.school_obj.eroll_student(student_name, passwd, sex, age, class_obj)
    def show_core(self):
        pass

class Teacher_manager(School_manager):
    def operate(self):
        self.login()
        while True:
            print("\033[1;31;47m欢迎来到讲师视图"
                  "选择今天上课的班级:\ttake_class\n"
                  "查看班级的学生:\tshow_student\n"
                  "给学生改分:\tchange_score\n"
                  "保存，退出程序:\texit\033[0m\n")
            choice = input(">>: ").strip()
            if hasattr(self, choice):
                getattr(self, choice)()
            elif choice == "exit":
                break
            else:
                print("无此方法，请重新输入")
                continue
        pass

    def login(self):
        while True:
            while True:
                teacher_name = input("名称： ").strip()
                if teacher_name:
                    break
            self.teacher_name = teacher_name
            while True:
                passwd = input("密码： ").strip()
                if passwd:
                    break
            if teacher_name in self.school_obj.school_teacher and passwd == self.school_obj.school_teacher[teacher_name].passwd:
                print("欢迎你，%s" %teacher_name)
                break
            else:
                print("用户名或密码错误，请重新登陆")
                continue

    @staticmethod
    def get_class_name(self):
        print(self.teacher_name)
        teacher_obj = self.school_obj.school_teacher[self.teacher_name]
        while True:
            print("你所授的班级有", ','.join(teacher_obj.class_list))
            class_name = input("选择你教授的班级名： ").strip()
            if class_name in teacher_obj.class_list:
                return  class_name
            else:
                print("输入的不存在，请重新输入")

    def take_class(self):
        class_name = Teacher_manager.get_class_name(self)
        print("今天的授课班级为%s" %class_name)

    def show_student(self):
        class_name = Teacher_manager.get_class_name(self)
        print("\033[32;1m班级：\t%s\n"
              "学生：\t%s\033[0m" %(class_name, ','.join(self.school_obj.school_class[class_name].class_student)))

    def change_score(self):
        class_name = Teacher_manager.get_class_name(self)
        class_student_list = self.school_obj.school_class[class_name].class_student
        print("\033[32;1m班级：\t%s\n"
              "学生：\t%s\033[0m" % (class_name, ','.join(class_student_list)))
        while True:
            student_name = input("请选择学生: ").strip()
            if student_name in class_student_list:
                break
            else:
                print("你输入的学生不存在，请重新输入")
        while True:
            new_score = input("您给该学生的分数为： ").strip()
            if new_score.isdigit():
                break
            else:
                print("你输入的不是一个数值")
        self.school_obj.school_student[student_name].score = new_score
















