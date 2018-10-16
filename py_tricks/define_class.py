# Using namedtuple is easier method
# to define a class

from collections import namedtuple

Book = namedtuple('Book', 'pages type')

my_book = Book(100, 'ruled')
print(my_book.pages)  # returns number of pages
print(my_book.type)  # returns type i.e. ruled, unruled, etc

# String representation
print(my_book)

# namedtuples are immutable
my_book.pages = 200  # throws AttributeError
