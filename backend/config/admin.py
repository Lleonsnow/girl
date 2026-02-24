from django.contrib import admin
from .models import CookieConsent


@admin.register(CookieConsent)
class CookieConsentAdmin(admin.ModelAdmin):
    list_display = ('consent_id', 'consent_type', 'ip_address', 'created_at')
    list_filter = ('consent_type',)
    search_fields = ('consent_id', 'ip_address')
    readonly_fields = ('consent_id', 'created_at')
