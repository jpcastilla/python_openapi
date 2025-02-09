from fastapi import FastAPI

app = FastAPI(
    title="Mi API",
    description="Esta es una API de ejemplo que genera automáticamente la documentación OpenAPI.",
    version="1.0.0"
    """
    uvicorn main:app --reload   to launch the server CNTRL + C to stop
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc
    
    OpenAPI JSON: http://127.0.0.1:8000/openapi.json
    """
)

@app.get("/items/{item_id}", summary="Obtiene un ítem", response_description="El ítem solicitado")
def read_item(item_id: int):
    """
    Obtiene la información del ítem con el ID especificado.
    """
    return {"item_id": item_id, "name": f"Item {item_id}"}
