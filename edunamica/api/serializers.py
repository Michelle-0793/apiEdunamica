#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from rest_framework import serializers
import re

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

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  
        
#Validación de espacios Vacios 
    def validate_Role_Name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  
 
#Validación para el nombre empieze con Mayúscula
    def validate_Role_Name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del rol debe empezar con mayúscula.")
        return value

#Validación de espacios Vacios
    def validate_Description(self, value):
        if len(value) <= 10:
            raise serializers.ValidationError("La descripción tener más de 10 caracteres.")
        return value      
            
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

#Validación de espacios Vacios
    def validate_Permission_Name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  

    #Validación para el nombre empieze con Mayúscula
    def validate_Permission_Name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del permiso debe empezar con mayúscula.")
        return value 

    #Validación de espacios Vacios
    def validate_Description(self, value):
        if len(value) <= 10:
            raise serializers.ValidationError("La descripción tener más de 10 caracteres.")
        return value                

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

     #Validación de espacios Vacios
    def validate_Username(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  

#Validación para el nombre empieze con Mayúscula
    def validate_Username(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del permiso debe empezar con mayúscula.")
        return value    

#Validación para que la contraseña tenga  mas de 8 caracteres 
    def validate_Password_hash(self, value):
         if len(value) <= 8:
            raise serializers.ValidationError("La contraseña debe tener más de 8 caracteres.")
         if not re.search(r'[A-Za-z]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos una letra.")
         if not re.search(r'[0-9]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos un número.")
         return value



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


        
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'   

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'    

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'      
        
class GraduatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduated
        fields = '__all__'  

        

class Administrative_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative_Staff
        fields = '__all__'

class Cleaning_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning_Staff
        fields = '__all__'

class Maintenance_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_Staff
        fields = '__all__'

class Security_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_Staff
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class SoccerField_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerField_Reservation
        fields = '__all__'


class Coworking_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coworking_Reservation
        fields = '__all__'


class Salon_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon_Reservation
        fields = '__all__'


class Permission_SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission_Slip
        fields = '__all__'


class Early_Exit_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Early_Exit_Permission
        fields = '__all__'


class Meeting_Request_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Request_Permission
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'



class Role_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Permission
        fields = '__all__'
