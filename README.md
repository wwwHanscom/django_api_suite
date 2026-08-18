# Django API Suite

Backend desarrollado con **Django** y **Django REST Framework (DRF)** como parte del proceso de aprendizaje y práctica del desarrollo de APIs REST.

## Descripción

Este proyecto implementa un backend modular utilizando Django. Incluye una página web renderizada del lado del servidor, una API REST de demostración para operaciones CRUD y una API conectada con **Firebase Realtime Database** mediante el **Firebase Admin Python SDK**.

El proyecto también contempla el despliegue del backend en **PythonAnywhere**, permitiendo exponer los servicios REST para su consumo desde clientes externos.

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- Firebase Admin Python SDK
- Firebase Realtime Database
- HTML / CSS
- Git y GitHub
- PythonAnywhere

## Estructura del proyecto

```
django_api_suite/
├── backend_data_server/    # Configuración principal de Django
├── homepage/               # Página principal y plantillas SSR
├── demo_rest_api/          # API REST de demostración
├── landing_api/            # API conectada con Firebase
├── templates/              # Plantillas HTML
├── static/                 # Archivos estáticos
├── secrets/                # Credenciales privadas (no versionadas)
├── assets/                 # Archivos estáticos recolectados para despliegue
├── manage.py
├── requirements.txt
└── .gitignore
```

## APIs disponibles

### Homepage

Página principal renderizada mediante Django Server Side Rendering (SSR).

```
/
```

### Demo REST API

API de demostración que utiliza una lista en memoria como fuente de datos y permite practicar las operaciones HTTP:

```
GET     /demo/rest/api/index/
POST    /demo/rest/api/index/
PUT     /demo/rest/api/<id>/
PATCH   /demo/rest/api/<id>/
DELETE  /demo/rest/api/<id>/
```

Las operaciones `PUT`, `PATCH` y `DELETE` trabajan sobre un elemento identificado mediante su `id`.

### Landing API

API desarrollada con Django REST Framework que funciona como intermediario entre el cliente y Firebase Realtime Database.

```
GET     /landing/api/index/
POST    /landing/api/index/
```

El método `GET` consulta los datos almacenados en Firebase, mientras que `POST` permite crear nuevos registros y agrega automáticamente un campo `timestamp`.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/<USUARIO-GITHUB>/django_api_suite.git
cd django_api_suite
```

Crear el ambiente virtual:

```bash
python -m venv env
```

Activarlo en Linux/macOS:

```bash
source env/bin/activate
```

En Windows:

```powershell
env\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de Firebase

La API `landing_api` requiere credenciales del Firebase Admin SDK.

Crear la carpeta:

```
secrets/
```

y colocar dentro la clave privada:

```
secrets/
└── landing-key.json
```

La carpeta `secrets/` está excluida del control de versiones mediante `.gitignore` para evitar publicar credenciales privadas.

También debe configurarse en Django la URL de Firebase Realtime Database correspondiente al proyecto.

## Ejecución local

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

El proyecto estará disponible normalmente en:

```
http://127.0.0.1:8000/
```

## Archivos estáticos

Los archivos estáticos se encuentran en:

```
static/
└── img/
    └── team.jpg
```

Django utiliza la etiqueta `{% static %}` para resolver las rutas de estos recursos desde las plantillas.

Para preparar los archivos estáticos para producción:

```bash
python manage.py collectstatic
```

## Dependencias

Las dependencias utilizadas en el proyecto se encuentran en:

```
requirements.txt
```

Para actualizar el archivo después de instalar o modificar paquetes:

```bash
pip freeze > requirements.txt
```

## Despliegue

El backend puede desplegarse en **PythonAnywhere** utilizando una configuración WSGI de Django.

Durante el despliegue se deben configurar:

- El ambiente virtual.
- El directorio de trabajo del proyecto.
- `ALLOWED_HOSTS`.
- Los archivos estáticos.
- El archivo WSGI.
- Las credenciales de Firebase.
- La conexión con Firebase Realtime Database.

## Seguridad

Las credenciales y archivos sensibles no deben almacenarse en el repositorio.

En particular:

```
secrets/
```

debe permanecer incluido en `.gitignore`.

Nunca se deben publicar en GitHub las claves privadas del Firebase Admin SDK.

## Control de versiones

El proyecto utiliza Git para controlar los cambios y GitHub como repositorio remoto.

El desarrollo se realiza mediante ramas y los cambios terminados se integran a la rama principal mediante Pull Requests.

## Objetivo académico

El propósito del proyecto es consolidar los conocimientos fundamentales para construir, probar y desplegar un backend con Django, pasando progresivamente por:

1. Creación y configuración de un proyecto Django.
2. Desarrollo de aplicaciones Django.
3. Server Side Rendering y plantillas.
4. Gestión de archivos estáticos.
5. Desarrollo de APIs REST con Django REST Framework.
6. Implementación de operaciones CRUD.
7. Integración con Firebase Realtime Database.
8. Gestión segura de credenciales.
9. Despliegue de una API en la nube.

## Autores

**Hans Rivas**

**Miguel Galarza**


Proyecto desarrollado con fines académicos.
