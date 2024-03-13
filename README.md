# SPORTAPP-Arquitecturas-ágiles-de-software

Este repositorio utiliza Docker Compose para gestionar sus contenedores. Sigue las instrucciones a continuación para ejecutar el programa en tu entorno local.

## Requisitos Previos

Asegúrate de tener instalado Docker y Docker Compose en tu sistema.

## Pasos para Ejecutar

1. **Clonar el Repositorio**: `git clone https://github.com/japago25andes/SportApp-Equipo-18.git`

2. **Navegar al Directorio del Proyecto**: `cd SportApp-Equipo-18\plan_deportivo`

3. **Configuración del Entorno**: Asegúrate de configurar cualquier variable de entorno necesaria en el archivo `.env`.

4. **Construir la Imagen Docker**: `docker-compose build`

5. **Ejecutar el Programa**: `docker-compose up`

6. **Acceder al Programa**: Una vez que el programa esté en funcionamiento, podrás acceder a él desde tu navegador web o utilizando cualquier cliente necesario.

para ejecutar la prueba para el plan_deportivo
```
curl --location 'http://localhost:8080/plan_deportivo/health' \
--header 'Authorization: Bearer dk9KOTM2ZkR1TmxVQVFCSjl5U1I3bEhWMjhBbHRQNUM6WA==' \
--data ''
```

para ejecutar la prueba para deportistas
```
curl --location 'http://localhost:8080/deportistas/health/5002' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer dk9KOTM2ZkR1TmxVQVFCSjl5U1I3bEhWMjhBbHRQNUM6WA==' \
--data '{
"nombre":"deportista uniandes"
}'
```


7. **Detener la Ejecución**: `docker-compose down` o `Control+C` en la terminal donde se ejecuto docker

## Contribución y Problemas

Si encuentras algún problema con el programa o deseas contribuir con mejoras, no dudes en abrir un issue o enviar un pull request a este repositorio.
