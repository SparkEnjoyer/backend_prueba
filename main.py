from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite peticiones desde el frontend (ajusta la URL al dominio del frontend si quieres seguridad)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI"}
