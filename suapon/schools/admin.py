from django.contrib import admin
from .models import CertificateType, Course, CourseProfile, Institution,Campus, Lead,Manager
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class CampusInlineAdmin(admin.StackedInline):
    model=Campus
    list_display=['name','location','phone','admission_start_date','admission_end_date','region']
    list_filter=['region']
    extra=0
class InstitutionAdmin(admin.ModelAdmin):
    list_display=['name','institution_type','enable']
    list_filter=['enable','campus__region']
    inlines=[CampusInlineAdmin]
class CertificateTypeAdmin(admin.ModelAdmin):
    list_display=['name','abbreviation']
class CourseAdmin(admin.ModelAdmin):
    list_display=['name']
class CourseProfileAdmin(admin.ModelAdmin):
    list_display=['campus','course']
    list_filter=['certificates','mode_of_teaching','time_of_study']
class LeadsAdmin(admin.ModelAdmin):
    list_display=['lastname','firstname','gender','mobile','email','course','current_education_level']
    list_filter=['course__campus__institution']
    readonly_fields=['course','firstname','lastname','gender','mobile','current_education_level','email']
class ManagerInline(admin.StackedInline):
    model=Manager
    can_delete=False
class UserAdmin(BaseUserAdmin):
    inlines=[ManagerInline]

admin.site.register(Institution,InstitutionAdmin)
admin.site.register(CertificateType,CertificateTypeAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseProfile,CourseProfileAdmin)
admin.site.register(Lead,LeadsAdmin)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

admin.site.site_header='Suapon Administration'
admin.site.site_title='Suapon site admin'
#admin.site.index_title=''