from rest_framework import generics
from django.shortcuts import render

from .models import Usuario

from .serializers import UsuarioSerializer

#/////////////////// 1. Principales ///////////////////#

#Métodos roles
class RolListCreate(generics.ListCreateAPIView):
    queryset = Rol.objects.all() #Define el conjunto de datos que se utilizarán (todas las recetas)
    serializer_class = RolSerializer #Especifica el serializer para convertir los datos a JSON

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
""""
#Métodos Permissions
class PermissionListCreate(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = RolSerializer 

class RolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rol.objects.all()
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

#Métodos Meeting_Request_Permissions


#/////////////////// 3. Relación uno a muchos ///////////////////#

#Métodos Courses

#Métodos Registrations

#Métodos Reservations

#Métodos Permission_Slips


#/////////////////// 4. Relación muchos a muchos ///////////////////#

#Métodos Role_Permissions
""""