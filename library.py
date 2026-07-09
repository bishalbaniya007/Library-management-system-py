from admin import Admin
from book import Book
from student import Student
from helpers import get_valid_input

class Library:
  def __init__(self):
    self.books = []
    self.students = []
    self.admins = []

  ## Admin Book Management Part ##
  def display_books(self):
    if not self.books:
      print("=== No books available ===\n")
      return
    
    for book in self.books:
      print(book)

  def search_book(self):
    title = get_valid_input("Enter the title of the book you want to serch for: ").strip().lower()

    found = False
    print("\n=== Matches Found ===\n")
    for book in self.books:
      if title in book.title.lower():
        print(book)
        found = True

    if not found:
      print("--- No books found ---\n")

  def add_book(self):
    id = get_valid_input("Enter the id of the book: ")
     
    # for book in self.books:
    #   if id == book.book_id:
    #     print("=== Book already exists ===\n")
    #     return
    if any(book.book_id == id for book in self.books):
      print("--- Book already exists ---\n")
      return
      
    title = get_valid_input("Enter the title of the book: ")
    author = get_valid_input("Enter the name of author: ")

    book = Book(id, title, author)
    self.books.append(book)

    print("--- Book added successfully ---\n")
  
  def remove_book(self):
    id = get_valid_input("Enter the id of the book: ")
    for book in self.books:
      if id == book.book_id:
        if not book.available:
          print("--- Can not remove a borrowed book ---\n")
          return
        
        self.books.remove(book)
        print("--- Book removed successfully ---\n")
        return
      
    print("--- No book found ---\n")

  def update_book(self):
    id = get_valid_input("Enter the id of the book: ")
    # if not any(book.book_id == id for book in self.books):
    #   print("--- Book not found ---\n")
    #   return
    
    for book in self.books:
      if id == book.book_id:
        while True:
          print("\n--- Menu ---")
          print("a. Title")
          print("b. Author")

          choice = input("\nWhat would you like to update? ").strip().lower()

          if choice == 'a':
            new_title = get_valid_input("Enter the new title: ")
            book.title = new_title
            break

          elif choice == 'b':
            new_author = get_valid_input("Enter the new author name: ")
            book.author = new_author
            break
          
          else:
            print("--- Invalid choice ---\n")
      
        print("--- Book updated successfully ---\n")
        return

    print("--- Book not found ---\n")

  def admin_login(self):
    admin_id = get_valid_input("Enter the admin id: ")

    for admin in self.admins:
      if admin_id == admin.admin_id:
        while True:
          password = get_valid_input("Enter the password: ")
          if password != admin.password:
            print("--- Incorrect password ---\n")
            continue
          
          print("--- Log in succesful ---\n")
          return admin
        
    print("--- Admin not found ---\n")


  ## Student Management Part ##
  def register_student(self):
    std_id = get_valid_input("Enter the student id: ")

    # for student in self.students:
    #   if std_id == student.std_id:
    #     print("--- Studnet already exists ---")
    if any(student.std_id == std_id for student in self.students):
      print("--- Student already exists ---\n")
      return
    
    name = get_valid_input("Enter the name of student: ")
    password = get_valid_input("Enter the password: ")

    student = Student(std_id, name, password)
    self.students.append(student)

    print("\n=== Student registered successfully ===\n")

  def student_login(self):
    std_id = get_valid_input("Enter the student id: ")

    for student in self.students:
      if std_id == student.std_id:
        while True:
          password = get_valid_input("Enter the password: ")
          if password != student.password:
            print("--- Incorrect password ---\n")
            continue

          print("\n=== Log in succesful ===\n")
          return student

    print("--- Student not found ---\n")

  def borrow_book(self, student):
    book_id = get_valid_input("Enter the id of the book: ")

    for book in self.books:
      if book_id == book.book_id:

        if book.available:
          book.borrowed_by = student
          book.available = False

          student.borrowed_books.append(book)

          print("--- Book borrowed successfully ---\n")
          return
        
        print("--- Book not available ---\n")
        return

    print("--- No book found ---\n")

  def return_book(self, student):
    book_id = get_valid_input("Enter the id of the book: ")

    for book in student.borrowed_books:
      if book_id == book.book_id:
        student.borrowed_books.remove(book)

        book.borrowed_by = None
        book.available = True
        
        print("--- Book returned successfully ---\n")
        return
      
    print("--- No book found ---\n")

  def view_borrowed_books(self, student):
    if not student.borrowed_books:
      print("--- No books borrowed at the moment ---\n")
      return
    
    print("=== Borrowed Books ===\n")
    for book in student.borrowed_books:
      print(book)
      

b1 = Book("101", "Laws of motion", "Newton")
b2= Book("102", "Python Fundamentals", "Vakso", False)
b3= Book("103", "Basic Math", "Einstein")

a1 = Admin("1", "admin", "admin")

lib = Library()

lib.books.append(b1)
lib.books.append(b2)
lib.books.append(b3)

lib.admins.append(a1)

# print(len(lib.books))
# print(len(lib.admins))
# print(len(lib.students))

# lib.search_book()

# print(len(lib.books))l
