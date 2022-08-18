from django.contrib import admin
from .models import Country, Category, Review

admin.site.register(Country)
admin.site.register(Category)



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'film', 'rate', 'posted_date']
    readonly_fields = ['posted_date' ,]
