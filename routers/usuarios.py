from fastapi import APIRouter
from typing import List
from schemas.usuario import UsuarioOut, UserCreate
from services.usuarios_service import  service_usuario_crear, obtener_usuarios,consultar_usuarioId, consultar_usuarioEmailService

router = APIRouter()

@router.get("/usuarios", response_model=List[UsuarioOut])
def listar_usuarios():
    return obtener_usuarios()

@router.get("/usuario/{id}", response_model=UsuarioOut)
def consultar_usuario(id:int):
    return consultar_usuarioId(id)

# 2. definir endpoint para consultar usuario por email atraves del endpoint
@router.get("/usuarioEmail/{email}", response_model=UsuarioOut)
#defino funcion que va a llamar a la ruta, recibe como parametro desde la URL el email
def consultar_usuarioEmailRouter(email:str):
    return consultar_usuarioEmailService(email)

@router.post("/crear_usuario", response_model=UsuarioOut)
def ruta_usuario_crear(ObjetoUsuario:UserCreate):
    return service_usuario_crear(ObjetoUsuario)