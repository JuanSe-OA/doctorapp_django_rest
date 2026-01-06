DoctorApp - Medical Management API
DoctorApp es una solución de backend diseñada para digitalizar la interacción entre pacientes y profesionales de la salud. La plataforma centraliza la gestión de perfiles médicos, la disponibilidad de horarios y la reserva de citas en un entorno seguro y eficiente.

Arquitectura y Diseño
El proyecto sigue el patrón de diseño MVT (Model-View-Template) adaptado para servicios REST, separando la lógica de negocio de la presentación mediante el uso de serializadores avanzados.

Funcionalidades Principales
Gestión de Usuarios y Roles: Sistema de autenticación robusto con distinción entre personal médico y pacientes.

Perfiles Médicos Detallados: Administración de información profesional, especialidades y centros de atención.

Agendamiento de Citas: Motor de reservas que evita solapamientos y gestiona la disponibilidad en tiempo real.

Documentación Automática: Implementación de Swagger/Redoc para una fácil exploración y prueba de los endpoints de la API.

Filtros Avanzados: Capacidad de búsqueda de especialistas por categoría, ubicación o disponibilidad.

Stack Tecnológico
Framework Principal: Django.

API Toolkit: Django Rest Framework (DRF).

Lenguaje: Python.

Base de Datos: PostgreSQL.

Autenticación: JWT. 

Requisitos e Instalación
Clonar el repositorio: git clone https://github.com/JuanSe-OA/doctorapp_django_rest.git

Crear un entorno virtual: python -m venv venv

Activar el entorno e instalar dependencias: pip install -r requirements.txt

Ejecutar migraciones: python manage.py migrate

Iniciar el servidor: python manage.py runserver

Estructura del Proyecto
/users: Manejo de cuentas, login y permisos.

/doctors: Modelos y lógica específica para los profesionales de salud.

/appointments: Sistema de gestión de turnos y validación de horarios.

/api: Configuración de rutas y versionamiento de la API
