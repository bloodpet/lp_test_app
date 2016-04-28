import uuid

from django.db import models
from django.core.urlresolvers import reverse_lazy

from unsubscribe.fields import UUIDField


class UnsubscribeUrl(models.Model):
    id = UUIDField(primary_key=True, max_length=32, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255)
    # Use for expiring links
    sent_ts = models.DateTimeField(auto_now_add=True)
    # For one-time use links w/ delayed cleanup
    is_used = models.BooleanField(default=False)

    @property
    def form_url(self):
        return reverse_lazy('unsubscribe:form', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse_lazy('unsubscribe:url-detail', args=(self.id,))


def generate_url(email):
    return UnsubscribeUrl.objects.create(email=email)
