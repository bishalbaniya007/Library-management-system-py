class Book:
  def __init__(self, book_id, title, author, available = True, borrowed_by = None):
    self.book_id = book_id
    self.title = title
    self.author = author
    self.available = available
    self.borrowed_by = borrowed_by

  def __str__(self):
    status = "Available" if self.available else "Borrowed"

    return(f"\n-------------------------------- \nId: {self.book_id} \nTitle: {self.title} \nAuthor: {self.author} \nStatus: {status} \n--------------------------------")

# b1 = Book("101", "Laws of motion", "Newton")
# print(b1)

# b2= Book("102", "Python Fundamentals", "Vakso")
# print(b2)
