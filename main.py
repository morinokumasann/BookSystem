



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
        if not date_of_publication:
            break
        book = {"book_name": book_name, "author": author, "date_of_publication": date_of_publication}
        book_list.append(book)

        break






def delete():
    book_name=input("请输入要删除的书籍名")
    count=0
    number=0
    for i in book_list:
        if book_name==i['book_name']:
            count=1
            delete[number]
            print("书籍已删除")
        number +=1
    if count==0:
        print("书籍不存在")







def modify():
    pass

main()




