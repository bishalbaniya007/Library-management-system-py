from library import lib

def show_menu():
  print("\n=== Library Management System ===\n")
  print("1. Student Portal")
  print("2. Admin Portal")
  print("3. Display Books")
  print("4. Search Books")
  print("5. Exit")

def student_portal():
  while True:
    print("\n=== Student Portal ===\n")
    print("1. Register ")
    print("2. Login")
    print("3. Back")

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        print("=== Register Student ===\n")
        lib.register_student()
        

      elif choice == 2:
        print("=== Student Login ===\n")
        student = lib.student_login()

        if student:
          student_dashboard(student)
          break

      elif choice == 3:
        break
      
      else: 
        print("--- Please choose a valid option ---\n")
    
    except ValueError:
      print("--- Invalid input ---\n")

def student_dashboard(student):
  while True:
    print("\n=== Student Dashboard ===\n")
    print("1. Borrow Book ")
    print("2. Return Book")
    print("3. View Borrowed Books")
    print("4. Logout")

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        print("=== Borrow Book ===\n")
        lib.borrow_book(student)

      elif choice == 2:
        print("=== Return Book ===\n")
        lib.return_book(student)
      
      elif choice == 3:
        print("=== View Borrowed Books ===\n")
        lib.view_borrowed_books(student)

      elif choice == 4:
        print("\n=== Logged out ===\n")
        break
      
      else: 
        print("--- Please choose a valid option ---\n")
    
    except ValueError:
      print("--- Invalid input ---\n")

def admin_portal():
  while True:
    print("\n=== Admin Portal ===\n")
    print("1. Login")
    print("2. Back")

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        print("=== Admin Login ===\n")
        admin = lib.admin_login()
        if admin:
          admin_dashboard()
          break

      elif choice == 2:
        break

      else:
        print("--- Please choose a valid option ---\n")

    except ValueError:
      print("--- Invalid input ---\n")

def admin_dashboard():
  while True:
    print("\n=== Admin Dashboard ===\n")
    print("1. Add Book ")
    print("2. Remove Book")
    print("3. Update Book")
    print("4. Display Books")
    print("5. Logout")

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        print("=== Add Book ===\n")
        lib.add_book()

      elif choice ==2:
        print("=== Remove Book ===\n")
        lib.remove_book()

      elif choice == 3:
        print("=== Update Book ===\n")
        lib.update_book()

      elif choice == 4:
        print("=== Display Books ===\n")
        lib.display_books()

      elif choice == 5:
        print("=== Logged out ===\n")
        break

      else:
        print("--- Please choose a valid option ---\n")
    
    except ValueError:
      print("--- Invalid input ---\n")


def main():
  while True:
    show_menu()

    try:
      choice = int(input("\nEnter your choice: "))

      if choice == 1:
        student_portal()

      elif choice == 2:
        admin_portal()
      
      elif choice == 3:
        print("\n=== Displaying Books ===\n")
        lib.display_books()

      elif choice == 4:
        print("\n=== Searching Book ===\n")
        lib.search_book()

      elif choice == 5:
        print("\n=== Thank you for using our system ===\n")
        break

      else:
        print("--- Please choose a valid option ---\n")

    except ValueError:
      print("--- Invalid input ---\n")



if __name__ == "__main__":
  main()
