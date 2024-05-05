from django.contrib import admin

from course.models import course


# Register your models here.
class courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(course, courses)
