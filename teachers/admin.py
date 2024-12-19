from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'hire_date', 'phone_number')
    search_fields = ('user__username', 'subject')
    list_filter = ('hire_date',)
