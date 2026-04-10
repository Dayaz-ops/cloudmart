from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import datetime

from app.database import products_container

app = FastAPI()

@app.get("/health")
def health_check():
    try:
        list(products_container.query_items(
            query="SELECT * FROM c",
            enable_cross_partition_query=True
        ))
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.datetime.utcnow().isoformat()
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )

@app.get("/api/v1/products")
def get_products():
    items = list(products_container.query_items(
        query="SELECT * FROM c",
        enable_cross_partition_query=True
    ))
    return items

app.mount("/", StaticFiles(directory="static", html=True), name="static")
