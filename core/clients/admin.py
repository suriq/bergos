from django.contrib import admin
from .models import Company,Location,Person

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'tax_id', 'email', 'phone')
    search_fields = ('name', 'tax_id', 'email')
    list_filter = ('name',)






@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'address')
    search_fields = ('name', 'address', 'company__name')
    list_filter = ('company',)




@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone')
    search_fields = ('name', 'email', 'location__name', 'location__company__name')
    list_filter = ('location__company',)
