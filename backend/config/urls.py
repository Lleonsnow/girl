from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

from .consent_views import consent_check, consent_create
from .site_config_views import site_config


def api_health(request):
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', api_health),
    path('api/consent/', consent_create),
    path('api/consent/check/', consent_check),
    path('api/site-config/', site_config),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
