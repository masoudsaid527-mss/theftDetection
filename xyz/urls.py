from django.urls import path
from . import views

urlpatterns = [
    # Root
    path('', views.api_root, name='api-root'),

    # Suspects
    path('suspects/', views.Suspect, name='suspects-list'),
    path('suspects/<int:id>/', views.Suspect, name='suspects-detail'),

    # Victims
    path('victims/', views.Victim, name='victims-list'),
    path('victims/<int:id>/', views.Victim, name='victims-detail'),

    # Police Officers
    path('police_officers/', views.PoliceOfficer, name='police-officers-list'),
    path('police_officers/<int:id>/', views.PoliceOfficer, name='police-officers-detail'),

    # Theft Cases
    path('theft_cases/', views.TheftCase, name='theft-cases-list'),
    path('theft_cases/<int:id>/', views.TheftCase, name='theft-cases-detail'),

    # Stolen Items
    path('stolen_items/', views.StolenItem, name='stolen-items-list'),
    path('stolen_items/<int:id>/', views.StolenItem, name='stolen-items-detail'),

    # Police Centers
    path('police_centers/', views.PoliceCenter, name='police-centers-list'),
    path('police_centers/<int:id>/', views.PoliceCenter, name='police-centers-detail'),

    # History
    path('history/', views.History, name='history-list'),
    path('history/<int:id>/', views.History, name='history-detail'),

    # Witnesses
    path('witnesses/', views.Witness, name='witnesses-list'),
    path('witnesses/<int:id>/', views.Witness, name='witnesses-detail'),

    # Evidence
    path('evidence/', views.Evidence, name='evidence-list'),
    path('evidence/<int:id>/', views.Evidence, name='evidence-detail'),

    # Investigation Reports
    path('investigation_reports/', views.InvestigationReport, name='investigation-reports-list'),
    path('investigation_reports/<int:id>/', views.InvestigationReport, name='investigation-reports-detail'),

    # Notifications
    path('notifications/', views.Notification, name='notifications-list'),
    path('notifications/<int:id>/', views.Notification, name='notifications-detail'),
]