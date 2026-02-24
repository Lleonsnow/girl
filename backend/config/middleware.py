from urllib.parse import unquote

from django.core.signing import BadSignature, Signer
from django.http import HttpResponseForbidden


def admin_secret(get_response):
    def middleware(request):
        from django.conf import settings
        secret = getattr(settings, 'ADMIN_SECRET_KEY', None) or ''
        if not request.path.startswith('/admin/'):
            return get_response(request)
        if not secret:
            return get_response(request)
        if settings.DEBUG:
            return get_response(request)
        signer = Signer()
        cookie_val = request.COOKIES.get('admin_access')
        if cookie_val:
            try:
                if signer.unsign(cookie_val) == secret:
                    return get_response(request)
            except BadSignature:
                pass
        raw_key = request.GET.get('admin_key') or ''
        key = unquote(raw_key).strip()
        if key == secret:
            response = get_response(request)
            response.set_cookie(
                'admin_access',
                signer.sign(secret),
                max_age=60 * 60 * 24 * 30,
                httponly=True,
                samesite='Lax',
                secure=not settings.DEBUG,
            )
            return response
        return HttpResponseForbidden('Access denied')
    return middleware
