# Proyecto de blog personal

Este es un proyecto de blog personal creado para practicar y mejorar mis conocimientos de Django. El blog permite a los usuarios interactuar con las entradas, administrar sus publicaciones favoritas y explorar diferentes categorías.

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:


### Descripción de Carpetas y Archivos

- **apps**: Contiene las aplicaciones Django personalizadas.
  - **entrada**: Maneja las entradas o artículos del blog.
  - **favoritos**: Maneja la funcionalidad de favoritos para los usuarios.
  - **home**: Maneja la página principal del sitio.
  - **users**: Maneja la lógica relacionada con los usuarios, incluyendo el procesamiento de datos.
    - `processors.py`: Procesadores personalizados para manejar datos globales.
    
- **blog**: Contiene la configuración base del proyecto Django.
  - `settings/`: Configuración del proyecto.
  - `asgi.py`: Configuración ASGI para la implementación.
  - `urls.py`: Configuración de las rutas del proyecto.
  - `wsgi.py`: Configuración WSGI para la implementación.

- **media**: Directorio para almacenar archivos subidos por el usuario, como imágenes.

- **static**: Archivos estáticos como hojas de estilo (CSS), imágenes y JavaScript.
  - `css/`: Archivos CSS personalizados.
  - `img/`: Imágenes estáticas.
  - `js/`: Archivos JavaScript.

- **templates**: Contiene las plantillas HTML para las diferentes aplicaciones.
  - `entrada/`: Plantillas para las entradas del blog.
  - `favoritos/`: Plantillas relacionadas con la funcionalidad de favoritos.
  - `home/`: Plantillas para la página de inicio.
  - `includes/`: Fragmentos de código reutilizables en distintas partes del sitio.
  - `users/`: Plantillas para el manejo de usuarios.

- **base.html**: Plantilla base que heredan todas las otras plantillas del proyecto.

- **.gitignore**: Lista de archivos y carpetas que Git debe ignorar.

- **manage.py**: Script de Django para la gestión del proyecto (ejecución del servidor, migraciones, etc.).

- **requirements.txt**: Lista de dependencias y paquetes necesarios para el proyecto.
