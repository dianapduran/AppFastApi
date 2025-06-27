from fastapi import APIRouter
from typing import List
from schemas.contenido import ContenidoOut, ClsSerieOut, ClsSerieCrear, ClsPeliculaCrear, ClsPeliculaOut
from services.contenidos_service import obtener_contenidos, consultar_TipoContenidoService, service_serie_crear, service_pelicula_crear
router = APIRouter()

@router.get("/contenidos", response_model=List[ContenidoOut])
def listar_contenidos():
    return obtener_contenidos()

@router.get("/tipo_contenido/{tipocontenido}", response_model=List[ContenidoOut])
def listar_TipocontenidosRouter(tipocontenido:str):
    return consultar_TipoContenidoService(tipocontenido)

@router.post("/crear_serie", response_model= ClsSerieOut)
def MetSerieCrearRoute(serie:ClsSerieCrear):
    return service_serie_crear(serie)

@router.post("/crear_pelicula", response_model= ClsPeliculaOut)
def MetPeliculaCrearRoute(pelicula:ClsPeliculaCrear):
    return service_pelicula_crear(pelicula)