from django.contrib import admin

from registration.models import Registration


# Register your models here.
class Registrations(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_links = ('student', 'course')

admin.site.register(Registration, Registrations)
