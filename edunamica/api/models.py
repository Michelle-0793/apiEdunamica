#ESTRUCTURA DE LA BASE DATOS (TABLAS DE LA BASE DE DATOS)
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


#///////////////////1. Tablas de Apoyo y Base: Sin Dependencias Externas///////////////////#

class Roles(models.model):
    Role_Name = models.CharField(max_length=100)
    Description = models.CharField(max_length= 300)

    def __str__(self):
        return str(self.Role_Name)
    

class Permission (models.model):
    Permission_Name = models.CharField(max_length=100)
    permit_description = models.CharField(max_length=1000)

    def __str__(self):
         return str(self.Permission_Name)
    

class Users(models.model):
    Users_Name = Name = models.CharField(max_length=100)
    Pasword_Hash



class Team_Members(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone_Number = PhoneNumberField(unique=True)
    hire_date = models.DateField() 
    id_Roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
    Menbers_Type = models.CharField(max_length=200)

    def __str__(self):
         return str(self.Name)
     
     
#////////////////2. Tablas Dependientes Directas: Relaciones Uno a Uno////////////////#

class Administrative_Staff(models.Model):
    
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    
    def __str__(self):
         return str(self.department)
    
class Cleaning_Staff(models.Model):
    
    shift = models.CharField(max_length=100)
    assigned_area = models.CharField(max_length=100)
    
    def __str__(self):
         return str(self.shift)
    
    
class Maintenance_Staff(models.Model):
    
    skills = models.CharField(max_length=100)
    toolkit_provided = models.CharField(max_length=100)
    
    def __str__(self):
         return str(self.skills)
     
     

class Security_Staff(models.Model):
    
    shift = models.CharField(max_length=100)
    security_level = models.CharField(max_length=100)
    assigned_area = models.CharField(max_length=100)
    
    def __str__(self):
         return str(self.shift)
     
    
#////////////////3. Tablas de Relación Uno a Muchos ////////////////#


class Academic_Offerings(models.Model):
    
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    


#////////////////4. Tablas de Relaciones Muchos a Muchos ////////////////#