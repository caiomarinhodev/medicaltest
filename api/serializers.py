from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Profile, Account, Action, Appointment, Message, Notification, Admission, \
    Prescription, MedicalInfo, MedicalTest, Hospital, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'city', 'zip', 'state', 'country', 'address')


class HospitalSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Hospital
        fields = ('id', 'name', 'location', 'phone')


class ProfileSerializer(serializers.ModelSerializer):
    prefHospital = HospitalSerializer()

    class Meta:
        model = Profile
        fields = (
            'id',
            'firstname',
            'lastname',
            'insurance',
            'emergencyContactName',
            'emergencyContactNumber',
            'sex',
            'birthday',
            'phone',
            'allergies',
            'created',
            'prefHospital',
        )


class AccountSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ('id', 'role', 'profile', 'user')


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = AccountSerializer()
    patient = AccountSerializer()
    hospital = HospitalSerializer()

    class Meta:
        model = Appointment
        fields = ('id',
                  'doctor',
                  'patient',
                  'description',
                  'status',
                  'hospital',
                  'startTime',
                  'endTime'
                  )


class ActionSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Action
        fields = ('id',
                  'type',
                  'timePerformed',
                  'description',
                  'account'
                  )


class MessageSerializer(serializers.ModelSerializer):
    target = AccountSerializer()
    sender = AccountSerializer()

    class Meta:
        model = Message
        fields = (
            'id',
            'target',
            'sender',
            'header',
            'body',
            'sender_deleted',
            'target_deleted',
            'timestamp'
        )


class NotificationSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Notification
        fields = (
            'id',
            'account',
            'message',
            'read',
            'sent_timestamp',
            'read_timestamp'
        )


class AdmissionSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    hospital = HospitalSerializer()

    class Meta:
        model = Admission
        fields = (
            'id',
            'account',
            'timestamp',
            'discharged_timestamp',
            'reason',
            'description',
            'hospital',
            'active'
        )


class PrescriptionSerializer(serializers.ModelSerializer):
    patient = AccountSerializer()
    doctor = AccountSerializer()

    class Meta:
        model = Prescription
        fields = (
            'id',
            'patient',
            'doctor',
            'date',
            'medication',
            'strength',
            'instruction',
            'refill',
            'active'
        )


class MedicalInfoSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = MedicalInfo
        fields = (
            'id',
            'account',
            'bloodType',
            'allergy',
            'alzheimer',
            'asthma',
            'diabetes',
            'stroke',
            'comments'
        )


class MedicalTestSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()
    doctor = AccountSerializer()
    patient = AccountSerializer()

    class Meta:
        model = MedicalTest
        fields = (
            'id',
            'name',
            'date',
            'hospital',
            'description',
            'doctor',
            'patient',
            'private',
            'completed',
            'image1'
        )
