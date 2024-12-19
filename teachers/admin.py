from django.contrib import admin
from .models import Teacher

from .models import Schedule

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'hire_date', 'phone_number')
    search_fields = ('user__username', 'subject')
    list_filter = ('hire_date',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'day_of_week', 'start_time', 'end_time', 'subject')
    list_filter = ('day_of_week',)
    search_fields = ('teacher__user__username', 'subject')
