
import os
filename="book.txt"

def main():
    while True:
        menu()
        choice=int(input("请输入您所要使用的功能（如1，2等)"))
        if choice in[0,1,2,3,4,5]:
            if choice==0:
                answer=input("您确定要退出系统吗（Y/N）")
                if answer=="Y":
                    print("谢谢您的使用")
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                delete()
            elif choice==3:
                modify()
            elif choice==4:
                search()
            elif choice==5:
                show()






def menu():
    print("---------------图书管理系统---------------")
    print("-----------------功能菜单-----------------")
    print("--------------1:添加书籍信息--------------")
    print("--------------2:删除书籍信息--------------")
    print("--------------3:修改书籍信息--------------")
    print("--------------4:查询书籍信息--------------")
    print("--------------5:显示所有书籍--------------")
    print("--------------0:退出---------------------")


def insert():
    book_list=[]
    while True:
        book_name=input("请输入书名")
        if not book_name:
            break
        author=input("请输入作者名")
        if not author:
            break

        try:
            date_of_publication = int(input("请输入出版日期"))
        except:
            print(" 输入无效 非整数")
            continue

        book={"book_name":book_name,"author":author,"date_of_publication":date_of_publication}
        book_list.append(book)
        answer=input("是否继续添加?（Y/N)\n")
        if answer=="Y":
            continue
        else:
            break

    save(book_list)
    print("书籍信息录入完毕")

def save(list):
    try:
        book_txt=open(filename,"a",encoding="utf-8")
    except:
        book_txt=open(filename,"w",encoding="utf-8")
    for item in list:
        book_txt.write(str(item)+"\n")
    book_txt.close()



def delete():
    while True:
        book_name=input("请输入要删除的书籍名")
        if book_name!="":
            if os.path.exists(filename):
                with open(filename,"r",encoding="utf-8")as file:
                    book_name1=file.readlines()

            else:
                book_name1=[]
            flag=False
            if book_name1:
                with open(filename,"w",encoding="utf-8")as wfile:
                    d={}
                    for item in book_name1:
                        d=dict(eval(item))
                        if d["book_name"]!=book_name:
                            wfile.write(str(d)+"\n")
                        else:
                            flag=True
                    if flag:
                        print(f"书名为{book_name}的书籍已删除")
                    else:
                        print(f"没有找到书名为{book_name}的书籍")
            else:
                print("没有所查找的书籍信息")
                break
            show()
            answer=input("是否继续删除呢(Y/N)\n")
            if answer=="Y":
                continue
            else:
                break
def modify():
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8")as rfile:
            book_name1=rfile.readlines()
    else:
        return
    book_name=input("请您输入要修改的书籍名称")
    with open(filename,"w",encoding="utf-8")as wfile:
        for item in book_name1:
            d=dict(eval(item))
            if d["book_name"]==book_name:
                print("找到您所寻找的书籍 可以修改内容 ")
                while True:
                   try:
                    d["name"]=input("请输入书籍名称")
                    d["author"]=input("请输入作者名")
                    d["date_of_publication"]=input("请输入出版日期")
                   except:
                       print("非法输入")
                   else:
                       break
                wfile.write(str(d)+"\n")
                print("修改书籍内容成功")

            else:
                wfile.write(str(d)+"\n")





def search():
    pass
def show():
    pass

if __name__ == '__main__':
    main()