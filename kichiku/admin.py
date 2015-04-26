from django.contrib import admin
from .models import Audio


# Register your models here.
class AudioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['source', 'file', 'pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('text', 'source', 'pub_date')
    search_fields = ['text']
    list_filter = ['source']

admin.site.register(Audio, AudioAdmin)