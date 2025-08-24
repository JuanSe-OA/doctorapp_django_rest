from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


    @action(methods=["POST"], detail=True, url_path='set-on-vacations')
    def set_on_vacations(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacations = True 
        doctor.save()
        return Response({"status": "El doctor ha sido puesto en vacaciones."})
    
    @action(methods=["POST"], detail=True, url_path='set-off-vacations')
    def set_off_vacations(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacations = False 
        doctor.save()
        return Response({"status": "El doctor ha sido puesto en servicio."})
