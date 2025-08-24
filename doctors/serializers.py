from attr import attrs
from rest_framework import serializers
from doctors.models import Doctor,DoctorAvailability,Department,MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be from the domain 'example.com'")
        return value
    
    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacations'] == True:
            raise serializers.ValidationError("Contact number must be at least 10 digits if the doctor is on vacations.")
        return super().validate(attrs)

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'