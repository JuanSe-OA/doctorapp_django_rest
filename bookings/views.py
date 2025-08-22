from .serializers import AppointmentSerializer, MedicalNoteSerializer
from bookings.models import Appointment,MedicalNote
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

class ListAppointmentsView(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer.AppointmentSerializer

class DetailAppointmentView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer.AppointmentSerializer

class ListMedicalNotesView(ListAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer.MedicalNoteSerializer

class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer.MedicalNoteSerializer
