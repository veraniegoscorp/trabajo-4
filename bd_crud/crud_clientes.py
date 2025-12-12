import oracledb
from .conexion_oracle import obtener_conexion


def insertar_cliente(rut, nombre, email, contrasena_hash, nivel="General"):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        # Usamos la secuencia para generar ID automático
        cursor.execute("SELECT seq_cliente.NEXTVAL FROM DUAL")
        id_cliente = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO CLIENTE (
                ID_CLIENTE, RUT, NOMBRE, EMAIL, 
                CONTRASENA_HASH, NIVEL, FECHA_REGISTRO
            ) VALUES (
                :id, :rut, :nombre, :email, 
                :hash, :nivel, SYSDATE
            )
        """, {
            "id": id_cliente,
            "rut": rut,
            "nombre": nombre,
            "email": email,
            "hash": contrasena_hash,
            "nivel": nivel if nivel in ("General", "estudiante") else "General",
        })
        
        conexion.commit()
        print(f"Cliente creado con éxito! → ID: {id_cliente}")
        return id_cliente
        
    except oracledb.DatabaseError as e:
        print(f"Error al insertar cliente: {e}")
        conexion.rollback()
        return None
    finally:
        cursor.close()
        conexion.close()


def seleccionar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM CLIENTE")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)

    except oracledb.DatabaseError as e:
        print(f"Error en la consulta: {e}")
        return []

    finally:
        cursor.close()
        conexion.close()


def actualizar_email_cliente(id_cliente, nuevo_email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE CLIENTE
            SET EMAIL = :nuevo_email
            WHERE ID_CLIENTE = :id_cliente
        """, {
            "nuevo_email": nuevo_email,
            "id_cliente": id_cliente
        })
        conexion.commit()
        print("Email del cliente actualizado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al actualizar el email del cliente: {e}")

    finally:
        cursor.close()
        conexion.close()


def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            DELETE FROM CLIENTE
            WHERE ID_CLIENTE = :id_cliente
        """, {
            "id_cliente": id_cliente
        })
        conexion.commit()
        print("Cliente eliminado correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar el cliente: {e}")

    finally:
        cursor.close()
        conexion.close()

