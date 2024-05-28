from django.contrib import admin

from app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_dispay=('student','paid_students')
    search_fields=('stusent',)
admin.site.register(Student,StudentAdmin)