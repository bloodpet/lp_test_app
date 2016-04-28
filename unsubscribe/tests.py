import uuid
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from rest_framework.test import APISimpleTestCase

from .models import *


class UnsubscribeHomeViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse_lazy('unsubscribe:home')

    def test_get_view(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class UnsubscribeFormViewTestCase(TestCase):

    def test_get_view(self):
        obj = UnsubscribeUrl.objects.create(email='test-get@example.com')
        url = reverse_lazy('unsubscribe:form', kwargs={'pk': obj.pk})
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        UnsubscribeUrl.objects.all().delete()


class UnsubscribeUrlViewTestCase(APISimpleTestCase):

    def setUp(self):
        self.detail_url = reverse_lazy('unsubscribe:url-detail', args=(uuid.uuid4().hex,))
        self.list_url = reverse_lazy('unsubscribe:url-list')

    def test_delete_404_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(404, response.status_code)

    def test_create_view(self):
        test_mail = 'test-create@example.com'
        response = self.client.post(self.list_url, data={'email': test_mail})
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, UnsubscribeUrl.objects.filter(email=test_mail).count())
        instance_url = reverse_lazy('unsubscribe:url-detail', args=(response.data['id'],))
        response = self.client.delete(instance_url)
        self.assertEqual(204, response.status_code)

    def test_confirm_view(self):
        obj = UnsubscribeUrl.objects.create(email='test@example.com')
        url = reverse_lazy('unsubscribe:url-detail', kwargs={'pk': obj.pk})
        response = self.client.put(url, data={'email': obj.email})
        self.assertEqual(200, response.status_code)
        response = self.client.put(url, data={'email': 'fake email'})
        self.assertEqual(400, response.status_code)
