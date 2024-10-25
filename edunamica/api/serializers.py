#INFORMACIÓN QUE SE VA A USAR Y COMO SE VA A USAR
from django.core.exceptions import ValidationError
from rest_framework import serializers

#IMPORTS MODELS
from .models import Rol
#from .models import Permission
#from .models import User
#from .models import Student
#from .models import Teacher
#from .models import Member
#from .models import Partnership
#from .models import Graduated
#from .models import Administrative_Staff
#from .models import Cleaning_Staff
#from .models import Maintenance_Staff
#from .models import Security_Staff
#from .models import SoccerField_Reservation
#from .models import Coworking_Reservation
#from .models import Salon_Reservation
#from .models import Early_Exit_Permission
#from .models import Meeting_Request_Permission
#from .models import Course
#from .models import Registration
#from .models import Reservation
#from .models import Permission_Slip
#from .models import Role_Permission

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
        
"""
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

"""