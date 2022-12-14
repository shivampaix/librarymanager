class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lenddict={}
    def displaybooks(self):
        print(f"We have these books in {self.name}'s Library")
        for book in self.bookslist:
            print(book)
    def notavailablebooks(self):
        print("Not Available books are:")
        for book in self.lenddict:
            print(book)
    def availablebooks(self):
        dict=[]
        for book in self.bookslist:
            if book not in self.lenddict:
                dict.append(book)
        for book in dict:
            print(book)
    def totalbooks(self):
        print(f"Total no of books in library are :{len(self.bookslist)} ")
    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Book lending successfull")
        else :
            print(f"book has already taken by {self.lenddict[book]}")
    def addbook(self,book):
        self.bookslist.append(book)
        print("book has been added")
    def returnbook(self,book):
        self.lenddict.pop(book)

if __name__=='__main__':
    shivam=library(['Python','Alchemist','Ugly love'],"Shivampaix")

    while(True):
        print(f"Welcome to the {shivam.name} library. Enter your choice to continue")  
        print("1. Display Library")
        print("2. Lend a book")
        print("3.Add a book")
        print("4.Return a book")
        print("5.Total Books")
        print("6.Not Available books")
        print("7.Available Books")
        user_choice=input()
        if user_choice not in ['1','2','3','4','5','6','7']:
            print("Not valid selection")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            shivam.displaybooks()
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend :")
            user=input("Enter your name:")
            shivam.lendbook(user,book)
        elif user_choice==3:
            book=input("Enter the name of your book you want to add:")
            shivam.addbook(book)
        elif user_choice==4:
            book=input("Enter the name of your book you want to return:")
            shivam.returnbook(book)
        elif user_choice==5:
            shivam.totalbooks()
        elif user_choice==6:
            shivam.notavailablebooks()
        elif user_choice==7:
            shivam.availablebooks()
        else :
            print("not a valid option")
        print("press c to continue and q to exit")
        user_choice1=input()
        while(user_choice1!='c'and user_choice1!='q'):
            if user_choice1=='c':
                continue
            elif user_choice1=='q':
                exit()
