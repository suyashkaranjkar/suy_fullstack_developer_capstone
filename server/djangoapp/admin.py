from django.contrib import admin
from .models import CarMake, CarModel


# Inline admin to display CarModels within CarMake admin page
class CarModelInline(admin.TabularInline):  # You can also use StackedInline
    model = CarModel
    extra = 1  # Number of empty forms shown by default


# Admin for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('type', 'year')
    search_fields = ('name', 'car_make__name')


# Admin for CarMake with inline CarModel
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]


# Register models with customized admin
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
