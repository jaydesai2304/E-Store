from django.contrib import admin
from .models import Register


class UserAdmin(admin.ModelAdmin):
    list_display = ("fname","username","email","phone_no","password",)
admin.site.register(Register, UserAdmin)
