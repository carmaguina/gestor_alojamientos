# Gestor de Alojamientos

Gestor de Alojamientos es una aplicación web desarrollada en Django para la gestión interna de alojamientos turísticos pequeños, como cabañas, suites o departamentos de alquiler temporal.

En esta primera etapa, el proyecto permite administrar unidades disponibles y comenzar a estructurar la gestión de huéspedes y reservas.

## Repositorio

https://github.com/carmaguina/gestor_alojamientos.git

## Funcionalidades implementadas

- Modelo `Unidad` para representar alojamientos disponibles.
- Panel de administración de Django personalizado con `ModelAdmin`.
- Búsqueda y filtros en el admin para unidades.
- Acciones personalizadas para activar o desactivar unidades.
- Modelos `Huesped` y `Reserva` creados y registrados en el panel de administración.
- Admin personalizado para huéspedes y reservas.
- CRUD básico de unidades usando Class-Based Views:
  - listado de unidades
  - detalle de unidad
  - creación de unidad
  - edición de unidad
  - eliminación de unidad
- Login y logout de usuarios.
- Protección de vistas sensibles con `LoginRequiredMixin`.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Próximas funcionalidades

- CRUD completo de reservas.
- CRUD de huéspedes.

## Instalación y ejecución local

1. Clonar el repositorio

```powershell
git clone https://github.com/carmaguina/gestor_alojamientos.git
cd gestor_alojamientos
```

2. Crear entorno virtual
```powershell
python -m venv venv_django
```

3. Activar entorno virtual en Windows PowerShell
```powershell
.\venv_django\Scripts\Activate.ps1
```
Si PowerShell bloquea la activación, ejecutar:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```
y volver a activar el entorno.

4. Instalar dependencias
```powershell
pip install -r requirements.txt
```

5. Entrar a la carpeta del proyecto Django
```powershell
cd gestor_alojamientos
```

6. Aplicar migraciones
```powershell
python manage.py migrate
```

7. Crear superusuario
```powershell
python manage.py createsuperuser
```

8. Ejecutar servidor
```powershell
python manage.py runserver
```
Abrir en el navegador:
http://127.0.0.1:8000/alojamientos/  


## URLs principales  

/admin/  
Panel de administración de Django.  

/alojamientos/  
Listado de unidades disponibles.  

/alojamientos/crear/  
Crear una nueva unidad. Requiere iniciar sesión.  

/login/  
Inicio de sesión.  

/logout/  
Cierre de sesión mediante formulario POST.

Usuario de prueba
Para probar las vistas protegidas, se puede crear un superusuario local con:
```powershell
python manage.py createsuperuser
```

Por seguridad, no se incluyen credenciales reales en el repositorio.

## Estructura del proyecto

El repositorio utiliza una carpeta contenedora para el proyecto y, dentro de ella, una carpeta Django donde se encuentra `manage.py`.

Por eso, para ejecutar comandos de Django primero hay que entrar a la carpeta interna:

```bash
cd gestor_alojamientos
python manage.py runserver
```

Esta estructura corresponde a la forma habitual generada por `django-admin startproject nombre_proyecto` y se mantiene documentada para que el proyecto sea reproducible.
