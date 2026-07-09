class Student:
  def __init__(self, std_id, name, password, borrowed_books = []):
    self.std_id = std_id
    self.name = name
    self.password = password
    self.borrowed_books = borrowed_books

  def __str__(self):
    return (f"\nId: {self.std_id} \nName: {self.name} \npassword: {self.password}\nBorrowed_books: {self.borrowed_books}")

# std = Student(101, "Bishal", "hey")
# print(std)
