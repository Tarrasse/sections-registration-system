from django.contrib import admin

from section.models import Client, Course, Section, Reg


class SectionInline(admin.TabularInline):
    model = Section


class CourseAdmin(admin.ModelAdmin):
    inlines = [SectionInline, ]


class RegInline(admin.TabularInline):
    model = Reg
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    inlines = [RegInline, ]


class ClientAdmin(admin.ModelAdmin):
    inlines = [RegInline, ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Reg)
