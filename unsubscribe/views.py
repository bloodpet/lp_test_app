from django.views.generic import TemplateView, DetailView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .tasks import *


class UnsubscribeHomeView(TemplateView):
    template_name = 'unsubscribe/home.html'


class UnsubscribeFormView(DetailView):
    template_name = 'unsubscribe/form.html'
    model = UnsubscribeUrl


class UnsubscribeUrlView(CreateModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UnsubscribeUrl.objects.all()
    serializer_class = UnsubscribeUrlSerializer

    def update(self, request, pk, **kwargs):
        url = UnsubscribeUrl.objects.get(pk=pk)
        if url.email != request.data['email']:
            return Response({'message': 'Bad Request'}, status.HTTP_400_BAD_REQUEST)
        unsubscribe_email(url.email)
        return Response({'message': 'Good'})
