## Proyecto Final Python Tomasel

<br/>

Simple app de gestión de usuarios y cursos para una institución educativa.

Modo de uso: ejecutar `python manage.py runserver` y seguir el vínculo provisto.

Previamente se puede ejecutar `python manage.py livereload` para ver cambios en el código actualizados en tiempo real en el navegador.

<br/>

Los usuarios creados desde la vista de Register pueden acceder al listado completo de Cursos, Estudiantes y Profesores, así como a la búsqueda por id y vista de detalle de los mismos.

Con el Superusuario "admin" (contraseña: "admin") además se pueden crear y/o eliminar Estudiantes, Profesores y Cursos.

Las rutas están protegidas para impedir que sean accedidas sin estar logueado

Si se sube una imagen de perfil podrá ser visualizada desde la pestaña Profile, en donde además de ver los detalles de la cuenta, se podrán actualizar sus datos.
