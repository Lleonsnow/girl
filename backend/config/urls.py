from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def api_health(request):
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', api_health),
]
