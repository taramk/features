from django.contrib import admin
from features.models import Feature, Customer, Comment


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ['title']

admin.site.register(Feature, FeatureAdmin)

admin.site.register(Customer)

admin.site.register(Comment)

admin.site.site_header = 'Feature Admin'
