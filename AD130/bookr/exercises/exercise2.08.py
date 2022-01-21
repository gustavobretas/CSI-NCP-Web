# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
Contributor.objects.all()
contributors = Contributor.objects.all()
contributors[0]
contributors[0].first_names
contributors[0].last_names

