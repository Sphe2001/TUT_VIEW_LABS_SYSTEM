from rest_framework import serializers
from .models import Laboratory, Application, Computer, Bookings


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['id', 'building_no', 'lab_name',
                  'number_of_pcs', 'is_available']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'app_name', 'version', 'vendor', 'icon']


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ['id', 'computer_name', 'laboratory',
                  'available_applications', 'is_available']


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id', 'user', 'lab', 'start_time', 'end_time']
