from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *
from django.contrib.auth.models import User


# ==========================
# Generic CRUD Function
# ==========================

def crud_list(request, model, serializer_class):

    if request.method == "GET":

        objects = model.objects.all()

        serializer = serializer_class(
            objects,
            many=True
        )

        return Response(serializer.data)


    elif request.method == "POST":

        serializer = serializer_class(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors)



def crud_detail(request, model, serializer_class, id):

    try:

        obj = model.objects.get(id=id)

    except model.DoesNotExist:

        return Response(
            {"error":"Data not found"},
            status=404
        )


    if request.method == "GET":

        serializer = serializer_class(obj)

        return Response(serializer.data)



    elif request.method == "PUT":

        serializer = serializer_class(
            obj,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


        return Response(serializer.errors)



    elif request.method == "DELETE":

        obj.delete()

        return Response(
            {"message":"Deleted successfully"}
        )



# ==========================
# Suspect
# ==========================

@api_view(['GET','POST'])
def suspect_list(request):

    return crud_list(
        request,
        Suspect,
        SuspectSerializer
    )


@api_view(['GET','PUT','DELETE'])
def suspect_detail(request,id):

    return crud_detail(
        request,
        Suspect,
        SuspectSerializer,
        id
    )



# ==========================
# Victim
# ==========================

@api_view(['GET','POST'])
def victim_list(request):

    return crud_list(
        request,
        Victim,
        VictimSerializer
    )


@api_view(['GET','PUT','DELETE'])
def victim_detail(request,id):

    return crud_detail(
        request,
        Victim,
        VictimSerializer,
        id
    )



# ==========================
# Police Officer
# ==========================

@api_view(['GET','POST'])
def officer_list(request):

    return crud_list(
        request,
        PoliceOfficer,
        PoliceOfficerSerializer
    )


@api_view(['GET','PUT','DELETE'])
def officer_detail(request,id):

    return crud_detail(
        request,
        PoliceOfficer,
        PoliceOfficerSerializer,
        id
    )



# ==========================
# Theft Case
# ==========================

@api_view(['GET','POST'])
def case_list(request):

    return crud_list(
        request,
        TheftCase,
        TheftCaseSerializer
    )


@api_view(['GET','PUT','DELETE'])
def case_detail(request,id):

    return crud_detail(
        request,
        TheftCase,
        TheftCaseSerializer,
        id
    )



# ==========================
# Stolen Item
# ==========================

@api_view(['GET','POST'])
def stolen_item_list(request):

    return crud_list(
        request,
        StolenItem,
        StolenItemSerializer
    )


@api_view(['GET','PUT','DELETE'])
def stolen_item_detail(request,id):

    return crud_detail(
        request,
        StolenItem,
        StolenItemSerializer,
        id
    )



# ==========================
# Police Center
# ==========================

@api_view(['GET','POST'])
def police_center_list(request):

    return crud_list(
        request,
        PoliceCenter,
        PoliceCenterSerializer
    )


@api_view(['GET','PUT','DELETE'])
def police_center_detail(request,id):

    return crud_detail(
        request,
        PoliceCenter,
        PoliceCenterSerializer,
        id
    )



# ==========================
# Witness
# ==========================

@api_view(['GET','POST'])
def witness_list(request):

    return crud_list(
        request,
        Witness,
        WitnessSerializer
    )


@api_view(['GET','PUT','DELETE'])
def witness_detail(request,id):

    return crud_detail(
        request,
        Witness,
        WitnessSerializer,
        id
    )



# ==========================
# Evidence
# ==========================

@api_view(['GET','POST'])
def evidence_list(request):

    return crud_list(
        request,
        Evidence,
        EvidenceSerializer
    )


@api_view(['GET','PUT','DELETE'])
def evidence_detail(request,id):

    return crud_detail(
        request,
        Evidence,
        EvidenceSerializer,
        id
    )



# ==========================
# Investigation Report
# ==========================

@api_view(['GET','POST'])
def report_list(request):

    return crud_list(
        request,
        InvestigationReport,
        InvestigationReportSerializer
    )


@api_view(['GET','PUT','DELETE'])
def report_detail(request,id):

    return crud_detail(
        request,
        InvestigationReport,
        InvestigationReportSerializer,
        id
    )



# ==========================
# Notification
# ==========================

@api_view(['GET','POST'])
def notification_list(request):

    return crud_list(
        request,
        Notification,
        NotificationSerializer
    )


@api_view(['GET','PUT','DELETE'])
def notification_detail(request,id):

    return crud_detail(
        request,
        Notification,
        NotificationSerializer,
        id
    )



# ==========================
# History
# ==========================

@api_view(['GET','POST'])
def history_list(request):

    return crud_list(
        request,
        History,
        HistorySerializer
    )


@api_view(['GET','PUT','DELETE'])
def history_detail(request,id):

    return crud_detail(
        request,
        History,
        HistorySerializer,
        id
    )

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db import IntegrityError

@api_view(['POST'])
def register(request):
    data = request.data

    # Frontend payload (register.js):
    # { full_name, email, phone, national_id, password, confirm_password, role }
    full_name = data.get('full_name') or data.get('fullname')
    email = (data.get('email') or '').strip().lower()
    phone = (data.get('phone') or '').strip()
    national_id = (data.get('national_id') or '').strip()
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    role = data.get('role')

    # Backend also supports older payload shapes
    username = data.get('username')

    if not full_name or not str(full_name).strip():
        return Response({'error': 'full name is required'}, status=400)
    if not email:
        return Response({'error': 'email is required'}, status=400)
    if not phone:
        return Response({'error': 'phone is required'}, status=400)
    if not national_id:
        return Response({'error': 'national ID is required'}, status=400)

    if not username:
        if isinstance(email, str) and '@' in email:
            username = email

    if not username:
        return Response({'error': 'username is required (or provide email to derive it)'}, status=400)
    if not password:
        return Response({'error': 'password is required'}, status=400)

    # If frontend provides confirm_password, enforce it.
    if confirm_password is not None and confirm_password != password:
        return Response({'error': 'passwords do not match'}, status=400)

    if User.objects.filter(username=username).exists() or User.objects.filter(email__iexact=email).exists():
        return Response({'error': 'An account with this email already exists'}, status=400)

    if role not in dict(Profile.ROLE_CHOICES):
        return Response({'error': 'A valid account type is required'}, status=400)

    # Create user
    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=str(full_name).strip(),
        )
    except IntegrityError:
        return Response({'error': 'An account with this email already exists'}, status=400)

    # Create Profile for role-based redirects
    safe_role = role
    Profile.objects.create(user=user, role=safe_role)

    # Optional: create/update domain models (keep minimal, no structure change)
    # Currently the frontend doesn't use these models for auth.
    if safe_role == 'citizen' and isinstance(national_id, str) and national_id.strip():
        Victim.objects.get_or_create(
            national_id=national_id.strip(),
            defaults={
                'full_name': full_name or user.username,
                'phone': phone or '',
                'address': '',
            },
        )

    return Response({'message': 'Registration successful.'}, status=201)



@api_view(['POST'])
def login(request):
    data = request.data

    # Support both payload shapes:
    # 1) {username, password}
    # 2) {email, password}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not password:
        return Response({'error': 'password is required'}, status=400)

    user = None

    if username:
        user = authenticate(username=username, password=password)

    # If username auth failed or username not provided, try email auth
    if user is None and email:
        try:
            user_obj = User.objects.get(email=email)
            if user_obj.check_password(password):
                user = user_obj
        except User.DoesNotExist:
            user = None

    if user is not None:
        # chukua role ya user
        role = None
        if hasattr(user, 'profile'):
            role = user.profile.role
            if role == 'aker':
                role = 'policymaker'

        return Response({
            'message': 'Login successful',
            'user': {
                'username': user.username,
                'email': user.email,
                'role': role,
            }
        }, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
