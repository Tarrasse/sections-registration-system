from django.contrib import admin

from section.models import Student, Course, Section


class SectionInline(admin.TabularInline):
    model = Section


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ]


admin.site.register(Student)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
