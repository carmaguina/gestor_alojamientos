# Gestor de Alojamientos

Gestor de Alojamientos es una aplicacion web desarrollada en Django para la gestion interna de alojamientos turisticos pequenos, como cabanas, suites o departamentos de alquiler temporal.

En esta etapa, el proyecto permite administrar unidades disponibles, consultar alojamientos, buscar unidades por nombre, leer publicaciones del blog, registrarse, iniciar sesion, editar un perfil de usuario y enviar un formulario de contacto.

## Repositorio

https://github.com/carmaguina/gestor_alojamientos.git

## Funcionalidades implementadas

- Modelo `Unidad` para representar alojamientos disponibles.
- CRUD de unidades usando Class-Based Views:
  - listado de unidades
  - detalle de unidad
  - creacion de unidad
  - edicion de unidad
  - eliminacion de unidad
- Busqueda dinamica de unidades por nombre mediante metodo GET y ORM con `nombre__icontains`.
- Templates reutilizables con herencia desde `base.html`.
- Paginas publicas de inicio, acerca de y contacto.
- Formulario de contacto con validacion del mensaje.
- Blog publico con listado y detalle de publicaciones.
- Login y logout de usuarios.
- Registro de usuarios desde la aplicacion.
- Perfil editable para usuarios autenticados.
- Proteccion de vistas sensibles con `LoginRequiredMixin` y permisos especificos de Django.
- Panel de administracion personalizado con `ModelAdmin`.
- Busqueda, filtros y columnas configuradas en el admin de unidades.
- Acciones personalizadas para activar o desactivar unidades desde el admin.
- Modelos `Huesped` y `Reserva` creados, migrados y registrados en el panel de administracion.
- Admin personalizado para huespedes y reservas.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- Git y GitHub

## Estructura del proyecto

El repositorio utiliza una carpeta contenedora y, dentro de ella, una carpeta Django donde se encuentra `manage.py`.

```text
Proyecto_Final_Gestor_Alojamientos/
|-- gestor_alojamientos/
|   |-- manage.py
|   |-- alojamientos/
|   |-- blog/
|   |-- paginas/
|   |-- reservas/
|   |-- usuarios/
|   |-- gestor_alojamientos/
|   `-- templates/
|-- requirements.txt
|-- README.md
|-- .env.example
`-- .gitignore
```

Para ejecutar comandos de Django primero hay que entrar a la carpeta interna:

```powershell
cd gestor_alojamientos
```

Esta estructura corresponde a la forma habitual generada por `django-admin startproject nombre_proyecto` y se mantiene documentada para que el proyecto sea reproducible.

## Instalacion y ejecucion local desde cero

1. Clonar el repositorio:

```powershell
git clone https://github.com/carmaguina/gestor_alojamientos.git
cd gestor_alojamientos
```

2. Crear el entorno virtual:

```powershell
python -m venv venv_django
```

3. Activar el entorno virtual en Windows PowerShell:

```powershell
.\venv_django\Scripts\Activate.ps1
```

Si PowerShell bloquea la activacion de scripts, ejecutar una vez para la sesion:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv_django\Scripts\Activate.ps1
```

4. Instalar dependencias declaradas:

```powershell
pip install -r requirements.txt
```

5. Entrar a la carpeta donde esta `manage.py`:

```powershell
cd gestor_alojamientos
```

6. Aplicar migraciones:

```powershell
python manage.py migrate
```

7. Crear un superusuario local:

```powershell
python manage.py createsuperuser
```

8. Verificar configuracion del proyecto:

```powershell
python manage.py check
```

9. Ejecutar el servidor local:

```powershell
python manage.py runserver
```

10. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Dependencias declaradas

Las dependencias necesarias para reproducir el proyecto estan en `requirements.txt`:

```text
asgiref==3.12.1
Django==5.2.17
sqlparse==0.5.5
tzdata==2026.3
```

## Variables de entorno

El proyecto incluye un archivo `.env.example` como referencia de configuracion. No se sube ningun archivo `.env` real al repositorio porque puede contener secretos.

Variables disponibles:

```text
DJANGO_SECRET_KEY=change-me-in-production
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

En desarrollo local, `settings.py` tiene valores por defecto para poder ejecutar el proyecto sin crear un `.env` obligatorio.

## Migraciones incluidas

El repositorio incluye migraciones para reproducir la estructura de base de datos:

```text
gestor_alojamientos/alojamientos/migrations/0001_initial.py
gestor_alojamientos/alojamientos/migrations/0002_alter_unidad_options.py
gestor_alojamientos/blog/migrations/0001_initial.py
gestor_alojamientos/reservas/migrations/0001_initial.py
gestor_alojamientos/usuarios/migrations/0001_initial.py
```

Comandos utiles para verificar migraciones:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py check
```

## URLs principales

| URL | Descripcion | Acceso |
| --- | --- | --- |
| `/` | Pagina de inicio | Publico |
| `/alojamientos/` | Listado y busqueda de unidades | Publico |
| `/alojamientos/<id>/` | Detalle de una unidad | Publico |
| `/alojamientos/crear/` | Crear unidad | Requiere login y permiso `alojamientos.add_unidad` |
| `/alojamientos/<id>/editar/` | Editar unidad | Requiere login y permiso `alojamientos.change_unidad` |
| `/alojamientos/<id>/eliminar/` | Eliminar unidad | Requiere login y permiso `alojamientos.delete_unidad` |
| `/blog/` | Listado publico de posts publicados | Publico |
| `/blog/<id>/` | Detalle de un post publicado | Publico |
| `/acerca/` | Pagina institucional del proyecto | Publico |
| `/contacto/` | Formulario de contacto | Publico |
| `/registro/` | Registro de usuario | Publico |
| `/perfil/` | Edicion del perfil propio | Usuario autenticado |
| `/login/` | Inicio de sesion | Publico |
| `/logout/` | Cierre de sesion por POST | Usuario autenticado |
| `/admin/` | Panel de administracion | Usuario staff/superusuario |

## Roles y permisos

El proyecto utiliza el sistema de usuarios, grupos y permisos de Django.

| Tipo de usuario | Permisos esperados | Resultado esperado |
| --- | --- | --- |
| Visitante sin sesion | Sin permisos | Puede ver listado, detalle, busqueda, blog, paginas publicas y contacto. Si intenta crear, editar o eliminar unidades, Django lo redirige al login. |
| Usuario comun autenticado | Sin permisos de `Unidad` | Puede iniciar sesion y editar su perfil, pero no puede crear, editar ni eliminar unidades si no tiene permisos asignados. |
| Operador / staff | `add_unidad`, `change_unidad`, `view_unidad` | Puede acceder al admin si tiene `is_staff=True` y gestionar unidades segun permisos asignados. |
| Administrador / superusuario | Todos los permisos | Puede gestionar unidades, huespedes, reservas, posts, perfiles, usuarios, grupos y permisos. |

Para crear grupos desde el admin:

1. Entrar a `/admin/` con un superusuario.
2. Ir a `Autenticacion y autorizacion > Grupos`.
3. Crear grupos como `Operadores` y `Lectores`.
4. Asignar permisos de `Unidad` segun el rol:
   - `Can view unidad`
   - `Can add unidad`
   - `Can change unidad`
   - `Can delete unidad`

Las vistas de crear, editar y eliminar unidades estan protegidas en el codigo con permisos especificos mediante `PermissionRequiredMixin`.

## Pruebas manuales realizadas

| Caso | Comando o URL | Resultado esperado |
| --- | --- | --- |
| Verificar configuracion | `python manage.py check` | Sin errores |
| Ver migraciones | `python manage.py showmigrations` | Migraciones aplicadas con `[X]` |
| Listar unidades | `/alojamientos/` | Muestra unidades cargadas |
| Buscar unidad | `/alojamientos/?q=d` | Filtra unidades por nombre |
| Ver detalle | `/alojamientos/1/` | Muestra datos de la unidad |
| Ver blog | `/blog/` | Muestra posts publicados |
| Ver detalle de post | `/blog/1/` | Muestra titulo, fecha y contenido |
| Registrar usuario | `/registro/` | Crea un usuario y redirige al login |
| Editar perfil | `/perfil/` | Permite completar telefono, ciudad, fecha de nacimiento y bio |
| Enviar contacto | `/contacto/` | Valida el mensaje y muestra confirmacion |
| Crear sin sesion | `/alojamientos/crear/` | Redirige al login con parametro `next` |
| Crear con permisos | `/alojamientos/crear/` | Permite guardar una unidad |
| Admin personalizado | `/admin/alojamientos/unidad/` | Muestra columnas, filtros y busqueda |

## Estado de despliegue

El proyecto esta preparado para ejecutarse de forma local desde cero siguiendo las instrucciones de instalacion. Para un despliegue publico se deben configurar variables de entorno reales, usar `DEBUG=False`, definir `ALLOWED_HOSTS` y servir archivos estaticos con la configuracion correspondiente del hosting elegido.

## Seguridad

- No se sube el entorno virtual al repositorio.
- No se sube `db.sqlite3`.
- No se sube `.env`.
- Las credenciales reales no se incluyen en GitHub.
- Para pruebas locales se debe crear un superusuario con `python manage.py createsuperuser`.
- `SECRET_KEY`, `DEBUG` y `ALLOWED_HOSTS` pueden configurarse mediante variables de entorno.

## Proximas funcionalidades

- CRUD completo de reservas.
- CRUD completo de huespedes.
- Mejoras visuales de templates.
- Pruebas automatizadas para vistas y permisos.
- Configuracion de despliegue en un hosting publico.
