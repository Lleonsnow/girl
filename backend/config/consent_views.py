import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import CookieConsent


def get_client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


@csrf_exempt
@require_http_methods(['POST'])
def consent_create(request):
    try:
        body = json.loads(request.body or '{}')
        consent_type = body.get('consent_type')
        if consent_type not in ('full', 'essential'):
            return JsonResponse({'error': 'invalid consent_type'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'invalid json'}, status=400)

    obj = CookieConsent.objects.create(
        consent_type=consent_type,
        ip_address=get_client_ip(request),
        user_agent=(request.META.get('HTTP_USER_AGENT') or '')[:512],
    )
    return JsonResponse({'consent_id': str(obj.consent_id)})


@require_http_methods(['GET'])
def consent_check(request):
    consent_id = request.GET.get('id') or request.COOKIES.get('cookie_consent_id')
    if not consent_id:
        return JsonResponse({'accepted': False})

    try:
        obj = CookieConsent.objects.get(consent_id=consent_id)
        return JsonResponse({'accepted': True, 'consent_type': obj.consent_type})
    except CookieConsent.DoesNotExist:
        return JsonResponse({'accepted': False})
