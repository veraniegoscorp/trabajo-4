import oracledb
from .conexion_oracle import obtener_conexion
def insertar_carrito(id_cliente, fecha_creacion,subtotal,descuento_aplicado,total):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        # Usamos la secuencia para generar ID automático
        cursor.execute("SELECT seq_carrito.NEXTVAL FROM DUAL")
        id_carrito = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO CARRITO (
                ID_CARRITO, ID_CLIENTE, FECHA_CREACION, SUBTOTAL, DESCUENTO_APLICADO, TOTAL
            ) VALUES (
                :id_carrito, :id_cliente, SYSDATE, :subtotal, :descuento_aplicado, :total
            )
        """, {
            "id_carrito": id_carrito,
            "id_cliente": id_cliente,
            "subtotal": subtotal,
            "descuento_aplicado": descuento_aplicado,
            "total": total
        })
        conexion.commit()
        print(f"Carrito creado con éxito! → ID: {id_carrito}")
        return id_carrito
        
    except oracledb.DatabaseError as e:
        print(f"Error al insertar carrito: {e}")
        conexion.rollback()
        #desasemos los cambios si no se pudo insertar
        return None
    finally:
        cursor.close()
        conexion.close()


        

def obtener_carritos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM CARRITO")
        carritos = cursor.fetchall()
        for I in carritos:
            print(I)

    except oracledb.DatabaseError as e:
        print(f"Error en la consulta: {e}")
        return None

    finally:
        cursor.close()
        conexion.close()






def actualizar_fecha_creacion(id_carrito, nueva_fecha_creacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE CARRITO
            SET FECHA_CREACION = :nueva_fecha_creacion
            WHERE ID_CARRITO = :id_carrito
        """, {
            "nueva_fecha_creacion": nueva_fecha_creacion,
            "id_carrito": id_carrito
        })
        conexion.commit()
        print("Fecha de creación del carrito actualizada correctamente.")

    except oracledb.DatabaseError as e:
        print(f"Error al actualizar la fecha de creación del carrito: {e}")

    finally:
        cursor.close()
        conexion.close()







def eliminar_carrito(id_carrito):
    conexion= obtener_conexion()
    cursor= conexion.cursor()
    try:
        cursor.execute("""
            delete from carrito
            where id_carrito= :id_carrito
        """, {
            "id_carrito": id_carrito
        })
        conexion.commit()
        print("Carrito eliminado correctamente.")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar el carrito: {e}")

    finally:
        cursor.close()
        conexion.close()