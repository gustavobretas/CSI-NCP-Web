# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Publisher

publisher = Publisher.objects.get(name='Pocket Books')

publisher

publisher.name

publisher.website

publisher.email

publisher = Publisher.objects.get(website='https://pocketbookssampleurl.com')

publisher.name

Publisher.objects.get(pk=2)

Publisher.objects.get(id=2)