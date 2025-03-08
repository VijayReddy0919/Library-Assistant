from django.contrib import admin
from olmsapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('studentid', 'admin', 'mobilenumber')  # Specify the fields to display

admin.site.register(Student, StudentAdmin)
