from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class SuspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suspect
        fields = '__all__'

class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = '__all__'

class TheftCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftCase
        fields = '__all__'

class StolenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StolenItem
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class PoliceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceCenter
        fields = '__all__'

class PoliceOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOfficer
        fields = '__all__'

class InvestigationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationReport
        fields = '__all__'

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'

class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witness
        fields = '__all__'
