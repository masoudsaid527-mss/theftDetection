from django.db import models

from django.db import models


class Suspect(models.Model):
    genderChoices = [
        ('M','Male'),
        ('F','Female'),
    ]
    full_name = models.CharField(max_length =100)
    gender = models.CharField(max_length = 1, choices = genderChoices,default = 'm')
    age = models.IntegerField(default = 0)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.full_name


class Victim(models.Model):
    full_name =models.CharField(max_length = 100)
    genderChoices = [
        ('M','Male'),
        ('F','Female'),
    ]
    gender = models.CharField(max_length = 1, choices = genderChoices,default = 'M')
    age = models.IntegerField(default = 0)
    phone = models.CharField(max_length =20)
    address = models.CharField(max_length =100)

    def __str__(self):
        return self.full_name

class PoliceOfficer(models.Model):
    name = models.CharField(max_length = 100)
    badge_number = models.CharField(max_length = 100 ,unique = True)
    station = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)

    def __str__(self):
        return self.name    


class TheftCase(models.Model):
    case_status = [
        ('O','Open'),
        ('C','Closed'),
        ('F','Finished'),
        ('R','Resolved'),
    ]
    status = models.CharField(max_length = 1, choices = case_status,default = 'O')
    case_number = models.IntegerField()
    victim = models.ForeignKey(Victim,on_delete = models.CASCADE)
    suspect = models.ForeignKey(Suspect,on_delete = models.CASCADE)
    incident_date = models.DateField()
    location = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 20)
    assigned_officer = models.ForeignKey(PoliceOfficer,on_delete = models.SET_NULL,  null = True, blank =True)

    def __int__(self):
        return self.case_number

class StolenItem(models.Model):
    theft_case = models.ForeignKey(TheftCase,on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 1)
    values = models.IntegerField(default = 0)   

    def __str__(self):
        return self.item_name   


class PoliceCenter(models.Model):
    center_name = models.CharField(max_length = 100)
    office_name = models.CharField(max_length = 100)
    police_name = models.ForeignKey(PoliceOfficer,on_delete = models.CASCADE)

    def __str__(self):
        return self.center_name

class Witness(models.Model):
    theft_case = models.ForeignKey(TheftCase,on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20)
    statement = models.TextField()

    def __str__(self):
        return self.full_name  

class Evidence(models.Model):
    theft_case = models.ForeignKey(TheftCase,on_delete = models.CASCADE)
    description = models.TextField()
    date_collected = models.DateTimeField(auto_now_add = True)

    def __int__(self):
        return self.theft_case

class InvestigationReport(models.Model):
    theft_case = models.OneToOneField(TheftCase,on_delete = models.CASCADE)
    office_name = models.ForeignKey(PoliceOfficer,on_delete = models.SET_NULL, null=True, blank = True)
    report_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Report{self.theft_case}"   

class Notification(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.message

class History(models.Model):
    theft_case = models.ForeignKey(TheftCase,on_delete = models.CASCADE)
    caseaction = [
        ('u','Followed Up'),
        ('C','Closed'),
        ('F','Finished'),
    ]
    action = models.CharField(max_length = 1, choices = caseaction, default = 'U')
    perfomed_by = models.ForeignKey(Witness,on_delete = models.SET_NULL, null = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __int__(self):
        return self.theft_case






# Create your models here.


# Create your models here.
