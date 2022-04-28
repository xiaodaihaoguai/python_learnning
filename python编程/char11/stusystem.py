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

'''def search() : #按照自己理解写的
    while True :
        answer1=input("按照id搜索请按1，按照姓名搜索请按2：")
        if answer1=='1' :
            student_id=input('请输入学生id')
            with open(filename,'r',encoding='utf-8') as  rfile :
                student_old=rfile.readlines()
                for item in student_old :
                    d=dict(eval(item))
                    if student_id==d['id'] :
                        lst1=[]
                        lst2=[]
                        lst1=['id','姓名','英语','python','java','总成绩']
                        lst2.append(d['id'])
                        lst2.append(d['name'])
                        lst2.append(d['english'])
                        lst2.append(d['python'])
                        #,d['java'],d['english']+d['python']+d['java'])
                        #d['english'],d['python'],d['java'],d['english']+d['python']+d['java'])
                        print(lst1)
                        print(lst2)
        elif answer1=='2':
            student_id = input('请输入学生姓名')
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d = dict(eval(item))
                    if student_id == d['name']:
                        lst3 = []
                        lst4 = []
                        lst3 = ['id', '姓名', '英语', 'python', 'java', '总成绩']
                        lst4.append(d['id'])
                        lst4.append(d['name'])
                        lst4.append(d['english'])
                        lst4.append(d['python'])
                        lst4.append(d['java'])
                        lst4.append(int(d['python'])+int(d['java'])+int(d['python']))
                        print(lst3)
                        print(lst4)
        else:
            print('请重新输入')
            continue
        answer2=input('是否继续y/n')
        if answer2=='y' :
            continue
        else:
            break
            '''

def search() :
    student_query=[]
    while True :
        id=''
        name=''
        if os.path.exists(filename) :
            mode=input('按照ID查找输入1，按照姓名查找输入2：')
            if mode=='1':
                id=input('请输入学生id')
            elif mode=='2':
                name=input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename,'r',encoding='utf-8') as  rfile :
                student=rfile.readlines()
                for item in student :
                    d=dict(eval(item))
                    if id!='' :
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='' :
                        if d['name']==name:
                            student_query.append(d)
            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查询：y/n?')
            if answer=='y':
                continue
            else:
                break

def show_student(lst):
    if len(lst)==0 :
        print('没有查到学生信息，无数据显示')
        return
    #定义显示格式,结构化字符串
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst :
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))

def delete() :
    while True :
        student_id=input('请输入要输入删除的学生id：')
        if student_id!='' :
            if os.path.exists(filename) :#判断文件是否存在
                with open(filename,'r',encoding='utf-8') as file:
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
            if answer=='y' :
                continue
            else:
                break

'''def modify() : #太牛逼了  自己独立写的第一段代码 继续加油
    while True :
        student_id=input('请输入要输入修改的学生id：')
        if student_id!="" :
            if os.path.exists(filename):
                with open(filename,'r',encoding="utf-8") as file1 :
                    student_old=file1.readlines()
            else:
                student_old=[]
            flag = False  # 标记是否修改
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile :
                    d={}
                    for item in student_old :
                        d=dict(eval(item))
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
'''

def modify():
    show()
    if os.path.exists(filename) :
        with open(filename,'r',encoding='utf-8') as rfile :
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改的学生id：')
    with open(filename,'w',encoding="utf-8") as wfile :
        for item in student_old :
            d=dict(eval(item))
            if d['id']==student_id :
                print('找到相关学生信息，可以修改他的信息了！')
                while True :
                    try:
                        d['name']=input('请输入姓名')
                        d['english']=input('请输入英语成绩：')
                        d['python']=input('请输入python成绩：')
                        d['java']=input('请输入java成绩：')
                    except :
                        print('您输入的信息有误')
                    else:
                        break

                wfile.write(str(d)+"\n")
                print('修改成功')
            else:
                wfile.write(str(d)+"\n")
        answer=input('是否继续修改？y/n\n')
        if answer=='y' :
            modify()

'''def sort() :#自己实现排序功能
    while True :
        if os.path.exists(filename):
            show()
            answer = input('请选择（0升序，1降序）：')
            if answer!='0' and answer!='1':
                print('输入有误，请重新输入')
                continue
            with open(filename,"r",encoding='utf-8') as rfile :
                students=rfile.readlines()
                lst=[]
                lst1=[]
                choice1=''
                choice_num=input('请输入排列顺序0-英语成绩 1-python成绩 2-java成绩 3-总成绩')
                if choice_num=='0' :
                    choice1='english'
                elif choice_num=='1' :
                    choice1='python'
                elif choice_num=='2' :
                    choice1='java'
                if choice_num=='0' and choice_num=='1' and choice_num=='2':
                    for item in students :
                        d=dict(eval(item))
                        lst.append(d[choice1])
                    if answer=='0' :
                        lst.sort()
                    else:
                        lst.sort(reverse=True)
                    with open(filename, 'w', encoding='utf-8') as wfile1:
                        wfile1.write('')
                        for i in lst :
                            for item in students :
                                d2=dict(eval(item))
                                if d2[choice1]==i:
                                    with open(filename, 'a', encoding='utf-8') as wfile:
                                        wfile.write(str(d2) + "\n")
                elif choice_num=='3':
                    for item2 in students:
                        d = dict(eval(item2))
                        lst1.append(d['english']+d['python']+d['java'])
                    if answer == '0':
                        lst1.sort()
                    else:
                        lst1.sort(reverse=True)
                    with open(filename, 'w', encoding='utf-8') as wfile2 :
                        wfile2.write('')
                        for j in lst1:
                            for item in students:
                                d3 = dict(eval(item))
                                if d3['english']+d3['python']+d3['java'] == j:
                                    with open(filename, 'a', encoding='utf-8') as wfile:
                                        wfile.write(str(d3) + "\n")

                else:
                    print('输入异常，请重新输入')
                    break

                show()
                break
'''
def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile :
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list :
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择0，升序，1，降序：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入')
        sort()
    mode=input('请选择排序方式1.英语 2.python 3.Java 0.总成绩')
    if mode==1:
        student_new.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool) # 表示列表当中的每一项 这块儿没太懂？
    elif mode==2:
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)  # 表示列表当中的每一项 这块儿没太懂？
    elif mode==3:
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)  # 表示列表当中的每一项 这块儿没太懂？
    elif mode==0:
        student_new.sort(key=lambda x: int(x['english'])+int(x['java'])+int(x['python']), reverse=asc_or_desc_bool)# 表示列表当中的每一项 这块儿没太懂？

    '''
    else:
        print('输入有误')
        sort()
    '''
    show_student(student_new)
def total() :
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile :
            student_old=rfile.readlines() #readlines 返回的原来是列表啊
            num=0
            for item in student_old :
                if item!=0 :
                    num+=1
            print('学生总数为{}'.format(num)) # 格式化字符串 {}作为转义

    else:
        print('没有保存的信息')
        return
    answer = input('是否继续统计总数？y/n\n')
    if answer == 'y':
        total()

def show() :
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile :
            students=rfile.readlines()
            format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
            print(format_title.format('ID','姓名','英语成绩','python成绩','java成绩','总成绩'))
            format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
            for item in students :
                d = dict(eval(item))
                print(format_data.format(d.get('id'),
                                         d.get('name'),
                                         d.get('english'),
                                         d.get('python'),
                                         d.get('java'),
                                         int(d.get('english')) + int(d.get('python')) + int(d.get('java'))))
            answer=input('是否继续显示y/n')
            if answer=='y' :
                show()
            else:
                return



if __name__ == '__main__':
    main()



