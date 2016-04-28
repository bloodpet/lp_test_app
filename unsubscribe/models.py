import uuid

from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from unsubscribe.fields import UUIDField

REASON_CHOICES = (
    ('STOP', 'I no longer want to receive these emails'),
    ('NOSIGNUP', 'I never signed up for this mailing list'),
    ('INAPPROPRIATE', 'The emails are inappropriate'),
    ('SPAM', 'The emails are spam and should be reported'),
    ('OTHER', 'Other'),
)
REASONS = dict(REASON_CHOICES)


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


class UnsubscribeSurvey(models.Model):
    email = models.EmailField(max_length=255)
    reason = models.CharField(max_length=32, choices=REASON_CHOICES)
    is_other = models.BooleanField(default=False)
    other_reason = models.TextField()


class UnsubscribeSurveyCount(models.Model):
    reason = models.CharField(max_length=32, choices=REASON_CHOICES)
    count = models.IntegerField(default=0)


def generate_url(email):
    return UnsubscribeUrl.objects.create(email=email)

@receiver(post_save, sender=UnsubscribeSurvey)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        cnt, _ = UnsubscribeSurveyCount.objects.get_or_create(reason=instance.reason)
        cnt.count += 1
        cnt.save()
