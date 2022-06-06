from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, Review, BookContributor

class BookAdmin(admin.ModelAdmin):
	search_fields = ('title', 'isbn', 'publisher__name__startswith')
	date_hierarchy = 'publication_date'
	list_display = ('title', 'isbn', 'get_publisher', 'publication_date')
	list_filter = ('publisher', 'publication_date')

	def get_publisher(self, obj):
		return obj.publisher.name


class ReviewAdmin(admin.ModelAdmin):
	fieldsets = (('Linkage', {'fields': ('creator', 'book')}), ('Review content', {'fields': ('content', 'rating')}))


class ContributorAdmin(admin.ModelAdmin):
	search_fields = ('last_names__startswith', 'first_names')
	list_display = ('last_names', 'first_names')
	list_filter = ('last_names',)


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(BookContributor)
