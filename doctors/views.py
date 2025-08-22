from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# GET /api/doctors --> Listar
# POST /api/doctors --> Crear
# GET /api/doctors/<id> --> Detalle
# PUT /api/doctors/<id> --> Actualizar
# DELETE /api/doctors/<id> --> Eliminar    

    
class ListDoctorsView(ListAPIView,CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()   

    

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
