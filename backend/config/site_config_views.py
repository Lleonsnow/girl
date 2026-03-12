from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import SiteImage


def _image_url(request, img):
    if not img or not img.image:
        return None
    return request.build_absolute_uri(img.image.url)


@require_GET
def site_config(request):
    qs = SiteImage.objects.all()
    by_cat = {}
    for img in qs:
        by_cat.setdefault(img.category, []).append(img)
    hero = by_cat.get(SiteImage.CATEGORY_HERO, [None])[0]
    miniature = by_cat.get(SiteImage.CATEGORY_MINIATURE, [None])[0]
    carousel = sorted(by_cat.get(SiteImage.CATEGORY_CAROUSEL, []), key=lambda x: (x.order, x.pk))
    photo = sorted(by_cat.get(SiteImage.CATEGORY_PHOTO, []), key=lambda x: (x.order, x.pk))
    return JsonResponse({
        'authorName': settings.AUTHOR_NAME,
        'authorPseudonym': settings.AUTHOR_PSEUDONYM,
        'authorEmail': settings.AUTHOR_EMAIL,
        'siteUrl': getattr(settings, 'SITE_URL', None) or settings.SITE_ORIGIN,
        'siteOwnerName': settings.SITE_OWNER_NAME,
        'siteOwnerNameEn': settings.SITE_OWNER_NAME_EN,
        'siteContactEmail': settings.SITE_CONTACT_EMAIL,
        'social': {
            'telegram': settings.AUTHOR_SOCIAL_TELEGRAM,
            'instagram': settings.AUTHOR_SOCIAL_INSTAGRAM,
            'tiktok': settings.AUTHOR_SOCIAL_TIKTOK,
            'twitch': settings.AUTHOR_SOCIAL_TWITCH,
            'youtube': settings.AUTHOR_SOCIAL_YOUTUBE,
            'discord': settings.AUTHOR_SOCIAL_DISCORD,
            'boosty': settings.AUTHOR_SOCIAL_BOOSTY,
        },
        'images': {
            'hero': _image_url(request, hero),
            'miniature': _image_url(request, miniature),
            'carousel': [u for x in carousel if (u := _image_url(request, x))],
            'photo': [u for x in photo if (u := _image_url(request, x))],
        },
    })
