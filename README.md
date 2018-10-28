# ⏳ PythonDay México 2018

Repo con cuenta regresiva para el PythonDay México 2018 a realizarse en Guadalajara.

Info: [http://pythonday.mx/](http://pythonday.mx/)

## Contribuye

[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/0)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/0)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/1)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/1)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/2)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/2)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/3)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/3)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/4)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/4)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/5)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/5)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/6)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/6)[![](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/images/7)](https://sourcerer.io/fame/RodolfoFerro/RodolfoFerro/CountdownPythonDayMx2018/links/7)

La idea es crear un backend sencillo con [Flask](http://flask.pocoo.org/) para desplegar un reloj con cuenta regresiva.

Dejaré la `app.py` para el server en Flask ya hecho, que renderice solamente el archivo `index.html` (el cual estará vacío). Cualquier contribución es bienvenida mediante un *Pull Request*.

### TODO:
- Checar issues en el repo
- ¿Alguno extra?


## Instalación

A continuación te ofrecemos dos sencillas instalaciones de requerimientos para tu sistema, con [*pip*](https://pip.pypa.io/en/stable/installing/) y con [*Anaconda*](https://www.anaconda.com/download/).

### Instalación con `pip` y `virtualenv`

Para instalar los requerimientos en un entorno virtual de Python:

    # Clonar el repositorio
    $ git clone git@github.com:RodolfoFerro/CountdownPythonDayMx2018.git
    $ cd CountdownPythonDayMx2018

    # Crear el entorno virtual
    $ virtualenv env
    $ source env/bin/activate

    # Instalar requerimientos
    $ pip install -r src/requirements/base.txt

### Instalación con `conda env`

    # Clonar el repositorio
    $ git clone git@github.com:RodolfoFerro/CountdownPythonDayMx2018.git
    $ cd CountdownPythonDayMx2018

    # Crear el entorno conda
    $ conda env create -f src/environment.yml
    
    # Activar el entorno conda
    $ conda activate countdown_pymx_2018

### Instalación con `Docker`

Es necesario tener [Docker](https://docs.docker.com/engine/installation/) y [Docker Compose](https://docs.docker.com/compose/install/) instalados previamente

    $ docker-compose up

Abrir navegador en ```0.0.0.0:8000```
