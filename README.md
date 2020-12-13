# Proyecto Django REST que implementa un API REST que sirva de backend para una aplicación de gestión de proyectos tipo Jira o Trello

## Pasos seguidos para la creación del proyecto

1. Instalar el paquete django:
   ```
   pip3 install Django==3.1.3
   ```

1. Instalar el paquete django REST:
   ```
   pip3 install djangorestframework
   ```

2. Crear nuevo proyecto
   ```
   django-admin startproject projectManager
   ```

3. Crear nueva aplicación:
   ```
   python3 manage.py startapp projectManagement
   ```

4. En projectManager.settings.py agregar la nueva aplicación 'projectManagement' en INSTALLED_APPS y además añadir también 'rest_framework'

5. En projectManager.settings.py cambiar la configuración de base de datos

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'database',
            'USER': 'root',
            'PASSWORD': 'root,
            'HOST': 'localhost,
            'PORT': '3306'
        }
    }
   ```

5. Para usar MySQL antes hay que haber creado el esquema que vaya a utilizarse, el que se pone en la propiedad 'NAME'

6. En projectManagement.models.py crear los modelos correspondientes:

    ```
    Company 1:1 BillingInfo
    Company 1:N User
    Project N:M User
    Task 1:N User
    Task 1:N Project
    Tag N:M Task
    ```

7. En projectManagement.serializers.py crear un serializador por modelo. No olvidarse de incluir los campos relación.

8. En projectManagement.urls.py agregar las urls para las diferentes operaciones. Las operaciones sobre colecciones tienen el path en plural y las operaciones sobre elementos individuales tienen el path en singular.

8. En projectManager.urls.py añadir 'projectManagement.urls'

9. En projectManagement.views.py crear los métodos para las urls definidas anteriormente. Distinguir en base a los verbos HTTP las distintas operaciones. Cada elemento del modelo de datos tendrá 5 operaciones posibles:

```
Consultar colección - GET
Añadir elemento a colección - POST
Consultar elemento individual - GET
Modificar elemento individual - PUT
Borrar elemento individual - DELETE
```

10. Crear migraciones
   ```
   python3 manage.py makemigrations
   ```
11. Ejecutar migraciones
   ```
   python3 manage.py migrate
   ```

12. Ejecutar la aplicación
   ```
   python3 manage.py runserver
   ```

13. Para testear las URLS se ha incluido un archivo projectManagement.postman_collection.json el cual podemos importar en la herramienta POSTMAN y nos importa las diferentes peticiones ya preparadas para realizar las operaciones CRUD. Tener en cuenta que las operaciones van en orden y que acaban borrando elementos que luego deben usarse para mantener la integridad referencial del modelo. Tener en cuenta también que si vuelve a ejecutarse una petición de creación de un elemento para usar en los ejemplos posteriores, el id de dicho elemento aumentará en cada petición ejecutada al ser una secuencia de base de datos.


## Pasos a seguir para ejecutar el proyecto una vez descargado

1. Abrirlo en visual studio code y abrir una nueva terminal dentro, en el mimso directorio donde está el archivo manage.py, es decir, en la carpeta projectManager.

2. Adaptar la base de datos o no, por defecto utilizar SQLite, no tenemos que instalar ni configurar nada pero si se desea 
utilizar MySQL habrá que actualizar settings.py para que apunte a MySQL:

3. Crear migraciones
   ```
   python3 manage.py makemigrations
   ```
4. Ejecutar migraciones
   ```
   python3 manage.py migrate
   ```

5. Ejecutar la aplicación
   ```
   python3 manage.py runserver
   ```
Nota: en windows utilizaremos py -3 en lugar de python3 para los comandos.