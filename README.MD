# Proyecto final - Analitica de sentimientos 

Proyecto de analisis de sentimientos en Twitter. La solución permite proporcionar un servidor web a los usuarios en el cual se pueden hacer consultas en tiempo real a twitter y analizar los tweets recopilados.

## Despliegue local
### Requisitos 

1. Docker
1. Postman
1. Git

### Instrucciones

La solución puede desplegarse utilizando docker. Los pasos para utilizarla localmente son los siguientes:

En un inicio es necesario descargar y configurar el proyecto. Para esto es necesario seguir las siguientes instrucciones:

1. Ejecutar el comando `git clone <url del proyecto>` en el directorio donde quieres descargar el proyecto
1. Dentro de la carpeta existe un directorio llamado `sentiment_api_service`. En este directorio existe un archivo .env.example
1. Duplicar el archivo previamente mencionado y colocarle el nombre `.env`
1. Este servicio se puede ejecutar con 2 configuraciones distintas. En producción y en testing. Para correrlo en testing puede dejarlo tal y como esta, esta configuración utilizara datos de prueba. Para correrlo en producción: 
    - **Tienes un token de twitter**: Colocarlo en el campo `BEARER_TOKEN` y cambiar el valor de `ENVIRONMENT` por `PRODUCTION`.
    - **No tienes un token de twitter**: Contactarse con nosotros para proporcionarlo.

Una vez configurado puede seguir las siguientes instrucciones para el despliegue local:

1. Desplazarse al directorio padre: `sentiment-analysis`
1. Ejecutar el comando `docker-compose up --build` en ese directorio.

### Pruebas
#### Requerimientos para pruebas

Esta solución actualmente cuenta con 3 simples pasos que el usuario debe ejecutar para poder consumir el servicio que ofrecemos. Estos pasos los podemos dividir de la siguiente manera y todos son mediante llamados a la API:

#### 1. Recolección de datos

Para la recopilación de datos tenemos dos posibles fuentes de información. Los hashtags o las menciones. El usuario puede usar nuestra API para recopilar los tweets que contengan un hashtag en especifico o una mención a otro usuario en su defecto. (Para ejecutar este paso puede usar Postman, su explorador de preferencia o alguna otra aplicación que pueda hacer GET requests)

Para recopilar tweets que mencionen a un usuario hay que hacer un GET request al siguiente endpoint:

`localhost:3000/tweets/user/:usuario` - remplazar `:usuario` por el nombre del usuario que quiere buscar, ej. sergio_fajardo.

Por otro lado, para recopilar tweets de un hashtag en especifico hay que hacer un GET request al siguiente endpoint:

`localhost:3000/tweets/toppic/:topic` - remplazar `:topic` por el nombre del usuario que quiere buscar, ej. sergio_fajardo.


**IMPORTANTE**: Este paso retorna los tweets serializados con la información que consideramos importante para el proximo analisis. Al mismo tiempo guardara los tweets recopilados en la base de datos para proximos usos.

#### 2. Solicitud de análisis.

Para la solicitud de análisis se debe de hacer un POST request al siguiente endpoint:

`localhost:3000/sentiment/analysis/:subject` - reemplazar `:subject` por el hashtag o usuario que se quiere analizar.

**IMPORTANTE**: Este paso es totalmente asincrono, es decir, la solicitud se generara en el servidor y empezara a clasificar los tweets que contengan el topico a analizar. 


### 3. Recopilación del análisis.

Para obtener los datos resultantes del análisis hay que realizar un GET request al siguiente endpoint:

`localhost:3000/sentiment/analysis/:subject` - reemplazar `:subject` por el hashtag o usuario que se quiere analizar.

**IMPORTANTE**: Para ejecutar este paso se debieron haber ejecutado los dos pasos anteriores con el mismo usuario o topico para que exista información en la base de datos.
    
***INFORMACION ADICIONAL***: En el directorio del proyecto existe una carpeta con el nombre `demo`. En esta carpeta hay unos scripts escritos en python y javascript que utilizan la información proporcionada para generar otros análisis en base a la información proporcionada.


## Arquitectura
La arquitectura de la solución propuesta esta orientada a micro-servicios. Esto permite que sea altamente escalable y desacoplada, implicando asi un gran potencial para la evolución de la solución.
- #### Sentiment Analysis API
    REST API para la recopilación de datos y solicitud de eventos. El desarrollo de este servicio fue realizado teniendo la metodologia DDD en mente. Esto implica que el codigo seguira un patron para la implementación de funciones nuevas y por consiguiente mantendra una alta mantenibilidad.
- #### Neural Network
    Aplicación en Python para el entrenamiento y clasificación de frases. Se desarrollo una red neuronal teniendo en cuenta el patron de POO utilizando librerias tales como:

    - Tensorflow
    - Keras
    - NLTK
    - Pandas
    
    Entre otras liberias para el correcto funcionamiento dentro del cluster de servicios.
- #### Event Stream
    Stream de comunicación entre microservicios basado en Redis.
- #### PostgreSQL Database
    Base de datos relacional utilizada para la persistencia de datos.

## Información adicional
- Proyecto de grado
- Universidad del Norte