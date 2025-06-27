from database.connection import ConnectionFactory
from schemas.usuario import UsuarioOut, UserCreate
def obtener_usuarios():
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,nombre,email,contrasena FROM usuarios")
    rows = cursor.fetchall()
    return [UsuarioOut(
        id=row[0],
        nombre=row[1],
        email=row[2],
        contrasena=row[3]
    ) for row in rows]

def consultar_usuarioId(id:int):
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,nombre,email,contrasena FROM usuarios where id=?",id)
    rows = cursor.fetchone()
    conn.close()
    return UsuarioOut(
        id=rows[0],
        nombre=rows[1],
        email=rows[2],
        contrasena=rows[3]
    ) 
 #1.construi método en el servicio   
def consultar_usuarioEmailService(email:str):
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,nombre,email,contrasena FROM usuarios where email=?",email)
    rows = cursor.fetchone()
    conn.close()
    return UsuarioOut(
        id=rows[0],
        nombre=rows[1],
        email=rows[2],
        contrasena=rows[3]
    ) 
    

def service_usuario_crear(usuario: UserCreate) -> UsuarioOut:
    conn = ConnectionFactory.create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO usuarios (nombre, email, contrasena)
        OUTPUT INSERTED.id, INSERTED.nombre, INSERTED.email
        VALUES (?, ?, ?)
    """, (usuario.nombre, usuario.email, usuario.contrasena))

    row = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return UsuarioOut(
        id=row.id,
        nombre=row.nombre,
        email=row.email,
        contrasena=None
    )