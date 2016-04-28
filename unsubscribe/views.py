from django.views.generic import TemplateView, DetailView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import *
from .serializers import *
from .tasks import *


class UnsubscribeHomeView(TemplateView):
    template_name = 'unsubscribe/home.html'


class UnsubscribeFormView(DetailView):
    template_name = 'unsubscribe/form.html'
    model = UnsubscribeUrl

    def get_context_data(self, **kwargs):
        context = super(UnsubscribeFormView, self).get_context_data(**kwargs)
        context['reasons'] = REASON_CHOICES
        return context


class UnsubscribeUrlView(CreateModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UnsubscribeUrl.objects.all()
    serializer_class = UnsubscribeUrlSerializer

    def update(self, request, pk, **kwargs):
        url = UnsubscribeUrl.objects.get(pk=pk)
        if url.email != request.data['email']:
            return Response({'message': 'Bad Request'}, status.HTTP_400_BAD_REQUEST)
        unsubscribe_email(url.email)
        return Response({'message': 'Good'})


class UnsubscribeSurveyView(CreateModelMixin, GenericViewSet):
    queryset = UnsubscribeSurvey.objects.all()


@api_view(http_method_names=['GET'])
def reason_view(request):
    choices = []
    for reason in REASON_CHOICES:
        choices.append({'value': reason[0], 'label': reason[1]})
    return Response(choices)
