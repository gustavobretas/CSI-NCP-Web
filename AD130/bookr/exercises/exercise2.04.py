# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Book, Publisher
from datetime import date
publisher = Publisher.objects.get(name='Packt Publishing')
book = Book.objects.create(title="Advanced Deep Learning with Keras", publication_date=date(2018, 10, 31), isbn="9781788629416", publisher=publisher)
