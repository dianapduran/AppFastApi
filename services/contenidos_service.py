from database.connection import ConnectionFactory
from schemas.contenido import ContenidoOut, Contenido, ClsSerieCrear, ClsSerieOut

def obtener_contenidos():
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descripcion, fecha_lanzamiento, tipo_contenido FROM contenidos")
    rows = cursor.fetchall()
    return [ContenidoOut(
        id=row[0],
        titulo=row[1],
        descripcion=row[2],
        fecha_lanzamiento=str(row[3]) if row[3] else None,
        tipo_contenido=row[4]
    ) for row in rows]
    
     #1.construi método en el servicio   
def consultar_TipoContenidoService(tipocontenido:str):
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,titulo,descripcion,fecha_lanzamiento, tipo_contenido FROM contenidos where tipo_contenido=?",tipocontenido)
    rows = cursor.fetchall()
    conn.close()
    return [ContenidoOut(
        id=row[0],
        titulo=row[1],
        descripcion=row[2],
        fecha_lanzamiento=str(row[3]) if row[3] else None,
        tipo_contenido=row[4]
    ) for row in rows]
    
## Serie
def service_serie_crear(ObjSerie: ClsSerieCrear) -> ClsSerieOut:
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contenidos (titulo, descripcion, fecha_lanzamiento, tipo_contenido)
        OUTPUT INSERTED.id 
        VALUES (?, ?, ?, ?)
    """, (ObjSerie.titulo, ObjSerie.descripcion, ObjSerie.fecha_lanzamiento, ObjSerie.tipo_contenido))
#OUTPUT INSERTED.id  consulta el id generado en la bd

    id_generado = cursor.fetchone()[0]
    cursor.execute("""
        INSERT INTO series (contenido_id, cantidad_temporadas)
        VALUES (?, ?)
    """, (id_generado, ObjSerie.cantidad_temporadas))
    conn.commit()
     
    cursor.close()
    conn.close()

    return ClsSerieOut(
        id=id_generado,
        titulo=ObjSerie.titulo,
        descripcion=ObjSerie.descripcion,
        fecha_lanzamiento=ObjSerie.fecha_lanzamiento,
        tipo_contenido = ObjSerie.tipo_contenido,
        cantidad_temporadas=ObjSerie.cantidad_temporadas        
    )