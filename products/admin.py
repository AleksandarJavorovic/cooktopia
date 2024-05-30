from django.contrib import admin
from .models import Product, Category, ReviewRating


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "brand",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "name",
    )


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subject",
        "rating",
        "created_on",
        "updated_on",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
