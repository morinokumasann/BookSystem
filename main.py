

from datetime import datetime

book_list=[]
book={}
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
    while True:
        book_name = input("请输入书籍名称")
        if not book_name:
            break
        author = input("请输入作者名")
        if not author:
            break
        date_of_publication = input("请输入出版日期（如19910101等)")
        if date_of_publication.isdigit():
            book = {"book_name": book_name, "author": author, "date_of_publication": date_of_publication}
            book_list.append(book)
            break
        else:
            print("您输入了非法格式 请输入正确的格式 类似（19910909）")


def delete():
    book_name=input("请输入要删除的书籍名称")
    count=0
    number=0
    global book_list
    for i in book_list:
        if book_name==i['book_name']:
            count=1
            del book_list[number]
            print("书籍已删除")
            number +=1
    if count==0:
        print("书籍不存在")







def modify():
    book_name=input("请输入要修改的书籍名称")
    count = 0
    number = 0
    global book_list
    for i in book_list:
        if book_name==i["book_name"]:
            count=1
            del book_list[number]
            new_book_name=book_name
            author = input("请输入要修改的作者名")
            date_of_publication=input("请输入要修改出版日期（如19910101等)")
            if date_of_publication.isdigit():
                new_book={"book_name":new_book_name,"author":author,"date_of_publication":date_of_publication}
                book_list.append(new_book)
                print("修改成功")
            else:
                print("您输入了非法格式 请输入正确的格式 类似（19910909）")
        number+=1
    if count==0:
        print("书籍不存在")



def search():
    book_name = input("请输入要查看书籍名称")
    count=0
    print("书籍名称\t作者\t出版日期\t")
    global book_list
    for i in book_list:
        if book_name ==i["book_name"]:
            count=1
            print('%s\t%s\t%s\t'%(i['book_name'],i['author'],i["date_of_publication"]))
    if count==0:
            print("书籍不存在")


def show():
    print("书籍名称\t作者\t出版日期\t")
    global book_list
    for i in book_list:
        print('%s\t%s\t%s\t'%(i['book_name'],i['author'],i['date_of_publication']))






main()




