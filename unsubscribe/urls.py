try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *
from rest_framework import routers

from unsubscribe.views import *

router = routers.DefaultRouter()
router.register(r'unsubscribe', UnsubscribeUrlView, base_name='url')
router.register(r'survey', UnsubscribeSurveyView, base_name='survey')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/$', UnsubscribeHomeView.as_view(), name='home'),
    url(r'^reason/$', reason_view, name='reason'),
    url(r'^form/(?P<pk>\S+)/$', UnsubscribeFormView.as_view(), name='form'),
]
