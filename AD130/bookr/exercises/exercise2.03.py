# Execute the Code, line by line using the Terminal
# In order to open the Shell, run the following command

# python manage.py shell

from reviews.models import Contributor
contributor = Contributor.objects.create(first_names="Rowel", last_names="Atienza", email="RowelAtienza@example.com")
