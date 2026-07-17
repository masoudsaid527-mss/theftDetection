from django.db import models
from django.contrib.auth.models import User


# ==========================
# Suspect
# ==========================

class Suspect(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name


# ==========================
# Victim (Citizen)
# ==========================

class Victim(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    national_id = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name



# ==========================
# Police Officer
# ==========================

class PoliceOfficer(models.Model):
    name = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=50, unique=True)
    station = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# ==========================
# Police Center
# ==========================

class PoliceCenter(models.Model):

    center_name = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100)

    police_officer = models.ForeignKey(
        PoliceOfficer,
        on_delete=models.CASCADE,
        related_name="centers"
    )

    def __str__(self):
        return self.center_name


# ==========================
# Theft Case
# ==========================

class TheftCase(models.Model):

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'Investigating'),
        ('R', 'Resolved'),
        ('C', 'Closed'),
    ]

    case_number = models.CharField(max_length=30, unique=True)

    victim = models.ForeignKey(
        Victim,
        on_delete=models.CASCADE,
        related_name="cases"
    )

    suspect = models.ForeignKey(
        Suspect,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cases"
    )

    incident_date = models.DateField()

    reported_at = models.DateTimeField()

    location = models.CharField(max_length=200)

    description = models.TextField()

    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='P'
    )

    assigned_officer = models.ForeignKey(
        PoliceOfficer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_cases"
    )

    def __int__(self):
        return self.case_number


# ==========================
# Stolen Item
# ==========================

class StolenItem(models.Model):

    theft_case = models.ForeignKey(
        TheftCase,
        on_delete=models.CASCADE,
        related_name="stolen_items"
    )

    item_name = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField(default=1)

    value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.item_name

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    ROLE_CHOICES=(

        ('citizen','Citizen'),

        ('police','Police'),

        ('admin','Admin'),

        ('policymaker','Policy Maker'),

        # Backward compatible typo (if any old rows exist)
        ('aker','Aker'),

    )


    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


    role=models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )
# ==========================
# Witness
# ==========================

class Witness(models.Model):

    theft_case = models.ForeignKey(
        TheftCase,
        on_delete=models.CASCADE,
        related_name="witnesses"
    )

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    statement = models.TextField()

    def __str__(self):
        return self.full_name


# ==========================
# Evidence
# ==========================

class Evidence(models.Model):

    theft_case = models.ForeignKey(
        TheftCase,
        on_delete=models.CASCADE,
        related_name="evidence"
    )

    description = models.TextField()

    date_collected = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Evidence - {self.theft_case.case_number}"


# ==========================
# Investigation Report
# ==========================

class InvestigationReport(models.Model):

    theft_case = models.OneToOneField(
        TheftCase,
        on_delete=models.CASCADE,
        related_name="investigation_report"
    )

    officer = models.ForeignKey(
        PoliceOfficer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    report = models.TextField(default="")

    report_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Report - {self.theft_case.case_number}"


# ==========================
# Notification
# ==========================

class Notification(models.Model):
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.message[:50]


# ==========================
# History
# ==========================

class History(models.Model):

    ACTION_CHOICES = [
        ('Followed Up', 'Followed Up'),
        ('Closed', 'Closed'),
        ('Finished', 'Finished'),
    ]

    theft_case = models.ForeignKey(
        TheftCase,
        on_delete=models.CASCADE,
        related_name="history"
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES
    )

    performed_by = models.ForeignKey(
        PoliceOfficer,
        on_delete=models.SET_NULL,
        null=True
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.action} - {self.theft_case.case_number}"