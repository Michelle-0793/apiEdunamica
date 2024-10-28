from rest_framework import generics
from django.shortcuts import render

from rest_framework import permissions

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

#/////////////////// 1. Principales ///////////////////#

#Métodos roles
class RolListCreate(generics.ListCreateAPIView):
    queryset = Rol.objects.all() #Define el conjunto de datos que se utilizarán (todas las recetas)
    serializer_class = RolSerializer #Especifica el serializer para convertir los datos a JSON
    #permission_classes = [permissions.IsAuthenticated]  #Para proteger esta vista

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
#Métodos Permissions
class PermissionListCreate(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer 

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    
#Métodos Users
class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Métodos Students
class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  

#Métodos Teachers
class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer    
    
#Métodos Team_Members
class MemberListCreate(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer 

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer      

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

class GraduatedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Graduated.objects.all()
    serializer_class = GraduatedSerializer
    
    
#/////////////////// 2. Relación Uno a Uno ///////////////////#

#Métodos Administrative_Staff
class Administrative_StaffListCreate(generics.ListCreateAPIView):
    queryset = Administrative_Staff.objects.all()
    serializer_class = Administrative_StaffSerializer 

class Administrative_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrative_Staff.objects.all()
    serializer_class = Administrative_StaffSerializer    
    
#Métodos Cleaning_Staff
class Cleaning_StaffListCreate(generics.ListCreateAPIView):
    queryset = Cleaning_Staff.objects.all()
    serializer_class = Cleaning_StaffSerializer 

class Cleaning_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cleaning_Staff.objects.all()
    serializer_class = Cleaning_StaffSerializer   
    
#Métodos Maintenance_Staff
class Maintenance_StaffListCreate(generics.ListCreateAPIView):
    queryset = Maintenance_Staff.objects.all()
    serializer_class = Maintenance_StaffSerializer 

class Maintenance_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maintenance_Staff.objects.all()
    serializer_class = Maintenance_StaffSerializer

#Métodos Security_Staff
class Security_StaffListCreate(generics.ListCreateAPIView):
    queryset = Security_Staff.objects.all()
    serializer_class = Security_StaffSerializer 

class Security_StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Security_Staff.objects.all()
    serializer_class = Security_StaffSerializer


#/////////////////// 3. Relación uno a muchos ///////////////////#

#Métodos Reservations
class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer 

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#Métodos SoccerField_Reservations
class SoccerField_ReservationListCreate(generics.ListCreateAPIView):
    queryset = SoccerField_Reservation.objects.all()
    serializer_class = SoccerField_ReservationSerializer 

class SoccerField_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoccerField_Reservation.objects.all()
    serializer_class = SoccerField_ReservationSerializer

#Métodos Coworking_Reservations
class Coworking_ReservationListCreate(generics.ListCreateAPIView):
    queryset = Coworking_Reservation.objects.all()
    serializer_class = Coworking_ReservationSerializer 

class Coworking_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coworking_Reservation.objects.all()
    serializer_class = Coworking_ReservationSerializer

#Métodos Salon_Reservations
class Salon_ReservationListCreate(generics.ListCreateAPIView):
    queryset = Salon_Reservation.objects.all()
    serializer_class = Salon_ReservationSerializer 

class Salon_ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salon_Reservation.objects.all()
    serializer_class = Salon_ReservationSerializer


#Métodos Early_Exit_Permissions
class Early_Exit_PermissionListCreate(generics.ListCreateAPIView):
    queryset = Early_Exit_Permission.objects.all()
    serializer_class = Early_Exit_PermissionSerializer 
    
class Early_Exit_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Early_Exit_Permission.objects.all()
    serializer_class = Early_Exit_PermissionSerializer

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

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#Métodos Registrations
class RegistrationListCreate(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer 

class RegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


#Métodos Permission_Slips
class Permission_SlipListCreate(generics.ListCreateAPIView):
    queryset = Permission_Slip.objects.all()
    serializer_class = Permission_SlipSerializer 

class Permission_SlipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission_Slip.objects.all()
    serializer_class = Permission_SlipSerializer


#/////////////////// 4. Relación muchos a muchos ///////////////////#

#Métodos Role_Permissions
class Role_PermissionListCreate(generics.ListCreateAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = Role_PermissionSerializer 

class Role_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = Role_PermissionSerializer


