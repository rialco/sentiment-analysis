# Proyecto final - Analitica de sentimientos 

Proyecto de analisis de sentimientos en Twitter. La solución permite tener un servidor web al cual se pueden hacer consultas en tiempo real a twitter y analizar los tweets recopilados.

## Despliegue local
### Requisitos 

1. Docker instalado

### Instrucciones

La solución puede desplegarse utilizando docker. Los pasos para utilizarla localmente son los siguientes:

1. Abrir la terminal de comandos en el directorio del proyecto.
1. Ejecutar el comando `docker-compose up --build`.

## Arquitectura

Solución orientada a micro-servicios. 

### Sentiment Analysis API

- REST API para la recopilación de datos y solicitud de eventos.

### Neural Network

- Aplicación en Python para el entrenamiento y clasificación de frases

### Event Stream

- Stream de comunicación entre microservicios basado en Redis.

### PostgreSQL Database

## Información adicional
- Proyecto de grado
- Universidad del Norte