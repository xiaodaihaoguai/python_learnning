# 工程名称：学生管理系统
# 作者：王宇
# 开发时间：2022/4/1 20:23
import os.path

filename='student.txt'
def main() :
    while True :
        menu()
        choice=int(input("请选择"))
        if choice in [0,1,2,3,4,5,6,7] :
            if choice == 0 :
                answer=input('您确定要退出系统嘛？y/n')
                if answer=='y' or 'Y' :
                    print('谢谢使用')
                    break #退出系统
                else :
                    continue
            elif choice == 1:
                insert()#录入学生信息
            elif choice == 2:
                search() #查找学生信息
            elif choice == 3:
                delete() #删除学生信息
            elif choice == 4:
                modify() #修改学生信息
            elif choice == 5:
                sort()  #统计学生总人数
            elif choice == 6:
                total() #总人数
            elif choice == 7 :
                show()  #显示所有信息

def menu() :
    print('====================学生信息管理系统===================')
    print('----------------------------------------------------')
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('-------------------------------------------------------')
def insert() :
    student_list=[]
    while True :
        id=input('请输入id（如1001）：')
        if not id:#空字符串的布尔值
            break
        name=input('请输入姓名：')
        if not name:
            break
        try:
            englist=int(input('请输入英语成绩：'))
            python=int(input('请输入python成绩'))
            java=int(input('请输入JAVA成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #讲录入的学生信息保存到字典里
        student={'id':id,'name':name,'english':englist,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加y/n')
        if answer=='y' :
            continue
        else:
            break

    #调用save函数
    save(student_list)
    print('学生信息录入完毕')
def save (lst) :
    try :
        stu_txt=open(filename,'a',encoding="utf-8")
    except :
        stu_txt=open(filename,'w',encoding="utf-8")
    for item in lst :
        stu_txt.write(str(item)+'\n')#将列表的每一行数据都添加进来
    stu_txt.close()
def search() :
    pass###阿
def delete() :
    while True :
        student_id=input('请输入要输入删除的学生id：')
        if student_id!='' :
            if os.path.exists(filename) :#判断文件是否存在
                with open(filename,'r',encoding='utf-8') as  file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False #标记是否删除
            if student_old :
                with open(filename,'w',encoding='utf-8') as wfile :
                    d={}
                    for item in student_old :
                        d=dict(eval(item)) # 将字符串转成字典
                        if d['id']!=student_id :
                            wfile.write(str(d)+"\n")
                        else:
                            flag=True
                    if flag:
                        print(f"id为{student_id}的学生信息已经被删除")
                    else:
                        print(f"没有找到ID为{student_id}的学生信息")
            else:
                print("无学生信息")
                break
            show() #删除之后要重新显示所有学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=="y" :
                continue
            else:
                break


def modify() :
    while True :
        student_id=input('请输入要输入修改的学生id：')
        if student_id!="" :
            if os.path.exists(filename):
                with open(filename,'w',encoding="utf-8") as file :
                    student_old=file.readlines()
            else:
                student_old=[]
            flag = False  # 标记是否修改
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile :
                    d={}
                    for item in student_old :
                        d=dict(eval(student_old))
                        if d["id"]!=student_id :
                            wfile.write(str(d)+"\n")
                        else :
                            id = student_id
                            name = input('请输入姓名：')
                            if not name:
                                print("输入名不能为空")
                                continue
                            try:
                                englist = int(input('请输入英语成绩：'))
                                python = int(input('请输入python成绩'))
                                java = int(input('请输入JAVA成绩'))
                            except:
                                print('输入无效，不是整数类型，请重新输入')
                                continue
                            # 讲录入的学生信息保存到字典里
                            student = {'id': id, 'name': name, 'english': englist, 'python': python, 'java': java}
                            wfile.write(str(student)+"\n")
                            flag=True
                        if flag :
                            print(f"id为{student_id}的学生信息已经被修改")
                        else:
                            print(f"没有找到学生信息")
        else:
            print("无学生信息")
            break
        show()  # 修改之后要重新显示所有学生信息
        answer = input('是否继续修改？y/n\n')
        if answer == "y":
            continue
        else:
            break










def sort() :
    pass
def total() :
    pass
def show() :
    pass

if __name__ == '__main__':
    main()



