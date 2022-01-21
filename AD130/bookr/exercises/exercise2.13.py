# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
Contributor.objects.filter(last_names='Tyrrell'). update(first_names='Mike')
Contributor.objects.get(last_names='Tyrrell').first_names