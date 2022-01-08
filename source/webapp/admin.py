from django.contrib import admin

# Register your models here
from webapp.models import Guest

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'status']
    list_filter = ['created_at']
    search_fields = ['email', 'name']
    fields = ['name', 'email', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Guest, GuestAdmin)
