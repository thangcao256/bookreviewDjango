from django.contrib.admin import AdminSite
from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book, BookContributor, Review)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


class BookAdmin(admin.ModelAdmin):
    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])

    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')


# class ReviewAdmin(admin.ModelAdmin):
#     exclude = ['date_edited']


class ReviewAdmin(admin.ModelAdmin):
    exclude = ['date_edited']  # hoặc
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = (('Linkage', {'fields': ('creator', 'book')}), \
                 ('Review content', \
                  {'fields': ('content', 'rating')}))


# Register your models here.

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)


# Register your models here.
class BookrAdminSite(AdminSite):
    title_header = 'Bookreviews Admin'
    site_header = 'Bookreviews administration'
    index_title = 'Bookreviews site admin'


admin_site = BookrAdminSite(name='bookreviews')
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(Book)
admin_site.register(BookContributor)
admin_site.register(Review)
