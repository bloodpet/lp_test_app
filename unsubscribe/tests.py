import uuid
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy

from .models import *


class UnsubscribeHomeViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse_lazy('unsubscribe:home')

    def test_get_view(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class UnsubscribeFormViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse_lazy('unsubscribe:form', kwargs={'pk': uuid.uuid4().hex})

    def test_get_view(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class UnsubscribeUrlViewTestCase(TestCase):

    def setUp(self):
        self.detail_url = reverse_lazy('unsubscribe:url-detail', args=(uuid.uuid4().hex,))
        self.list_url = reverse_lazy('unsubscribe:url-list')

    def test_delete_404_view(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(404, response.status_code)

    def test_create_view(self):
        test_mail = 'test@example.com'
        response = self.client.post(self.list_url, data={'email': test_mail})
        self.assertEqual(201, response.status_code)
        self.assertEqual(1, UnsubscribeUrl.objects.count())
        instance_url = reverse_lazy('unsubscribe:url-detail', args=(response.data['id'],))
        response = self.client.delete(instance_url)
        self.assertEqual(204, response.status_code)
