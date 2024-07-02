from django.contrib import admin
from .models import (
    Register,
    MenProduct,
    WomenProduct,
    KidsProduct,
    FashionProduct,
    GadgetProduct,

)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "fname",
        "username",
        "email",
        "phone_no",
        "password",
    )


admin.site.register(Register, UserAdmin)

admin.site.register(MenProduct)

admin.site.register(WomenProduct)

admin.site.register(KidsProduct)

admin.site.register(FashionProduct)

admin.site.register(GadgetProduct)
