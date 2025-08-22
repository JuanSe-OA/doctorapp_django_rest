from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import AppointmentSerializer, MedicalNoteSerializer
from bookings.models import Appointment,MedicalNote

class ListAppointmentView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de citas medicas programadas
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()