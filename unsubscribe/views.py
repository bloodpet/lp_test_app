from django.views.generic import TemplateView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from .models import *
from .serializers import *


class UnsubscribeHomeView(TemplateView):
    template_name = 'unsubscribe/home.html'


class UnsubscribeFormView(TemplateView):
    template_name = 'unsubscribe/form.html'


class UnsubscribeUrlView(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = UnsubscribeUrl.objects.all()
    serializer_class = UnsubscribeUrlSerializer

    def create0(self, *args):
        ret = super(UnsubscribeUrlView, self).create(*args)
        print ret
        return ret
