Avance del proyecto - facturacion y transaciones
El vidoe de demostracion del funcionamiento se pued ver en este link:



Contenido
Este proyecto simula el nucleo financiero de una plataforma comercial. La API fue desarrollada utilizando Python y el framework FastAPI, siguiendo una arquitectura basada en modelos(clientes, facturas y transacciones) y esquemas para validar los datos mediante Pydantic.

Avance 1: Instalacion y configuracion
Como primer paso para la creacion de este proyecto se debe:

Crear una carpeta del proyecto, y abrir con Visual Studio Code.

Ir a la pestaña superior y abrir una nueva terminal.

Abrir una terminal y ejecutar los sigueinte comandos:

Crear un entrono virtual:
windows: python -m venv .mi_env

Activar el entorno:
windows: .mi_env\Scripts\activate (debe aparecer (.mi_env) PS C:...... al inicio de la consola para confirmar que está activo)

Instalar FastAPI, ejecutando comandos en la terminal:

Digitar el siguiente comando para instalarlo completo:
pip install "fastapi[standard]"

Para ver la lista de instalacion y confirmar dependencias:
pip list --> ver lista de instalacion

Crear el archivo main.py

Se crea el archivo principal y se ejecuta con el comando -> fastapi dev main.py

Una vez ejecutado se mostararn unas lineas para poder ver la documentacion interactiva

SERVER http://127.0.0.1:8000

SERVER http://127.0.0.1:8000/docs (Para entrar al entorno grafico de Swagger)

Para detener el servidor Uvicorn, se dijita el comando en la consola: ctrl + c

Para limpiar la consola usar el comando clear

Se hace una Configuracion git: se crea un repositorio local

Se debe comprobar versiones instaladas de python y git: pip --version | python --version

Inicializar el repositorio: git init

Configurar tu identidad en git con los siguiente comandos:

git config user.name = "tu_nombre"

git config user.email = "tu_correo@ejemplo.com" (no necesita ser real)

Crear el archivo .gitignore (Archivos o carpetas que NO debe subir al repositorio), se agregaron los archivos:

.mi_env

pycache/

*.pyc

Crear el archivo requirements.txt (contiene la lista de las librerías que necesita mi proyecto para funcionar).

Comando: pip freeze > requirements.txt

Avance 2: Creacion de los commits
En la consola ejecutar los siguientes comandos para manejar versiones:

git status -> Muestra qué archivos fueron modificados, creados y estan listos para el commit. Los archivos en rojo son los modificados.

git add . -> Agrega todos los archivos modificados.

git commit -m "Mensaje del commit" -> guarda los cambios (crear commit) con mensajes especificos de los avances.

git log -> Para ver el historial de los commits creados y confirmar que se guardaron.

Avance 3: Como vincular con un repositorio GITGHUB:
Crear una cuenta en gitghub (si no se tiene una).

Configurar la cuenta de gitghub con el Visual Studio Code.

Crear repositorio en la pagina de github para subir el proyecto.

En la consola digitar digitar el comando de subida:

git push origin main --> la rama principal de mi proyecto es main.py

Avance 4: Creacion de los Endpoints
Se crearon los endpoints de Listar, Listar uno, Crear, Editar y Eliminar, comprobando sus rutas:
- Clientes: Listar_clientes, Listar_cliente, Crear_cliente, Editar_cliente, Eliminar_cliente
- Facturas: Listar_facturas, Listar_factura, Crear_factura, Editar_factura, Eliminar_factura
- Transacciones: Listar_transacciones, Listar_transaccion, Crear_transaccion, Editar_transaccion, Eliminar_transaccion.

Avance 5: Organizacion de carpetas
Se creo la carpeta principal app

Guardar archivo main.py dentro y crear archivo conexion_bd.py.

Crear subcarpetas: enrutadores - modelos.

Dentro de las dos carpetas crear 3 archivos para cada una: clientes.py, facturas.py y transacciones.py.

El arbol de carpetas queda asi:
app/
|_enrutadores/
|__clientes.py
|__facturas.py
|__transacciones.py
|_modelos
|__clientes.py
|__facturas.py
|__transacciones.py
|_conexion_bd.py
|_main.py

Avance 6: Enrutar
- Se editaron los archivos de la carpeta enrutadores (instanciar la clase ROUTER para modularizar):
        rutas_clientes = APIRouter()
        rutas_facturas = APIRouter()
        rutas_transacciones = APIRouter()
- Se creo el archivo de listas donde se importaron todos los modelos.
- Se comprobo el funcionamiento de los endpoints directamente desde /docs.
Avance 7: Conexion y Creacion a base de datos
Se debe Instalar Dependencias sqlmodel:

pip install sqlmodel

con el comando pip list, se verifica si se instalo correctamente el sql model y SQLAlchemy.

En el archivo requirements.txt se debe copiar el numero de la version instalada de sqlmodel:

sqlmodel >=0.0.39

Documentacion usada de referencia: https://sqlmodel.tiangolo.com/

Se edito el archivo conexion_bd.py:

se crea el motor para la base de datos (engine).

Se define el metodo para crear las tablas y la sesion.

Se creo inyeccion depentencias con Depends.

Se edito el archivo enrutadores/cliente.py = se editaron los enpoints de listar_cliente (FastAPI entrega una sesión de la base de datos) y
crear_clientes (se añade un cliente, se guarda y refresca automaticamente) de esta forma:
mi_sesion.add(cliente_val)
mi_sesion.commit()
mi_sesion.refresh(cliente_val)

Se agrega lista_cli = sesion.exec(select(Cliente)).all() en el enpoint de listar todos los clientes para que consulte todos los clientes que se han guardado en la base de datos y retorne los registros.

Se edito el archivo modelos/clientes.py = Se importo la conixon a sqlmodel, se le asigna un Field a los campos de las tablas para que los datos que se envien se guarden por defecto así: id: None = Field(default=None).

Se edito el archivo main.py: Dentro de la variable app se pone lifespan=crear_tablas, es decir que ejecuta crear_tablas antes de recibir una peticion, creando la BD si no existe.

Una vez corregido los archivos se creara automaticamente el archivo de base de datos con el nombre asignado en conexion_bd.py.

Para abrir la base de datos se pueden de dos formas:

En la Terminal.

Descargando SQLlite viewer en VS Code.

Se comprobo el funcionamiento de crear cliente y listar todos los clientes guardados en DB.

Avance 8: Crud completo de cliente, facturas y transacciones
Modelos y Rutas de Clientes

Se edito el archivo modulos/cliente.py:

Se añadieron Field en ClienteBase, Cliente: id con llave primaria.

Se edito el archivo enrutadores/cliente.py:

Se añadio una sesion(mi_sesion) de base de datos a listar un solo cliente, Editar un cliente y Elimiar un cliente.

Modelos y Rutas de Facturas

Se edito el archivo modulos/factura.py:

Se añadieron Field en FacturaBase, Factura: id con llave primaria y se añadio una llave foranea con cliente_id.

Se edito el archivo enrutadores/factura.py:

Se añadio una sesion(mi_sesion) de base de datos a listar una sola factura, Editar una factura y Elimiar una factura.

Modelos y Rutas de Transacciones

Se edito el archivo modulos/transacciones.py:

Se añadieron Field en TransaccionBase, Transaccion: id con llave primaria y se añadio una llave foranea con factura_id.

Se edito el archivo enrutadores/transacciones.py:

Se añadio una sesion(mi_sesion) de base de datos a listar una sola Transaccion, Editar una transaccion y Elimiar una transaccion de la DB.