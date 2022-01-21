# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Publisher

publisher = Publisher(name='Packt Publishing', website='https://www.packtpub.com', email='info@packtpub.com')
publisher.save()
publisher.email = 'customersupport@packtpub.com'
publisher.save()