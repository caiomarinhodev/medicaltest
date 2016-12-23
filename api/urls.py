from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^locations/$', views.LocationList.as_view(), name='location-list'),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view(),
        name='location-detail'),
    url(r'^accounts/$', views.AccountList.as_view(), name='account-list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='account-detail'),
    url(r'^actions/$', views.ActionList.as_view(), name='action-list'),
    url(r'^actions/(?P<pk>[0-9]+)/$', views.ActionDetail.as_view(), name='action-detail'),
    url(r'^admissions/$', views.AdmissionList.as_view(), name='admission-list'),
    url(r'^admissions/(?P<pk>[0-9]+)/$', views.AdmissionDetail.as_view(),
        name='admission-detail'),
    url(r'^appointments/$', views.AppointmentList.as_view(), name='appointment-list'),
    url(r'^appointments/(?P<pk>[0-9]+)/$', views.AppointmentDetail.as_view(),
        name='appointment-detail'),
    url(r'^hospitals/$', views.HospitalList.as_view(), name='hospital-list'),
    url(r'^hospitals/(?P<pk>[0-9]+)/$', views.HospitalDetail.as_view(),
        name='hospital-detail'),
    url(r'^medicalinfos/$', views.MedicalInfoList.as_view(), name='medicalinfo-list'),
    url(r'^medicalinfos/(?P<pk>[0-9]+)/$', views.MedicalInfoDetail.as_view(),
        name='medicalinfo-detail'),
    url(r'^medicaltests/$', views.MedicalTestList.as_view(), name='medicaltest-list'),
    url(r'^medicaltests/(?P<pk>[0-9]+)/$', views.MedicalTestDetail.as_view(),
        name='medicaltest-detail'),
    url(r'^messages/$', views.MessageList.as_view(), name='message-list'),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message-detail'),
    url(r'^notifications/$', views.NotificationList.as_view(), name='notification-list'),
    url(r'^notifications/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view(),
        name='notification-detail'),
    url(r'^prescriptions/$', views.PrescriptionList.as_view(), name='prescription-list'),
    url(r'^prescriptions/(?P<pk>[0-9]+)/$', views.PrescriptionDetail.as_view(),
        name='prescription-detail'),
    url(r'^profiles/$', views.ProfileList.as_view(), name='profile-list'),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view(), name='profile-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
