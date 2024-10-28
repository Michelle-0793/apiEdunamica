from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Admin'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Estudiante'

class CanViewContent(BasePermission):
    def has_permission(self, request, view):
        return 'Ver contenido' in request.user.permissions

class CanCreateReservations(BasePermission):
    def has_permission(self, request, view):
        return 'Crear reservas' in request.user.permissions