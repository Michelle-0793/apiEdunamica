# API EDUNAMICA
La API EDUNAMICA, desarrollada con Django, es una herramienta de gestión educativa que permite realizar operaciones CRUD sobre distintas entidades de una base de datos para instituciones, como roles, usuarios y estudiantes. Utiliza una base de datos MySQL y se asegura de proteger el acceso a través de autenticación JWT, permitiendo que solo usuarios autenticados puedan interactuar con los datos.

## Principales Componentes
1. **Modelos**: Los modelos definen la estructura de las tablas y relaciones en la base de datos. Por ejemplo, Rol representa roles dentro del sistema y se relaciona con otros modelos como User.
2. **Serializadores**: Los datos se convierten a JSON mediante serializadores, que también incluyen validaciones (como verificar que el nombre de un rol comience con mayúscula).
3. **Vistas**: Las vistas basadas en clases manejan las solicitudes HTTP. Por ejemplo, RolListCreate permite listar y crear roles, mientras que RolDetail facilita la visualización, actualización o eliminación de roles específicos.
4. **URLs**: Definen rutas específicas para acceder a las vistas y realizar operaciones sobre entidades como roles y usuarios.
5. **Autenticación**: Utiliza JWT para asegurar las rutas, permitiendo un control de acceso granular para distintos roles, como administrador, profesor o estudiante.

## Estructura de Base de Datos
La base de datos organiza la información en varias tablas:
- Tablas de Apoyo: Tablas como Rol y Permission definen los roles y permisos del sistema.
- Tablas Uno a Uno y Uno a Muchos: Permiten registrar al personal administrativo y reservas, como permisos de salida o cursos asignados a estudiantes.
- Tablas Muchos a Muchos: Role_Permission gestiona las relaciones de permisos y roles, permitiendo múltiples asociaciones.

## Vista de Registro de Usuarios - Tabla de Django
Este módulo en Django implementa vistas para la gestión de usuarios, incluyendo registro, detalle y lista de usuarios, utilizando permisos de autenticación y roles específicos.

Clases de Vistas
1. UserRegisterView
    **Descripción**: Permite el registro de nuevos usuarios.
    **Tipo de vista**: CreateAPIView
    **Permisos**: Solo usuarios autenticados (IsAuthenticated).
    **Serializador**: UserRegisterSerializer.
2. UserDetailView
    **Descripción**: Permite obtener, actualizar o eliminar un usuario específico.
    **Tipo de vista**: RetrieveUpdateDestroyAPIView
    **Permisos**: Solo usuarios autenticados (IsAuthenticated).
    **Serializador**: UserRegisterSerializer.
3. UserListView
    **Descripción**: Permite listar todos los usuarios registrados en el sistema.
    **Tipo de vista**: ListAPIView
    **Permisos**: Solo usuarios autenticados (IsAuthenticated).
    **Serializador**: UserListSerializer.

=> Permisos Personalizados
- IsAdministrator: Permite el acceso solo a usuarios que pertenecen al grupo "Administrador".
- IsProfesor: Permite el acceso solo a usuarios que pertenecen al grupo "Profesor".
- IsEstudiante: Permite el acceso solo a usuarios que pertenecen al grupo "Estudiante".

=> Requisitos
Autenticación: Todas las vistas requieren que el usuario esté autenticado mediante un token.


## Instalación y Configuración
Para ejecutar la API:
- Clonar el repositorio y configurar la base de datos en settings.py.
- Instalar dependencias y ejecutar migraciones.
- Crear un superusuario para acceder a rutas privadas con token JWT.
- Probar rutas privadas con herramientas como Postman, asegurándose de usar el token de acceso para autenticación.
Este proyecto de API REST es ideal para gestionar el flujo de información en una institución educativa de manera segura y estructurada, manteniendo el acceso restringido y facilitando la administración de roles, usuarios y permisos.
