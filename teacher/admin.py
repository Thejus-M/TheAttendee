from django.contrib import admin

# Register your models here.
from .models import student,Attendant,Class

class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno','name','class_section')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('classname','name')


class AttendantAdmin(admin.ModelAdmin):
    list_display = ('name','attendants','subject','period_no','time')

admin.site.register(Attendant,AttendantAdmin)
admin.site.register(student,StudentAdmin)
admin.site.register(Class, ClassAdmin)