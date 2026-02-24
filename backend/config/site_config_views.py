from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def site_config(request):
    return JsonResponse({
        'authorName': settings.AUTHOR_NAME,
        'authorPseudonym': settings.AUTHOR_PSEUDONYM,
        'authorEmail': settings.AUTHOR_EMAIL,
        'siteUrl': settings.SITE_URL,
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
    })
