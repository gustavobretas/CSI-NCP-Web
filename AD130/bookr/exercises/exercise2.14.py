# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
Contributor.objects.get(last_names='Wharton').delete()
Contributor.objects.get(last_names='Wharton')