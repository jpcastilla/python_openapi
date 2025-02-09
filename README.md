# python_openapi

## Descripción
Este proyecto es una API de ejemplo creada con FastAPI que genera automáticamente la documentación OpenAPI.

## Instalación
Para instalar las dependencias necesarias, ejecuta el siguiente comando:
```sh
pip install fastapi uvicorn
```
## Ejecución
Para iniciar el servidor, ejecuta el siguiente comando:
```sh
uvicorn main:app --reload
```

## Endpoints
La API expone los siguientes endpoints:  
GET /items/{item_id}: Obtiene un ítem por su ID.

## Documentación
La documentación de la API está disponible en los siguientes enlaces:  
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Ejemplo de Uso
Para obtener un ítem, realiza una solicitud GET al siguiente endpoint:
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/items/1' \
  -H 'accept: application/json'
```