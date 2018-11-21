from django.contrib import admin
from main.models import Book, Author

admin.site.register(Book)

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email')


