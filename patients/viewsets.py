from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Patient, MedicalRecord
from .serializers import MedicalRecordSerializer


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = Patient.objects.all()

    @action(methods=["GET"], detail=True, url_path='medical-record')
    def get_medical_record(self, request, pk):
        patient = self.get_object()
        medical_records = MedicalRecord.objects.filter(patient=patient)
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)
    
    @action(methods=["POST"], detail=True, url_path='add-medical-record')
    def add_medical_record(self, request, pk):
        patient = self.get_object()
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=patient)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    
