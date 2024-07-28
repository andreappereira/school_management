from django.contrib import admin

from student.models import Student


# Register your models here.
class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('name',)

admin.site.register(Student, Students)
