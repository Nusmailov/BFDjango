from django.contrib import admin
from main.models import Restaurant, User

admin.register(Restaurant)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
# Register your models here.
