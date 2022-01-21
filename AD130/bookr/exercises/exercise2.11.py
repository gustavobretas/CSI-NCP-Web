# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Book
book = Book.objects.get(title='The Talisman')
book.contributors.all()