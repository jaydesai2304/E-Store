from django.contrib import admin
from .models import (
    Register,
    MenProduct,
    WomenProduct,
    KidsProduct,
    FashionProduct,
    GadgetProduct,
    News_Letter,
    CartItem,
    Contact,

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

admin.site.register(News_Letter)

admin.site.register(CartItem)


class Messages(admin.ModelAdmin):
    list_display = ("fname", "email", "message",)

admin.site.register(Contact, Messages)
