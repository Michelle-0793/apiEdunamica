#ESTRUCTURA DE LA BASE DATOS (TABLAS DE LA BASE DE DATOS)
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


#///////////////////1. Tablas de Apoyo y Base: Sin Dependencias Externas///////////////////#
class Team_Members(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone_Number = PhoneNumberField(unique=True)
    hire_date = models.DateField() 
    Id_Rol = models.ForeignKey(Id_Rol, on_delete=models.CASCADE)
    Menbers_Type = models.CharField(max_length=200)

    def __str__(self):
         return str(self.Name)
     
     
#////////////////2. Tablas Dependientes Directas: Relaciones Uno a Uno////////////////#




#////////////////3. Tablas de Relación Uno a Muchos ////////////////#



#////////////////4. Tablas de Relaciones Muchos a Muchos ////////////////#