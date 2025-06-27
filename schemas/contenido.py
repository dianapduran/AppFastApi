from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TipoContenido(str, Enum):
    pelicula = 'pelicula'
    serie = 'serie'

class ContenidoOut(BaseModel):
    id: int
    titulo: str
    descripcion: Optional[str]
    fecha_lanzamiento: Optional[str]
    tipo_contenido: TipoContenido
  
 # para crear contenido   
class Contenido(BaseModel):
    titulo: str
    descripcion: Optional[str]
    fecha_lanzamiento: Optional[str]
    tipo_contenido: TipoContenido
  
 # Serie   
 ## para crear contenido serie   
class ClsSerieCrear(Contenido):
    cantidad_temporadas: int

 ## para consultar contenido serie   
class ClsSerieOut(ContenidoOut):
    cantidad_temporadas: int
    
    

        
