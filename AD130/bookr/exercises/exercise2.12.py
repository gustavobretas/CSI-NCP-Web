# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
contributor = Contributor.objects.get(first_names='Rowel')
contributor.book_set.all()