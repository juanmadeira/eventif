from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at', 'contacted_today')
    search_fields = ('name', 'email', 'phone', 'message', 'created_at')
    date_hierarchy = 'created_at'

    def contacted_today(self, obj):
        return obj.created_at.date() == now().date()

    contacted_today.short_description = 'Enviada hoje'
    contacted_today.boolean = True


admin.site.register(Contact, ContactModelAdmin)