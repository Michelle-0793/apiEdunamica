#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from django.utils import timezone
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
        
    def validate_Role_Name(self, value):
        # Validación de espacios vacíos y longitud
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        
        # Validación para que el nombre empiece con mayúscula
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del rol debe empezar con mayúscula.")

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
            raise ValidationError("El nombre del permiso debe empezar con mayúscula.")
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
            raise ValidationError("La contraseña debe contener al menos un número.")
         return value



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

     #Validación de espacios Vacios
    def validate_First_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  

    #Validación para el nombre empieze con Mayúscula
    def validate_First_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre debe empezar con mayúscula.")
        return value   


         #Validación de espacios Vacios
    def validate_Last_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Apellido debe tener más de 2 caracteres.")
        return value  

    #Validación para el nombre empieze con Mayúscula
    def validate_Last_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El Apellido debe empezar con mayúscula.")
        return value   


#Validación de espacios Vacios
    def validate_Address (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La dirección debe tener más de 2 caracteres.")
        return value         
    
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'   

#Validación de espacios Vacios
    def validate_First_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  

#Validación para el nombre empieze con Mayúscula
    def validate_First_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre debe empezar con mayúscula.")
        return value   


#Validación de espacios Vacios
    def validate_Last_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Apellido debe tener más de 2 caracteres.")
        return value  

#Validación para el Apellido empieze con Mayúscula
    def validate_Last_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El Apellido debe empezar con mayúscula.")
        return value   

#Validación de espacios Vacios
    def validate_Specialization(self, value):
        if len(value) <= 5:
            raise serializers.ValidationError("La especialización debe tener más de 5 caracteres.")
        return value  

#Validación para el nombre empieze con Mayúscula
    def validate_Specialization(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La especialización debe empezar con mayúscula.")
        return value  


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
    
#Validación para el nombre empieze con Mayúscula
    def validate_Name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre debe empezar con mayúscula.")
        return value   
     
 #Validación de espacios Vacios
    def validate_Name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Nombre debe tener más de 2 caracteres.")
        return value


#Validación de espacios Vacios
    def validate_Last_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El Apellido debe tener más de 2 caracteres.")
        return value  

#Validación para el Apellido empieze con Mayúscula
    def validate_Last_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El Apellido debe empezar con mayúscula.")
        return value   


#Validación de espacios Vacios
    def validate_Menbers_Type (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_Menbers_Type(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Debe empezar con mayúscula.")
        return value   


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__' 


    #Validación de espacios Vacios
    def validate_Partner_Name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("Debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_Partner_Name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Debe empezar con mayúscula.")
        return value   


#Validación de espacios Vacios
    def validate_Status (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El estado debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_Status(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El estado debe empezar con mayúscula.")
        return value   

        
class GraduatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduated
        fields = '__all__' 

    def validate_Graduation_date(self, value):

        current_date = timezone.now().date()
        # Validar si la fecha es mayor o igual a la fecha actual
        if value >= current_date:
            raise serializers.ValidationError('La fecha debe ser anterior al día actual.')
        
        return value

        
class Administrative_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative_Staff
        fields = '__all__'

        
#Validación de espacios Vacios
    def validate_department (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre del departamento debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_department(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El estado debe empezar con mayúscula.")
        return value         
    
#Validación de espacios Vacios
    def validate_office_location (self, value):
        if len(value) <= 5:
            raise serializers.ValidationError("Debe tener más de 5 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_office_location(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Debe empezar con mayúscula.")
        return value 
        

class Cleaning_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning_Staff
        fields = '__all__'

            
    #Validación de espacios Vacios
    def validate_shift  (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_shift (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value


        #Validación de espacios Vacios
    def validate_assigned_area (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_assigned_area (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value    



class Maintenance_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_Staff
        fields = '__all__'
        
     #Validación de espacios Vacios
    def validate_Permission_Name(self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre debe tener más de 2 caracteres.")
        return value  

    #Validación para el nombre empieze con Mayúscula
    def validate_Permission_Name(self, value):
        if not value[0].isupper():
            raise ValidationError("El nombre del permiso debe empezar con mayúscula.")
        return value    

    
class Security_StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Security_Staff
        fields = '__all__'

    #Validación de espacios Vacios
    def validate_shift  (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_shift (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value

        #Validación de espacios Vacios
    def validate_assigned_area (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_assigned_area (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value      

                  
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

        #Validación de espacios Vacios
    def validate_Reservation_Type (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_Reservation_Type (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value

        #Validación de espacios Vacios
    def validate_Status (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El estado debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_Status(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El estado debe empezar con mayúscula.")
        return value 

                

class SoccerField_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoccerField_Reservation
        fields = '__all__'

        #Validación de espacios Vacios
    def validate_field_type  (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_field_type (self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value

                
  
class Coworking_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coworking_Reservation
        fields = '__all__'

            
    #Validación de espacios Vacios
    def validate_equipment_required (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El contenido debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula
    def validate_equipment_required(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El contenido debe empezar con mayúscula.")
        return value    


class Salon_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon_Reservation
        fields = '__all__'


        #Validación de espacios Vacios ("disposición de asientos")
    def validate_seating_arrangement (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La disposicion de asientos debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula ("disposición de asientos")
    def validate_seating_arrangement(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La disposicion de asientos debe empezar con mayúscula.")
        return value 

  
class Permission_SlipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission_Slip
        fields = '__all__'

            
    #Validación de espacios Vacios (Estatus)
    def validate_Status (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El estado debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula (Estatus)
    def validate_Status(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El estado debe empezar con mayúscula.")
        return value  

        #Validación de espacios Vacios (Description)
    def validate_Description (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La descripcion debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula (Description)
    def validate_Description(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La descripcion debe empezar con mayúscula.")
        return value 

            
    #Validación de espacios Vacios (Tipo de permiso)
    def validate_Permission_type (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El tipo de permiso debe tener más de 2 caracteres.")
        return value  

    #Validación para que empieze con Mayúscula (Tipo de permiso)
    def validate_Permission_type(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El tipo de permiso debe empezar con mayúscula.")
        return value  

                 
class Early_Exit_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Early_Exit_Permission
        fields = '__all__'

        #Validación de espacios Vacios (Razon de salida)
    def validate_reason_for_exit (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La razón de salida debe tener más de 2 caracteres.")
        return value  

        #Validación para que empieze con Mayúscula (Razon de salida)
    def validate_reason_for_exit(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La razón de salida debe empezar con mayúscula.")
        return value  


class Meeting_Request_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting_Request_Permission
        fields = '__all__'

        #Validación de espacios Vacios (Lugar de reunion)
    def validate_meeting_location (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La direccion debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula (Lugar de reunion)
    def validate_meeting_location(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La direccion debe empezar con mayúscula.")
        return value  

            
    #Validación de espacios Vacios (Respuesta sobre)
    def validate_requested_by (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La respuesta debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula (Respuesta sobre)
    def validate_requested_by(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La respuesta debe empezar con mayúscula.")
        return value  


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
        
    def validate_course_name(self, course_name):
        
        # Comprobar si el curso ya existe
        if Course.objects.filter(course_name__iexact=course_name).exists():
            raise ValidationError(f'El curso "{course_name}" ya existe.')
        
        return course_name

            
    #Validación de espacios Vacios (Nombre)
    def validate_course_name (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El nombre del curso debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula (Nombre)
    def validate_course_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El nombre del curso debe empezar con mayúscula.")
        return value  
    

     #Validación de espacios Vacios (Descripcion)
    def validate_description (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("La descripcion del curso debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula (Descripcion)
    def validate_description(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("La descripcion del curso debe empezar con mayúscula.")
        return value  


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

    def validate(self, attrs):
        student = attrs.get('Student')
        course = attrs.get('Course')
        
        if Registration.objects.filter(Student=student, Course=course).exists():
            raise serializers.ValidationError('Este estudiante ya está inscrito en este curso.')
        
        return attrs
    
            
    #Validación de espacios Vacios
    def validate_Status (self, value):
        if len(value) <= 2:
            raise serializers.ValidationError("El estado debe tener más de 2 caracteres.")
        return value  

#Validación para que empieze con Mayúscula
    def validate_Status(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("El estado debe empezar con mayúscula.")
        return value  


class Role_PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Permission
        fields = '__all__'



#CONSULTAS Estudiantes, cursos en los que están matriculados, 
#profesor asignado al curso y horario del curso
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher  # Asegúrate de que tengas este modelo
        fields = ['id', 'First_Name', 'Last_Name', 'Email', 'Phone_Number', 'Specialization']

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()  # Incluye el serializador del profesor

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'start_date', 'end_date', 'teacher']  

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'First_name', 'Last_name', 'Email', 'Phone_Number', 'Registration_date']

class StudentCourseSerializer(serializers.ModelSerializer):
    Student = StudentSerializer() 
    Course = CourseSerializer()  # Anidar el serializador del curso

    class Meta:
        model = Registration
        fields = ['Student', 'Course']  # Incluye los campos del curso
