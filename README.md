Documentación del Proyecto:

Gestión de Cursos y Cobertura Docente

(Polo Tecnológico)

Nombre: Alexander Machin
Instituto: Polo Educativo Durazno
Docente: Leandro Cabrera

1. Introducción

El presente proyecto surge como parte de nuestra formación práctica en el Polo
Tecnológico, donde identificamos la necesidad de optimizar el seguimiento y control de los
cursos, asignaciones docentes y cobertura de grupos. Para responder a esta problemática,
adaptamos una aplicación web base construida sobre arquitectura LAMP (Linux, Apache,
MySQL, PHP 8.3), transformándola de un sistema de tickets a un sistema de Gestión de
Cobertura Docente. Nuestro objetivo es aplicar buenas prácticas de desarrollo backend,
control de versiones y contenerización con Docker, ofreciendo una solución funcional y
organizada para la institución.

2. Alcance

El sistema abarca la digitalización y control de la cobertura de cursos en el ámbito
institucional. Los límites funcionales contemplan:
● Gestión de usuarios con control de acceso basado en roles (Encargado y Docente).
● Administración de cursos, grupos, franjas horarias y asignación de aulas o espacios
académicos.
● Mecanismo de priorización de requerimientos bajo metodología MoSCoW.
● Despliegue contenerizado mediante Docker y Docker Compose para garantizar la
portabilidad y paridad de entornos de desarrollo y producción.
3. Definición de Roles del Sistema

El sistema contempla dos perfiles de usuario bien diferenciados:
● Rol Docente: Perfil orientado al usuario que imparte clases. Sus permisos le
permiten registrar necesidades de cobertura o asistencia en sus grupos asignados,
así como visualizar y modificar únicamente las solicitudes que él mismo haya
creado.
● Rol Encargado (Sección / Piso): Perfil de gestión y administración institucional. Es el
único usuario autorizado para registrar nuevas cuentas en el sistema. Además,
posee acceso a la vista global de todas las solicitudes, pudiendo filtrarlas,
ordenarlas, cambiarles el estado, modificar su prioridad y crear nuevas asignaciones
de cursos.

4. Product Backlog y Requerimientos
Para organizar el desarrollo de la aplicación, adaptamos la lista de requerimientos que
trabajamos en clase para el sistema de tickets a las necesidades de la gestión de cursos y
cobertura docente. Clasificamos los requerimientos entre lo que el sistema debe hacer
(funcionales) y cómo debe estar construido por dentro (no funcionales), asignándole a cada
uno su prioridad MoSCoW:
Requerimientos No Funcionales (Cómo está hecho el sistema)
● RF-01 (Frontend separado): Hacemos la interfaz con HTML5, CSS y JavaScript
vainilla de forma independiente al backend, para que el cliente solo se encargue de
mostrar los datos. (Prioridad: 1 - Debe Tener)
● RF-02 (Backend por capas): Armamos el backend en PHP 8.3 ordenado por capas
(Modelos, DTOs, Controladores, Rutas y Servicios) para que el código no quede
entreverado. (Prioridad: 1 - Debe Tener)
● RF-03 (Base de datos MySQL): Usamos MySQL 8.0 conectado mediante PDO para
guardar los datos de forma relacional y poder administrar la base desde
phpMyAdmin. (Prioridad: 1 - Debe Tener)
● RF-04 (Control de versiones con Git/GitHub): Llevamos todo el control de cambios
del código fuente en un repositorio de GitHub para trabajar en equipo y entregar el
proyecto. (Prioridad: 1 - Debe Tener)
● RF-05 (Contraseñas seguras): Guardamos las claves de los usuarios encriptadas en
la base de datos usando password_hash para evitar tener contraseñas en texto
plano. (Prioridad: 2 - Recomendado)
Requerimientos Funcionales (Lo que hace la aplicación)
● RF-06 (Pantallas según el rol): El sistema muestra una vista diferente dependiendo
de quién inicie sesión: un panel para el Encargado de piso/sección y otro para el
Docente. (Prioridad: 1 - Debe Tener)
● RF-07 (Ver y filtrar solicitudes): El Encargado puede ver el listado de todas las
solicitudes de cobertura y filtrarlas por fecha, estado o prioridad. (Prioridad: 1 - Debe
Tener)
● RF-08 (Ordenar el listado): El Encargado puede ordenar la lista de coberturas por
fecha de creación, estado o nivel de urgencia. (Prioridad: 2 - Recomendado)
● RF-09 (Cambiar estado y prioridad): El Encargado tiene permisos para modificar en
qué estado está la solicitud y qué prioridad tiene. (Prioridad: 2 - Recomendado)
● RF-10 (Crear solicitudes por Encargado): El Encargado puede registrar nuevas

solicitudes o asignaciones directas de cursos en el sistema. (Prioridad: 1 - Debe
Tener)
● RF-11 (Crear solicitudes por Docentes): Los Docentes pueden enviar solicitudes
para pedir asistencia o reportar necesidad de cobertura en sus grupos. (Prioridad: 1 -
Debe Tener)
● RF-12 (Editar solicitudes propias): El Docente puede modificar la descripción y
prioridad de sus propias solicitudes mientras no estén cerradas. (Prioridad: 2 -
Recomendado)
● RF-13 (Bloqueo de registros cerrados): Si una solicitud pasa a estado "Cerrado", el
sistema no permite que nadie la vuelva a modificar. (Prioridad: 1 - Debe Tener)
● RF-14 (Crear usuarios): Solo el Encargado puede dar de alta nuevos usuarios en la
plataforma y asignarles si son Docentes o Encargados. (Prioridad: 1 - Debe Tener)
● RF-15 (Asignar aula o salón): Se puede agregar en qué salón o laboratorio ocurre la
solicitud (dejándolo vacío si es un curso virtual o general). (Prioridad: 2 -
Recomendado)
Estructura de Entidades y Datos
● RF-16 (Entidad Solicitud/Cobertura): Tabla principal donde guardamos el ID,
descripción, fecha/hora, estado, prioridad y quién creó la solicitud. (Prioridad: 1)
● RF-17 (Entidad Usuario): Tabla de usuarios con ID, nombre, apellido, cédula, correo
institucional, contraseña cifrada, estado activo y rol. (Prioridad: 1)
● RF-18 (Entidad Prioridad): Catálogo para clasificar las urgencias (Fatal/Crítica, Alta,
Media, Baja). (Prioridad: 2)
● RF-19 (Entidad Estado): Catálogo para controlar las etapas de la solicitud (Abierta,
En Proceso, Resuelta / Fuera de Alcance). (Prioridad: 2)
● RF-20 (Enumerador de Roles): Registro de roles para diferenciar los accesos entre
Docente y Encargado. (Prioridad: 2)

5. Diagrama de Gantt y Planificación Temporal (Sprint

Backlog)

Prioridad Tarea / Entregable Semana
1

Semana
2

Semana 3

3
(Necesario)

Tarea 1: Configuración de
infraestructura Docker
Compose (PHP 8.3 Apache,
MySQL, phpMyAdmin)

X

3
(Necesario)

Tarea 2: Diseño del
esquema SQL relacional y
autenticación de usuarios

X X

2 (Debería) Tarea 3: Desarrollo de
backend por capas
(Modelos, DTOs,
Controladores, Servicios) y
rutas

X

1 (Se podría) Tarea 4: Implementación de
vistas diferenciadas para
Docente y Encargado

X

2 (Debería) Tarea 5: Lógica de
asignaciones, ordenamiento
y filtrado por fecha, estado y
prioridad

X X

3
(Necesario)

Tarea 6: Pruebas de
integración end-to-end,

X

inmutabilidad de estados y
entrega final

6. Análisis MoSCoW

● Prioridad 3 - Necesario: Es lo indispensable para que el sistema funcione. Incluye
levantar el entorno en Docker Compose, armar la base de datos MySQL,
implementar el login con contraseñas encriptadas, permitir crear solicitudes y
asegurar que una vez cerrada una cobertura no se pueda modificar.
● Prioridad 2 - Debería: Funcionalidades importantes para que la aplicación sea
práctica de usar. Abarca la arquitectura modular en PHP por capas, los filtros y
ordenamiento de solicitudes para el Encargado, la edición de solicitudes propias por
parte de los Docentes y poder indicar el aula o laboratorio.
● Prioridad 1 - Se podría: Mejoras secundarias orientadas a la experiencia visual,
como retoques estéticos en los paneles o interacciones más fluídas en el navegador
con JavaScript.
