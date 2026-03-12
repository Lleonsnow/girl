from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.urls import reverse
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import action
from unfold.enums import ActionVariant

from .models import CookieConsent, SiteImage


class SuperuserDeleteMixin:
    def has_delete_permission(self, request, obj=None):
        if getattr(request.user, 'is_superuser', False):
            return True
        return super().has_delete_permission(request, obj)


class RowDeleteMixin:
    actions_row = ['row_delete']

    @action(
        description='Удалить',
        url_path='delete',
        variant=ActionVariant.DANGER,
        permissions=['delete'],
    )
    def row_delete(self, request, object_id):
        meta = self.model._meta
        url_name = f'admin:{meta.app_label}_{meta.model_name}_delete'
        return redirect(reverse(url_name, args=[object_id]))


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(SuperuserDeleteMixin, RowDeleteMixin, UnfoldModelAdmin, UserAdmin):
    actions = ['delete_selected']


@admin.register(Group)
class CustomGroupAdmin(SuperuserDeleteMixin, RowDeleteMixin, UnfoldModelAdmin, GroupAdmin):
    actions = ['delete_selected']


@admin.register(SiteImage)
class SiteImageAdmin(SuperuserDeleteMixin, RowDeleteMixin, UnfoldModelAdmin):
    list_display = ('category', 'image_filename', 'order')
    list_editable = ('order',)
    list_filter = ('category',)
    list_per_page = 25
    list_max_show_all = 100
    ordering = ('category', 'order', 'pk')

    @admin.display(description='Файл')
    def image_filename(self, obj):
        return obj.image.name if obj.image else ''


@admin.register(CookieConsent)
class CookieConsentAdmin(SuperuserDeleteMixin, RowDeleteMixin, UnfoldModelAdmin):
    list_display = ('consent_id', 'consent_type', 'ip_address', 'created_at')
    list_filter = ('consent_type',)
    list_per_page = 50
    list_max_show_all = 200
    search_fields = ('consent_id', 'ip_address')
    readonly_fields = ('consent_id', 'created_at')
