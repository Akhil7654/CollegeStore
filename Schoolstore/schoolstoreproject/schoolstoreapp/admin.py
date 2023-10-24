from django.contrib import admin

from schoolstoreapp.models import Department, Course, Box, Testimonial


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('dname',)}
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cname',)}
admin.site.register(Course,CourseAdmin)

admin.site.register(Box)
admin.site.register(Testimonial)