from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import (
    DetailDepartmentView, DetailDoctorView, ListDepartmentView,
    ListMedicalNoteView,ListDoctorAvailabilityView, DetailDoctorAvailabilityView,
    DetailMedicalNoteView
)
from .viewsets import DoctorViewSet



router = DefaultRouter()
router.register('doctors', DoctorViewSet)
urlpatterns = [
    path('doctors/<int:pk>/', DetailDoctorView.as_view()),
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:pk>/', DetailDepartmentView.as_view()),
    path('medical-notes/', ListMedicalNoteView.as_view()),
    path('doctor-availability/', ListDoctorAvailabilityView.as_view()),
    path('doctor-availability/<int:pk>/', DetailDoctorAvailabilityView.as_view()),
    path('medical-notes/<int:pk>/', DetailMedicalNoteView.as_view()),

] + router.urls
