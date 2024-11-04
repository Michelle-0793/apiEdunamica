from django.urls import path
from . import views
from .views import StudentCourseView
from .views import UserListView
from .views import UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path ('token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path ('token/refresh/', TokenRefreshView.as_view(), name= 'token_resfresh'),
    
    path('roles/', views.RolListCreate.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', views.RolDetail.as_view(), name='rol-detail'),
    
    path('accesosRol/', views.PermissionListCreate.as_view(), name = 'Permission-List-Create'),
    path('accesosRol/<int:pk>/', views.PermissionDetail.as_view(), name= 'Permission-Detail'),
    
    path('usuarios/', views.UserListCreate.as_view(), name='user-list-create'),
    path('usuarios/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),  

    path('estudiantes/', views.StudentListCreate.as_view(), name = 'Student-List-Create'),
    path('estudiantes/<int:pk>/', views.StudentDetail.as_view(), name = 'Student-Detail'),

    path('profesores/', views.TeacherListCreate.as_view(), name = 'Teacher-List-Create'),
    path('profesores/<int:pk>/', views.TeacherDetail.as_view(), name = 'Teacher-Detail'),

    path('personal/', views.MemberListCreate.as_view(), name = 'Member-List-Create'),
    path('personal/<int:pk>/', views.MemberDetail.as_view(), name = 'Member-Detail'),
    
    path('convenios/', views.PartnershipListCreate.as_view(), name = 'Partnership-List-Create'),
    path('convenios/<int:pk>/', views.PartnershipDetail.as_view(), name = 'Partnership-Detail'),
   
    path('graduados/', views.GraduatedListCreate.as_view(), name = 'Graduated-List-Create'),
    path('graduados/<int:pk>/', views.GraduatedDetail.as_view(), name = 'Graduated-Detail'),
    
    path('personalAdministrativo/', views.Administrative_StaffListCreate.as_view(), name = 'Administrative_Staff-List-Create'),
    path('personalAdministrativo/<int:pk>/', views.Administrative_StaffDetail.as_view(), name = 'Administrative_Staff-Detail'),

    path('personal_Limpieza/', views.Cleaning_StaffListCreate.as_view(), name = 'Cleaning_Staff-List-Create'),
    path('personal_Limpieza/<int:pk>/', views.Cleaning_StaffDetail.as_view(), name = 'Cleaning_Staff-Detail'),

    path('personalMantenimiento/', views.Maintenance_StaffListCreate.as_view(), name = 'Maintenance_Staff-List-Create'),
    path('personalMantenimiento/<int:pk>/', views.Maintenance_StaffDetail.as_view(), name = 'Maintenance_Staff-Detail'),

    path('personalSeguridad/', views.Security_StaffListCreate.as_view(), name = 'Security_Staff-List-Create'),
    path('personalSeguridad/<int:pk>/', views.Security_StaffDetail.as_view(), name = 'Security_Staff-Detail'),

    path('reservas/', views.ReservationListCreate.as_view(), name = 'Reservation-List-Create'),
    path('reservas/<int:pk>/', views.ReservationDetail.as_view(), name = 'Reservation-Detail'),

    path('reservas_Sintetica/', views.SoccerField_ReservationListCreate.as_view(), name = 'SoccerField_Reservation-List-Create'),
    path('reservas_Sintetica/<int:pk>/', views.SoccerField_ReservationDetail.as_view(), name = 'SoccerField_Reservation-Detail'),

    path('reservasCoworking/', views.Coworking_ReservationListCreate.as_view(), name = 'Coworking_Reservation-List-Create'),
    path('reservasCoworking/<int:pk>/', views.Coworking_ReservationDetail.as_view(), name = 'Coworking_Reservation-Detail'),

    path('reservas_Salon/', views.Salon_ReservationListCreate.as_view(), name = 'Salon_Reservation-List-Create'),
    path('reservas_Salon/<int:pk>/', views.Salon_ReservationDetail.as_view(), name = 'Salon_Reservation-Detail'),

    path('permisos/', views.Permission_SlipListCreate.as_view(), name = 'Permission_Slip-List-Create'),
    path('permisos/<int:pk>/', views.Permission_SlipDetail.as_view(), name = 'Permission_Slip-Detail'),

    path('salida_anticipada/', views.Early_Exit_PermissionListCreate.as_view(), name = 'Early_Exit_Permission-List-Create'),
    path('salida_anticipada/<int:pk>/', views.Early_Exit_PermissionDetail.as_view(), name = 'Early_Exit_Permission-Detail'),

    path('solicitud_Reunion/', views.Meeting_Request_PermissionListCreate.as_view(), name = 'Meeting_Request_Permission-List-Create'),
    path('solicitud_Reunion/<int:pk>/', views.Meeting_Request_PermissionDetail.as_view(), name = 'Meeting_Request_Permission-Detail'),

    path('cursos/', views.CourseListCreate.as_view(), name = 'Course-List-Create'),
    path('cursos/<int:pk>/', views.CourseDetail.as_view(), name = 'Course-Detail'),

    path('inscripciones/', views.RegistrationListCreate.as_view(), name = 'Registration-List-Create'),
    path('inscrpciones/<int:pk>/', views.RegistrationDetail.as_view(), name = 'Registration-Detail'),

    path('control/', views.Role_PermissionListCreate.as_view(), name = 'Role_Permission-List-Create'),
    path('control/<int:pk>/', views.Role_PermissionDetail.as_view(), name = 'Role_Permission-Detail'),
    
    path('estudiantes_cursos/', StudentCourseView.as_view(), name='student-course-list'),
    
    path('register/', UserRegisterView.as_view(), name='register_user'),
    
    path('users/', UserListView.as_view(), name='user-list'),
    
]

#path('registro/', UserRegisterView.as_view(), name='register'),