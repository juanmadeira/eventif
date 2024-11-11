from django.contrib import admin
from subscriptions.models import Subscription

admin.site.register(Subscription)

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "cpf", "created_at")
    date_hierarchy = "created_at"
    search_fields = ("name", "email", )