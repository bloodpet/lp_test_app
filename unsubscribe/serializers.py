from rest_framework import serializers

from .models import *


class UnsubscribeUrlSerializer(serializers.ModelSerializer):
    form_url = serializers.URLField(read_only=True)

    class Meta:
        model = UnsubscribeUrl
        fields = ('form_url', 'id', 'email')

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'form_url': obj.form_url,
        }


class UnsubscribeSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnsubscribeSurvey
