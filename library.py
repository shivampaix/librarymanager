class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lenddict={}
    def displaybooks(self):
        print(f"We have these books in our Library: {self.name}")
        for book in self.bookslist:
            print(book)
    def totalbooks(self):
        print(f"Total no of books in library are :{len(self.bookslist)} ")
    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            self.bookslist.remove(book)
            print("Book registeration successfull")
        else :
            print(f"book has already taken by {self.lenddict[book]}")
    def addbook(self,book):
        self.bookslist.append(book)
        print("book has been added")
    def returnbook(self,book):
        self.lenddict.remove(book)

if __name__=='__main__':
    shivam=library(['Python','Alchemist','Ugly love'],"Shivampaix")

    while(True):
        print(f"Welcome to the {shivam.name} library. Enter your choice to continue")  
        print("1. Display a book")
        print("2. Lend a book")
        print("3.Add a book")
        print("4.Return a book")
        print("5.Total Books")
        user_choice=int(input())

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
        else :
            print("not a valid option")
        print("press c to continue and q to exit")
        user_choice1=input()
        while(user_choice1!='c'and user_choice1!='q'):
            if user_choice1=='c':
                continue
            elif user_choice1=='q':
                exit(all)
