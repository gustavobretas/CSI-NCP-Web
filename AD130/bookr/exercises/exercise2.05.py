# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Book
from reviews.models import Contributor
contributor = Contributor.objects.get(first_names='Rowel')
book = Book.objects.get(title="Advanced Deep Learning with Keras")

from reviews.models import BookContributor
book_contributor = BookContributor(book=book, contributor=contributor, role='AUTHOR')
book_contributor.save()