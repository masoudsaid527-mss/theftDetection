from rest_framework import serializers
from .models import *


# ==========================
# Suspect Serializer
# ==========================
class SuspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suspect
        fields = "__all__"


# ==========================
# Victim Serializer
# ==========================
class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = "__all__"


# ==========================
# Police Officer Serializer
# ==========================
class PoliceOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOfficer
        fields = "__all__"


# ==========================
# Theft Case Serializer
# ==========================
class TheftCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheftCase
        fields = "__all__"


# ==========================
# Stolen Item Serializer
# ==========================
class StolenItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StolenItem
        fields = "__all__"


# ==========================
# Police Center Serializer
# ==========================
class PoliceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceCenter
        fields = "__all__"


# ==========================
# Witness Serializer
# ==========================
class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witness
        fields = "__all__"


# ==========================
# Evidence Serializer
# ==========================
class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = "__all__"


# ==========================
# Investigation Report Serializer
# ==========================
class InvestigationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationReport
        fields = "__all__"


# ==========================
# Notification Serializer
# ==========================
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


# ==========================
# History Serializer
# ==========================
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"