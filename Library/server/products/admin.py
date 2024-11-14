from django.contrib import admin
from django.template.loader import render_to_string

from .models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'picture',
        'status',
        'created',
        'modified',
        'file',
    ]

    list_filter = [
        'category',
        'status',
        'created',
        'modified',
    ]

    search_fields = [
        'name',
        'description',
    ]

    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    'category',
                    'status',
                )
            }
        ),
        (
            'Описание', {
                'fields': (
                    'short_description',
                    'description',
                    'specifications',
                    'image',
                )
            }
        )
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'object': obj}
        )


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'picture',
        'product_num',
        'description',
        'created',
        'modified',
    ]

    list_filter = [
        'created',
        'modified',
    ]

    search_fields = ['name']

    fieldsets = (
        (
            None,
            {'fields': ('name',)}
        ),
        (
            'Описание',
            {'fields': ('description',)}
        )
    )

    inlines = [
        ProductInline
    ]

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'object': obj}
        )

    def product_num(self, obj):
        return obj.category.count()
