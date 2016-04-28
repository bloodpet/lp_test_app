from django.conf import settings

from .models import *


def unsubscribe_email(email):
    '''Unsubscribe given e-mail

    Add the call to the actual method where the email is unsubscribed.
    It would also be ideal to use celery here to delay the delete
    '''
    # For now, just mark the urls that correspond to *email* as used
    if getattr(settings, 'UNSUBSCRIBE_DELETE_USED', False):
        UnsubscribeUrl.objects.filter(email=email).delete()
    else:
        for unsubscribe_url in UnsubscribeUrl.objects.filter(email=email):
            unsubscribe_url.is_used = True
            unsubscribe_url.save()
