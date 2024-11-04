from rest_framework import generics
from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentCourseSerializer

from .serializers import UserRegisterSerializer

from rest_framework.decorators import api_view

#Para ver la lista de usuarios en postman
from .serializers import UserListSerializer
from django.contrib.auth import get_user_model

#TOKEN
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission


#IMPORTS MODELS
from .models import Rol
from .models import Permission
from .models import User
from .models import Student
from .models import Teacher
from .models import Member
from .models import Partnership
from .models import Graduated
from .models import Administrative_Staff
from .models import Cleaning_Staff
from .models import Maintenance_Staff
from .models import Security_Staff
from .models import SoccerField_Reservation
from .models import Coworking_Reservation
from .models import Salon_Reservation
from .models import Early_Exit_Permission
from .models import Meeting_Request_Permission
from .models import Course
from .models import Registration
from .models import Reservation
from .models import Permission_Slip
from .models import Role_Permission

#IMPORTS SERIALIZERS
from .serializers import RolSerializer
from .serializers import PermissionSerializer
from .serializers import UserSerializer
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import MemberSerializer
from .serializers import PartnershipSerializer
from .serializers import GraduatedSerializer
from .serializers import Administrative_StaffSerializer
from .serializers import Cleaning_StaffSerializer
from .serializers import Maintenance_StaffSerializer
from .serializers import Security_StaffSerializer
from .serializers import SoccerField_ReservationSerializer
from .serializers import Coworking_ReservationSerializer
from .serializers import Salon_ReservationSerializer
from .serializers import Early_Exit_PermissionSerializer
from .serializers import Meeting_Request_PermissionSerializer
from .serializers import CourseSerializer
from .serializers import RegistrationSerializer
from .serializers import ReservationSerializer
from .serializers import Permission_SlipSerializer
from .serializers import Role_PermissionSerializer


#VISTA REGISTRO DE USUARIOS TABLA DE DJANGO
User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAuthenticated]

class IsAdministrator (BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Administrador").exists()

class IsProfesor (BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Profesor").exists()

class IsEstudiante (BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name = "Estudiante").exists()


#LISTA DE USUARIOS
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]  #Requiere autenticación con token


#/////////////////// 1. Principales ///////////////////#

#Métodos roles
class RolListCreate(generics.ListCreateAPIView):
    queryset = Rol.objects.all() #Define el conjunto de datos que se utilizarán (todas las recetas)
    serializer_class = RolSerializer #Especifica el serializer para convertir los datos a JSON
    permission_classes = [IsAuthenticated]  #Para proteger esta vista

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
    
#Métodos Permissions
class PermissionListCreate(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    #permission_classes = [IsAuthenticated]

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    #permission_classes = [IsAuthenticated]
    
#Métodos Users
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

#Métodos Students
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 
    #permission_classes = [AllowAny]  #Permitir acceso a todos sin autenticación
    permission_classes = [IsAuthenticated]  # solo estudiantes con permiso para ver contenido

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  
    permission_classes = [IsAuthenticated, IsAdministrator] #Solo el administrador puede editar o eliminar estudiantes

#Métodos Teachers
class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos 

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 
    permission_classes = [IsAuthenticated, IsAdministrator] 
    
#Métodos Team_Members
class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos 

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]      

#Métodos Partnerships
class PartnershipListCreate(generics.ListCreateAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer 
    
class PartnershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partnership.objects.all()
    serializer_class = PartnershipSerializer

#Métodos Graduated_Students
class GraduatedListCreate(generics.ListCreateAPIView):
    queryset = Graduated.objects.all()
    serializer_class = GraduatedSerializer 
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos

class GraduatedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Graduated.objects.all()
    serializer_class = GraduatedSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]  
    
    
#/////////////////// 2. Relación Uno a Uno ///////////////////#

#Métodos Administrative_Staff
class Administrative_StaffListCreate(generics.ListCreateAPIView):
    queryset = Administrative_Staff.objects.all()
    serializer_class = Administrative_StaffSerializer 
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos 

class Administrative_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrative_Staff.objects.all()
    serializer_class = Administrative_StaffSerializer 
    permission_classes = [IsAuthenticated, IsAdministrator]     

#Métodos Cleaning_Staff
class Cleaning_StaffListCreate(generics.ListCreateAPIView):
    queryset = Cleaning_Staff.objects.all()
    serializer_class = Cleaning_StaffSerializer
    permission_classes = [AllowAny]     

class Cleaning_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cleaning_Staff.objects.all()
    serializer_class = Cleaning_StaffSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]     
    
#Métodos Maintenance_Staff
class Maintenance_StaffListCreate(generics.ListCreateAPIView):
    queryset = Maintenance_Staff.objects.all()
    serializer_class = Maintenance_StaffSerializer 
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos

class Maintenance_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maintenance_Staff.objects.all()
    serializer_class = Maintenance_StaffSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]  

#Métodos Security_Staff
class Security_StaffListCreate(generics.ListCreateAPIView):
    queryset = Security_Staff.objects.all()
    serializer_class = Security_StaffSerializer 
    permission_classes = [AllowAny]  #Permitir acceso a todos verlos

class Security_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security_Staff.objects.all()
    serializer_class = Security_StaffSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]  


#/////////////////// 3. Relación uno a muchos ///////////////////#

#Métodos Reservations
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsAdministrator] #Solo el administrador puede verlos

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]  #Permitir acceso a todos para hacer reservaciones

#Métodos SoccerField_Reservations
class SoccerField_ReservationListCreate(generics.ListCreateAPIView):
    queryset = SoccerField_Reservation.objects.all()
    serializer_class = SoccerField_ReservationSerializer 
    permission_classes = [IsAuthenticated, IsAdministrator] #Solo el administrador puede verlos

class SoccerField_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoccerField_Reservation.objects.all()
    serializer_class = SoccerField_ReservationSerializer
    permission_classes = [AllowAny]  #Permitir acceso a todos para hacer reservaciones

#Métodos Coworking_Reservations
class Coworking_ReservationListCreate(generics.ListCreateAPIView):
    queryset = Coworking_Reservation.objects.all()
    serializer_class = Coworking_ReservationSerializer
    permission_classes = [IsAuthenticated, IsAdministrator] #Solo el administrador puede verlos

class Coworking_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coworking_Reservation.objects.all()
    serializer_class = Coworking_ReservationSerializer
    permission_classes = [AllowAny]  #Permitir acceso a todos para hacer reservaciones

#Métodos Salon_Reservations
class Salon_ReservationListCreate(generics.ListCreateAPIView):
    queryset = Salon_Reservation.objects.all()
    serializer_class = Salon_ReservationSerializer
    permission_classes = [IsAuthenticated, IsAdministrator] #Solo el administrador puede verlos

class Salon_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salon_Reservation.objects.all()
    serializer_class = Salon_ReservationSerializer
    permission_classes = [AllowAny]  #Permitir acceso a todos para hacer reservaciones


#Métodos Early_Exit_Permissions
class Early_Exit_PermissionListCreate(generics.ListCreateAPIView):
    queryset = Early_Exit_Permission.objects.all()
    serializer_class = Early_Exit_PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdministrator] 
    
class Early_Exit_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Early_Exit_Permission.objects.all()
    serializer_class = Early_Exit_PermissionSerializer
    permission_classes = [IsAuthenticated, IsAdministrator, IsProfesor, IsEstudiante] #Todos ellos pueden hacer post

#Métodos Meeting_Request_Permissions
class Meeting_Request_PermissionListCreate(generics.ListCreateAPIView):
    queryset = Meeting_Request_Permission.objects.all()
    serializer_class = Meeting_Request_PermissionSerializer 

class Meeting_Request_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meeting_Request_Permission.objects.all()
    serializer_class = Meeting_Request_PermissionSerializer

#/////////////////// 3. Relación uno a muchos ///////////////////#

#Métodos Courses
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 
    permission_classes = [IsAuthenticated,IsEstudiante] #Permitir acceso a todos sin autenticación

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdministrator] 


#Métodos Permission_Slips
class Permission_SlipListCreate(generics.ListCreateAPIView):
    queryset = Permission_Slip.objects.all()
    serializer_class = Permission_SlipSerializer 

class Permission_SlipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission_Slip.objects.all()
    serializer_class = Permission_SlipSerializer


#/////////////////// 4. Relación muchos a muchos ///////////////////#

#Métodos Registrations
class RegistrationListCreate(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer 

class RegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


#Métodos Role_Permissions
class Role_PermissionListCreate(generics.ListCreateAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = Role_PermissionSerializer 

class Role_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = Role_PermissionSerializer


#CONSULTA 1
class StudentCourseView(APIView):
    def get(self, request):
        # Prefetch related desde Registration
        registrations = Registration.objects.prefetch_related('Course__teacher', 'Student')
        serializer = StudentCourseSerializer(registrations, many=True)
        return Response(serializer.data)





"""
#Se define la vista 'register_user' para manejar solicitudes HTTP de tipo POST
@api_view(['POST'])
def register_user(request):
    #Crea una instancia del serializador de usuario, tomando los datos que se envían en la solicitud POST
    serializer = UserRegisterSerializer(data=request.data)

    #Verificar si los datos cumplen con las reglas de validación del serializador
    if serializer.is_valid():
        #Si los datos son válidos, guarda el nuevo usuario en la base de datos
        #Aquí se asegura de que la contraseña esté encriptada y los datos cumplan con el modelo de usuario
        user = serializer.save()
        
        #Para agregar usuario a un grupo en especifico
        # Obtén el nombre del grupo desde los datos enviados en la solicitud
        grupo_nombre = request.data.get('grupo', None)
        
        if grupo_nombre:
            try:
                grupo = Group.objects.get(name=grupo_nombre)
                usuario.groups.add(grupo)
            except Group.DoesNotExist:
                return Response({"error": "El grupo especificado no existe."}, status=status.HTTP_400_BAD_REQUEST)
        
        
        #grupo_estudiante = Group.objects.get(name="Administrador")
        #usuario.groups.add(grupo_administrador)

        return Response({"message": "¡Usuario creado con éxito!"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
