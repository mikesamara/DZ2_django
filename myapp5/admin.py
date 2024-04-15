from django.contrib import admin
from .models import Category, Product


@admin.action(description='Сбросить кол-во в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    '''Список продуктов'''
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_add', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описания продукта (description)'
    actions = [reset_quantity]

    '''Отдельный продукт'''
    # fields = ['name', 'description', 'category', 'date_add', 'rating']
    readonly_fields = ['date_add', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            },
        ),
        (
            'Подробности',
            {'classes': ['collapse'],
             'description': 'Категория товара и его подробное описание',
             'fields': ['category', 'description'],
             },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг товара',
            {
                'description': 'Рейитинг сформирован автоматически на основе оценок покупателей',
                'fields': ['date_add', 'rating'],

            }
        ),

    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

# Register your models here.
