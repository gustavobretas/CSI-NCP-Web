from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')
    exclude = ['date_edited']
    # fieldsets = (('Linkage', {'fields': ('creator', 'book')}),
    #              ('Review content',
    #               {'fields': ('content', 'rating')}))

