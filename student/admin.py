from django.contrib import admin
from .models import Student,Subject,StudentSubject
# Register your models here.

class StudentSubjectAdmin(admin.TabularInline):
    model=StudentSubject
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","first_name","last_name","email","roll"]
    inlines=[StudentSubjectAdmin]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=["subject_name"]

@admin.register(StudentSubject)
class StudentSubjectAdmin(admin.ModelAdmin):
    list_display=["id","subject","student"]