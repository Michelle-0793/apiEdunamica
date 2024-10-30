#ESTRUCTURA DE LA BASE DATOS (TABLAS DE LA BASE DE DATOS)
from django.utils import timezone
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


#///////////////////1. Tablas de Apoyo y Base: Sin Dependencias Externas///////////////////#

class Rol(models.Model):
    Role_Name = models.CharField(max_length=100)
    Description = models.CharField(max_length= 300)

    def __str__(self):
        return str(self.Role_Name)

class Permission (models.Model):
    Permission_Name = models.CharField(max_length=100)
    permit_description = models.CharField(max_length=1000)

    def __str__(self):
         return str(self.Permission_Name)

class User(models.Model):
    Username = models.CharField(max_length=150, unique=True)  
    Password_hash = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255, unique=True) 
    Role = models.ForeignKey(Rol, on_delete=models.CASCADE) 
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Username 

class Student(models.Model):
    First_name = models.CharField(max_length=100) 
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=255, unique=True)
    Phone_Number = models.CharField(max_length=15, blank=True, null=True)
    Address = models.TextField(blank=True, null=True) 
    Birth_Date = models.DateField()
    Registration_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.First_name  

class Teacher(models.Model):
    First_Name = models.CharField(max_length=100)  
    Last_Name = models.CharField(max_length=100) 
    Email = models.EmailField(max_length=255, unique=True) 
    Phone_Number = models.CharField(max_length=15, blank=True, null=True) 
    Specialization = models.CharField(max_length=100) 
    Hire_date = models.DateField()

    def __str__(self): 
       return self.First_Name    
   
class Member(models.Model):
    Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone_Number = PhoneNumberField(unique=True)
    hire_date = models.DateField() 
    id_Roles = models.ForeignKey(Rol, on_delete=models.CASCADE)
    Menbers_Type = models.CharField(max_length=200)

    def __str__(self):
         return str(self.Name)   
     
class Partnership(models.Model):
    Partner_Name = models.CharField(max_length=100)  
    Agreement_Date = models.DateField()
    Expiration_Date = models.DateField()
    Status = models.CharField(max_length=20) 
    Contact_Info = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.Partner_Name     

class Graduated(models.Model):
    Graduated_name = models.CharField(max_length=100)  
    Graduated_lastname = models.CharField(max_length=100)  
    Course_name = models.CharField(max_length=100) 
    Email = models.EmailField(max_length=255)  
    Graduation_date = models.DateField()  

    def __str__(self):
       return str(self.Graduated_name)


#////////////////2. Tablas Dependientes Directas: Relaciones Uno a Uno////////////////#

class Administrative_Staff(models.Model):
    
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    Team_Members = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.department)       
 
class Cleaning_Staff(models.Model):
    
    shift = models.CharField(max_length=100)
    assigned_area = models.CharField(max_length=100)
    Team_Members = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.shift)

class Maintenance_Staff(models.Model):
    
    skills = models.CharField(max_length=100)
    toolkit_provided = models.CharField(max_length=100)
    Team_Members = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.skills)

class Security_Staff(models.Model):
    
    shift = models.CharField(max_length=100)
    security_level = models.CharField(max_length=100)
    assigned_area = models.CharField(max_length=100)
    Team_Members = models.ForeignKey(Member, on_delete=models.CASCADE)
    
    def __str__(self):
         return str(self.shift) 
     

#////////////////3. Tablas de Relación Uno a Muchos ////////////////#
class Reservation(models.Model):
    Reservation_Type = models.CharField(max_length=50)
    Reservation_Date = models.DateField() 
    Time_Start = models.TimeField() 
    Time_End = models.TimeField() 
    Status = models.CharField(max_length=20)

    def __str__(self):
       return self.Reservation_Type

class SoccerField_Reservation(models.Model):
    field_type = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    def __str__(self):
       return self.field_type


class Coworking_Reservation(models.Model):
    desk_number = models.IntegerField()
    equipment_required = models.CharField(max_length=100)
    reservation_duration = models.CharField(max_length=100)
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.desk_number
        
class Salon_Reservation (models.Model):   
    capacity = models.IntegerField()
    audio_video_equipment = models.BooleanField(default=False)
    seating_arrangement = models.CharField(max_length=100)
    Reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
       return self.capacity 

class Permission_Slip(models.Model):
    Permission_type = models.CharField(max_length=50) 
    Request_date = models.DateField()
    Status = models.CharField(max_length=20)
    Description = models.TextField()  

    def __str__(self):
        return self.Permission_type

class Early_Exit_Permission(models.Model):
    permission = models.ForeignKey(Permission_Slip, on_delete=models.CASCADE, related_name='early_exit_permissions')  
    exit_time = models.DateTimeField()
    reason_for_exit = models.TextField()

    def __str__(self):
        return f"Early Exit Permission for {self.permission}"          


class Meeting_Request_Permission(models.Model):
    permission = models.ForeignKey(Permission_Slip, on_delete=models.CASCADE, related_name='meeting_requests')  
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length=100)
    requested_by = models.CharField(max_length=50)

    def __str__(self):
        return f"Meeting Request for {self.permission.Permission_type} on {self.meeting_date} at {self.meeting_time} in {self.meeting_location}"

class Course(models.Model):
    
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.course_name)  


#////////////////4. Tablas de Relaciones Muchos a Muchos ////////////////#

class Registration(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Registration_date = models.DateField()
    Status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Student)
        
class Role_Permission(models.Model):
    Role = models.ForeignKey(Rol, on_delete=models.CASCADE)  
    Permission = models.ForeignKey(Permission, on_delete=models.CASCADE) 

    def __str__(self):
     return f"{self.Role} - {self.Permission}"


