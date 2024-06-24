from django.contrib import admin
from .models import Register, MenProduct


class UserAdmin(admin.ModelAdmin):
    list_display = ("fname","username","email","phone_no","password",)
admin.site.register(Register, UserAdmin)

admin.site.register(MenProduct)
