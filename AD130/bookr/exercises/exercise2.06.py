# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Book, Contributor
book = Book.objects.get(title="Advanced Deep Learning with Keras")

contributor = Contributor.objects.create(first_names='Packt', last_names='Example Editor', email='PacktEditor@example.com')
book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})

book.contributors.create(first_names='Packtp', last_names= 'Editor Example', email='PacktEditor2@example.com', through_defaults={'role': 'EDITOR'})

from reviews.models import Publisher
publisher = Publisher.objects.create(name='Pocket Books', website='https://pocketbookssampleurl.com', email='pocketbook@example.com')

contributor1 = Contributor.objects.create(first_names= 'Stephen', last_names='Stephen', email='StephenKing@example.com')
contributor2 = Contributor.objects.create(first_names= 'Peter', last_names='Straub', email='PeterStraub@example.com')

from datetime import date
book = Book.objects.create(title='The Talisman', publication_date=date(2012, 9, 25), isbn='9781451697216', publisher=publisher)

book.contributors.add(contributor, through_defaults={'role': 'EDITOR'})