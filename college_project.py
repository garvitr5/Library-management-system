"""
Project: Student library management system
"""

# Define a class Library to manage the library operations.
class Library:
    # Constructor to initialize the list of books.
    def __init__(self, listofBooks):
        self.books = listofBooks

    # Method to display available books.
    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" -- " + book)
        print("\n")

    # Method to borrow a book.
    def borrowBook(self, name, bookname):
        # Check if the book is available.
        if bookname not in self.books:
            print(f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            # Add the borrower's name and book to the track list and remove the book from available books.
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    # Method to return a book.
    def returnBook(self, bookname):
        # Print a message indicating the book has been returned and add the book back to available books.
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    # Method to donate a book.
    def donateBook(self, bookname):
        # Print a message indicating the book has been donated and add the book to available books.
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)

# Define a class Student to represent students using the library.
class Student():
    # Method for a student to request a book.
    def requestBook(self):
        print("So, you want to borrow book!")
        # Take input for the name of the book the student wants to borrow.
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    # Method for a student to return a book.
    def returnBook(self):
        print("So, you want to return book!")
        # Take input for the student's name and the name of the book they want to return.
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        # Check if the book is in the track list and remove it if found.
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    # Method for a student to donate a book.
    def donateBook(self):
        print("Okay! you want to donate book!")
        # Take input for the name of the book the student wants to donate.
        self.book = input("Enter name of the book you want to donate: ")
        return self.book

# Main part of the program starts here.
if __name__ == "__main__":
    # Create a Library object with a list of initial books.
    UPESlibrary = Library(
        ["Atomic Habits", "Rich Dad Poor Dad", "The Alchemist", "Ikigai", "Code in Python", "Let Us C"])
    # Create a Student object.
    student = Student()
    # Initialize an empty list to track borrowed books.
    track = []

    # Print welcome message and options menu.
    print("\t\t\t\t\t\t\t WELCOME TO THE UPES LIBRARY \n")
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")

    # Start a loop for user interaction.
    while (True):
            # Take user input for their choice.
            usr_response = int(input("Enter your choice: "))

            # Perform actions based on user's choice.
            if usr_response == 1:  # Listing available books
                UPESlibrary.displayAvailableBooks()
            elif usr_response == 2:  # Borrowing a book
                UPESlibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # Returning a book
                UPESlibrary.returnBook(student.returnBook())
            elif usr_response == 4:  # Donating a book
                UPESlibrary.donateBook(student.donateBook())
            elif usr_response == 5:  # Tracking borrowed books
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            elif usr_response == 6: # Exiting the library
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVALID INPUT! \n")
