from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsersAccount, Laboratory, Application, Computer, Bookings


class UsersAccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'student_no', 'surname', 'username', 'initials',
                    'qualification', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('id', 'email', 'student_no', 'surname',
                     'username', 'initials', 'qualification')
    readonly_fields = ('last_login', 'password')
    fieldsets = ()


admin.site.register(UsersAccount, UsersAccountAdmin)
admin.site.register(Laboratory)
admin.site.register(Application)
admin.site.register(Computer)
admin.site.register(Bookings)
