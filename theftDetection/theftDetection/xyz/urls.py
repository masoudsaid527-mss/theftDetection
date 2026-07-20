from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),

    # Suspect
    path('suspects/', views.suspect_list),
    path('suspects/<int:id>/', views.suspect_detail),


    # Victim
    path('victims/', views.victim_list),
    path('victims/<int:id>/', views.victim_detail),


    # Police Officer
    path('officers/', views.officer_list),
    path('officers/<int:id>/', views.officer_detail),


    # Theft Case
    path('cases/', views.case_list),
    path('cases/<int:id>/', views.case_detail),


    # Stolen Items
    path('items/', views.stolen_item_list),
    path('items/<int:id>/', views.stolen_item_detail),


    # Police Center
    path('centers/', views.police_center_list),
    path('centers/<int:id>/', views.police_center_detail),


    # Witness
    path('witnesses/', views.witness_list),
    path('witnesses/<int:id>/', views.witness_detail),


    # Evidence
    path('evidence/', views.evidence_list),
    path('evidence/<int:id>/', views.evidence_detail),


    # Investigation Report
    path('reports/', views.report_list),
    path('reports/<int:id>/', views.report_detail),


    # Notifications
    path('notifications/', views.notification_list),
    path('notifications/<int:id>/', views.notification_detail),


    # History
    path('history/', views.history_list),
    path('history/<int:id>/', views.history_detail),

]