# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
Contributor.objects.create(first_names='Peter', last_names='Wharton', email='PeterWharton@example.com')
Contributor.objects.create(first_names='Peter', last_names='Tyrrell', email='PeterTyrrell@example.com')
Contributor.objects.filter(first_names='Peter')
Contributor.objects.filter(first_names='Rowel')
Contributor.objects.filter(first_names='Nobody')
from reviews.models import Book
from datetime import date
book = Book.objects.filter(publication_date__gte=date(2018, 10, 30))
book
book[0].publication_date
book = Book.objects.filter(title__contains='Deep learning')
book
book[0].title
Contributor.objects.all()
Contributor.objects.exclude(first_names='Peter')
books = Book.objects.order_by("publication_date")
books
books[0].publication_date
books[1].publication_date
books = Book.objects.order_by("-publication_date")
books
books[0].publication_date
books[1].publication_date
books = Book.objects.order_by('id')
books[0].id
books[1].id
Book.objects.order_by('-id')
books[0].id
books[1].id
Book.objects.order_by('title')
books[0]
books[1]
Book.objects.order_by('-title')
books[0]
books[1]
from reviews.models import Publisher
publishers = Publisher.objects.all().values()
publishers
publishers[0]
publishers[1]
Book.objects.filter(publisher__name='Packt Publishing')
Publisher.objects.get(book__title='Advanced Deep Learning with Keras')
book = Book.objects.get(title='The Talisman')
book.publisher
publisher = Publisher.objects.get(name='Pocket Books')
publisher.book_set.all()
Book.objects.filter(publisher__name='Pocket Books').filter(title='The Talisman')
