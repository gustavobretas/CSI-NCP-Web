from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
