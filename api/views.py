from django.contrib.auth.models import User

# Create your views here.


# ViewSets define the view behavior.
from rest_framework import generics

from api.serializers import UserSerializer, LocationSerializer, AccountSerializer, \
    ActionSerializer, AdmissionSerializer, AppointmentSerializer, HospitalSerializer, \
    MedicalInfoSerializer, MedicalTestSerializer, MessageSerializer, NotificationSerializer, \
    PrescriptionSerializer, ProfileSerializer
from app.models import Location, Account, Action, Admission, Appointment, Hospital, \
    MedicalInfo, MedicalTest, Message, Notification, Prescription, Profile


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class AdmissionList(generics.ListCreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AdmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class HospitalList(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class MedicalInfoList(generics.ListCreateAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = MedicalInfoSerializer


class MedicalInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalInfo.objects.all()
    serializer_class = MedicalInfoSerializer


class MedicalTestList(generics.ListCreateAPIView):
    queryset = MedicalTest.objects.all()
    serializer_class = MedicalTestSerializer


class MedicalTestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalTest.objects.all()
    serializer_class = MedicalTestSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class PrescriptionList(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
