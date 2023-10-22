def return_book():
    students_pandas=pd.read_excel("students.xlsx")
    roll_no=str(input("Enter your roll number: ").strip())
    books_pandas=pd.read_excel("Books.xlsx")
    roll_numbers=[str(roll) for roll in students_pandas['roll_no']]
    if roll_no in roll_numbers:
        books_not_available=[]
        books_available=[]
        books=[str(b) for b in books_pandas['book']]
        status=[str(s) for s in books_pandas['status']]

        for i in range(len(status)):
            if status[i] == "yes":
                books_available.append(books[i])
            else:
                books_not_available.append(books[i])
        # print(books_available)
        # print(books_not_available)

        book_search=str(input('enter your book name to search: ').strip())
        if book_search in books_not_available:
            book_index=1
            for i in range(len(book_sheet['A'])):
                if book_sheet['A{}'.format(i+1)].value == book_search:
                    if str(book_sheet['D{}'.format(i+1)].value) == roll_no:
                        book_index=i+1
                        # print("done")
                        book_sheet['B{}'.format(book_index)]="yes"
                        book_sheet['C{}'.format(book_index)]=""
                        book_sheet['D{}'.format(book_index)]=""
                        book_sheet['E{}'.format(book_index)]=""
                        books_excel.save('Books.xlsx')
                        print("Book has been returned")
                        print("***************************************************")
                        break
                    else:
                        print("Wrong credentials")
                        print("***********************************************")
                        break
        elif book_search in books_available:
            print("Enter correct book name")
            print('***************************************')
        else:
            print("Enter correct book name")
            print('***************************************')
    else:
        print("************You are not registered*************")
        sign_up_for_register=str(input("Enter yes to sign up else press anything: "))
        if sign_up_for_register=="yes":
            student_row = (students_sheet.max_row)+1
            student_row1=sign_up(student_row)
            student_row=student_row+student_row1
            students.save('students.xlsx')

def detail_about_book_stocks():
    books_pandas=pd.read_excel("Books.xlsx")
    books_not_available=[]
    books_available=[]
    books=[str(b) for b in books_pandas['book']]
    status=[str(s) for s in books_pandas['status']]

    for i in range(len(status)):
        if status[i] == "yes":
            books_available.append(books[i])
        else:
            books_not_available.append(books[i])
    print("Total books are: ",len(books))
    print("******************************")
    print("Books are: ")
    print(books)
    print("*******************************")
    print("total available books are: ",len(books_available))
    print("Books that are available: ")
    print(books_available)
    print("************************************")
    print("total issued books are: ",len(books_not_available))
    print("Books that has been issued : ")
    print(books_not_available)
    print("***************************************")
    

while True:
    print("*******************************")
    print('press 1 to get book from library ')
    print('press 2 to return book into library')
    print('press 3 to get detail about library books')
    print('press 4 to exit')
    print("*****************************************")
    try:
        choice=int(input('enter what you want: '))
        if choice==1:
            get_book()
        elif choice==2:
            return_book()
        elif choice==3:
            detail_about_book_stocks()
        elif choice==4:
            print("Thanks for visiting")
            print("*********************")
            break
        else:
            print("Invalid Input")
            print("*************************")
    except Exception as e:
        print(e)
        print("invalid input")
        print("***********************")
        



