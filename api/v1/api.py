from fastapi import APIRouter
from api.v1.endpoints import artigo, usuario

api_router = APIRouter()
api_router.include_router(artigo.router, prefix='/cursos', tags=['cursos'])