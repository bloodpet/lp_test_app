from django.contrib import admin

from .models import *


class UnsubscribeUrlAdmin(admin.ModelAdmin):
   list_display = ('email', 'id', 'is_used')


class UnsubscribeSurveyAdmin(admin.ModelAdmin):
   list_display = ('reason', 'email')


class UnsubscribeSurveyCountAdmin(admin.ModelAdmin):
   list_display = ('reason', 'count')


admin.site.register(UnsubscribeUrl, UnsubscribeUrlAdmin)
admin.site.register(UnsubscribeSurvey, UnsubscribeSurveyAdmin)
admin.site.register(UnsubscribeSurveyCount, UnsubscribeSurveyCountAdmin)
