from django.contrib import admin

from section.models import Student, Course, Section


class SectionInline(admin.TabularInline):
    model = Section


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ]


class RegistrationInline(admin.TabularInline):
    model = Section.students.through


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        RegistrationInline,
    ]


class SectionAdmin(admin.ModelAdmin):
    inlines = [
        RegistrationInline,
    ]


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
