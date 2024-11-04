/////////////SQL INJECTION///////////////
**¿Que es SQL injection?**

La inyección de código SQL es un ataque en el que se inserta código malintencionado en cadenas que posteriormente se pasan a una instancia del motor de base de datos de SQL Server para su análisis y ejecución.

__________________________________________________________________________________________________________________

**¿ Como se puede prevenir un SQL injection?**

Para prevenir SQL injection en Django, lo más importante es usar el ORM (Object-Relational Mapping) de Django en lugar de escribir consultas SQL sin procesar. Algunos consejos son:

1. **Usa el ORM de Django**: El ORM genera consultas SQL automáticamente y maneja de forma segura los datos de entrada.
2. **Consulta parametrizada**: Si necesitas ejecutar una consulta cruda, usa consultas parametrizadas en lugar de concatenar strings.
3. **Escape de caracteres**: Si por alguna razón necesitas construir una consulta SQL manualmente, asegúrate de escapar todos los caracteres especiales.
4. **Validación y saneamiento de datos**: Siempre valida y sanea los datos de entrada.

___________________________________________________________________________________________________________________

**¿Que otras practicas adicionales se pueden implementar?**

1. **Principio de privilegios mínimos**: Asegúrate de que tus bases de datos y aplicaciones solo tengan los permisos necesarios para realizar sus funciones. Evita dar permisos de administrador si no es absolutamente necesario.
2. **Validación de entrada**: Siempre valida y sanea los datos de entrada. Usa las herramientas de validación integradas de Django para asegurar que los datos recibidos sean los esperados.
3. **Almacenamiento seguro de contraseñas**: Django gestiona esto automáticamente, pero es importante mencionarlo. Siempre hashea las contraseñas antes de almacenarlas y nunca guardes contraseñas en texto plano.
4. **Parámetros en consultas crudas**: Si por alguna razón necesitas usar consultas SQL crudas, usa parámetros en lugar de concatenar strings. Por ejemplo:
   
   from django.db import connection

   def get_user_by_email(email):
       with connection.cursor() as cursor:
           cursor.execute("SELECT * FROM users WHERE email = %s", [email])
           return cursor.fetchone()
   
   Aquí, el uso de %s y la lista de parámetros asegura que el email sea tratado de manera segura.

5. **Actualización y parches**: Mantén tu framework de Django y todas las dependencias actualizadas. Las versiones nuevas usualmente corrigen vulnerabilidades conocidas.
6. **Auditorías y pruebas de seguridad**: Realiza auditorías periódicas y pruebas de penetración en tu aplicación para detectar y corregir vulnerabilidades.


__________________________________________________________________________________________________________________

**En conclusion:**
Para lograr prevenir una inyeccion de SQL hay que validar todos los campos para que solo al cumplir todos los requicitos se puedan postear los datos que se quieren, mientras que se practique
sal 



///////////////////CROSS-SITE SCRIPTING (XSS)/////////////////


**¿Que es Cross-Site Scripting?**

Cross-Site Scripting (XSS) es una vulnerabilidad de seguridad que permite a un atacante inyectar scripts maliciosos en páginas web vistas por otros usuarios. En un proyecto Django, es crucial validar y sanitizar las entradas del usuario para prevenir este tipo de ataques. Aquí te dejo algunos pasos y prácticas recomendadas:

1. **Validación de Entrada**

Uso de formularios de Django: Utiliza los formularios de Django para validar la entrada del usuario. Esto incluye definir tipos de campos adecuados y usar validadores personalizados si es necesario.

Limitar los caracteres permitidos: Define qué caracteres son aceptables y restringe la entrada a esos caracteres.


2. **Sanitización de Entrada**

Librerías de sanitización: Considera usar bibliotecas como bleach para limpiar el HTML. bleach permite especificar qué etiquetas y atributos son seguros.

Evitar la inyección de HTML: Nunca permitas que el usuario envíe HTML sin una sanitización adecuada.


3. **Escapado de Salida**

Escapar contenido en plantillas: Por defecto, Django escapa las variables en las plantillas. Asegúrate de no desactivar esta opción, ya que previene la ejecución de scripts en el contenido mostrado.

Uso de safe: Solo utiliza el filtro |safe en Django cuando estés absolutamente seguro de que el contenido es seguro y ha sido debidamente sanitizado.


4. **Uso de Content Security Policy (CSP)**

Implementa un CSP en tus cabeceras HTTP para ayudar a mitigar los riesgos de XSS, permitiendo solo fuentes de scripts específicas.


5. **Pruebas y Monitoreo**

Realiza pruebas de penetración y utiliza herramientas de escaneo de vulnerabilidades para identificar posibles puntos débiles en tu aplicación.

Monitorea los registros de errores y actividades inusuales que puedan indicar intentos de XSS.


**Ejemplo de Uso de bleach:**

import bleach

# Lista de etiquetas permitidas
allowed_tags = ['b', 'i', 'u', 'em', 'strong', 'p']
allowed_attributes = {}

# Entrada del usuario
user_input = "<script>alert('XSS');</script> <b>Texto seguro</b>"

# Sanitizar la entrada
cleaned_input = bleach.clean(user_input, tags=allowed_tags, attributes=allowed_attributes)

print(cleaned_input)  # Solo se mostrará <b>Texto seguro</b>

**Conclución**

Implementar una combinación de validación, sanitización y buenas prácticas de escapado es fundamental para proteger tu aplicación Django contra XSS. Asegúrate de educar a tu equipo sobre estas prácticas y de mantener tu código revisado y actualizado.



# Implementación de JWT Usando el Modelo de Usuario por Defecto

# 1. Instalación de dependencias:
 Instalamos las bibliotecas necesarias, como djangorestframework y djangorestframework-simplejwt, para implementar el JWT.


 # 2.Configurar Django:
  Agregar 'rest_framework' a la lista de aplicaciones instaladas en el archivo settings.py. Y establecer la clase de autenticación de JWT en la configuración de REST Framework.

# 3.Crear Vistas de Autenticación:
 Utilizamos las vistas proporcionadas por djangorestframework-simplejwt para gestionar la obtención y renovación de tokens.

 # 4.


