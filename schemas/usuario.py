from pydantic import BaseModel,  EmailStr
from typing import Optional
from enum import Enum

class UserCreate(BaseModel):
    nombre: str
    email: EmailStr
    contrasena: str
    
class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: Optional[str]
    contrasena: Optional[str]


