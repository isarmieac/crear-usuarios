
# Proyecto para crear usuarios

_Este proyecto contempla una página web donde se pueden crear usuarios fácilmente_



## Componentes 📋
_La página estará compuesta de los siguientes componentes:_

* Formulario: Donde se deben ingresar los datos.
* Tabla usuarios actuales: Donde encontrarán una lista de los usuarios actuales.


## Construido con 🛠️

_Herramientas del proyecto_

* [Django](http://www.dropwizard.io/1.0.2/docs/) - El framework web para perfeccionistas con plazos
* [Python 3](https://www.python.org/doc/) - Usado para los request

## Instalar proyecto en la computadora
Para instalar desde git debes poner el siguiente enlace en la consola:

```
git clone https://github.com/isarmieac/crear-usuarios.git
```

Una vez copiado, debes colocar como lugar de trabajo la carpeta crear-usuario:

```
cd crear-usuario
```
Dependiendo del hosting, deberás ir al archivo crear_usuario/setting.py y modificar la siguiente línea:

```
ALLOWED_HOSTS = ["162.243.165.69","microdatos.xyz"]
```

Luego, deberás ir al archivo usuarios/views.py y modificar el usuario y la contraseña por los de la api, y el id del perfil de coordinador por el nuevo id (ver más información en el código.

Finalmente deberás migrar los cambios con 

```
python manage.py migrate 
```
y correr el servidor en el host deseado:
```
python manage.py runserver 162.243.165.69:1234
```
