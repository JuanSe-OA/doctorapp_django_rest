from .serializers import PatientSerializer
from .models import Patient

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

# GET /api/patients --> Listar
# POST /api/patients --> Crear
# GET /api/patients/<id> --> Detalle
# PUT /api/patients/<id> --> Actualizar
# DELETE /api/patients/<id> --> Eliminar    
    
class ListPatientsView(ListAPIView,CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()   

    

class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


