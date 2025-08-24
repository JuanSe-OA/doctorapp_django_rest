from rest_framework import serializers
from patients.models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate_contact_number(self, value):
        if len(value) < 15:
            raise serializers.ValidationError("Contact number must be at least 10 digits.")
        return value
    
    def validate_address(self, attrs):
        if attrs is None or attrs.strip() == "":
            raise serializers.ValidationError("Address cannot be empty.")

    def validate_date_of_birth(self, value):
        if value is None:
            raise serializers.ValidationError("Date of birth cannot be empty.")
        return value

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'