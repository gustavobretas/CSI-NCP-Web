from django.contrib import admin
from admin import BookAdmin, ContributorAdmin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)


# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
