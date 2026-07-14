from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


def api_root(request):
    return JsonResponse({
        'message': 'Theft Detection system API',
        'endpoints': {
            'suspects': '/api/suspects/',
            'victims': '/api/victims/',
            'police_officers': '/api/police_officers/',
            'theftCases': '/api/theftCases/',
            'stolenItems': '/api/stolenItems/',
            'policeCenter': '/api/policeCenter/',
            'history': '/api/history/',
            'witness': '/api/witness/',
            'evidences': '/api/evidences/',
            'investigationReports': '/api/investigationReports/',
            'notifications': '/api/notifications/',
        }
    });

def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'DELETE', 'PUT'])
    @authentication_classes([])  # Bypasses Session Auth CSRF enforcement
    @csrf_exempt                 # Must live beneath @api_view to take effect
    def api(request, id=None):
        
        # --- GET METHOD ---
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, many=False) 
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many=True)
                return Response(serializer.data)

        # --- POST METHOD ---
        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # --- DELETE METHOD ---
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    instance.delete()
                    return Response({'message': 'Deleted Successfully'}, status=status.HTTP_200_OK)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Method DELETE requires an ID in the URL'}, status=status.HTTP_400_BAD_REQUEST)

        # --- PUT METHOD ---
        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Method PUT requires an ID in the URL'}, status=status.HTTP_400_BAD_REQUEST)

        # Fallback return statement to prevent Django from crashing if an unhandled state occurs
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return api

# Dynamic view mapping
Suspect = generic_api(Suspect, SuspectSerializer)
Victim = generic_api(Victim, VictimSerializer)
PoliceOfficer = generic_api(PoliceOfficer, PoliceOfficerSerializer)
TheftCase = generic_api(TheftCase, TheftCaseSerializer)
StolenItem = generic_api(StolenItem, StolenItemSerializer)
PoliceCenter = generic_api(PoliceCenter, PoliceCenterSerializer)
History = generic_api(History, HistorySerializer)
Witness = generic_api(Witness, WitnessSerializer)
Evidence = generic_api(Evidence, EvidenceSerializer)
InvestigationReport = generic_api(InvestigationReport, InvestigationReportSerializer)
Notification = generic_api(Notification, NotificationSerializer)

# Create your views here.
