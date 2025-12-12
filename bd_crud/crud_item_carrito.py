import oracledb
from conexion_oracle import obtener_conexion
def insertar_item_carrito(id_item, id_carrito, codigo_producto, cantidad, subtotal_item):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    
    try:
        # Usamos la secuencia para generar ID automático
        cursor.execute("SELECT seq_item.NEXTVAL FROM DUAL")
        id_item = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO ITEM_CARRITO (
                ID_ITEM, ID_CARRITO, CODIGO_PRODUCTO, CANTIDAD, SUBTOTAL_ITEM
            ) VALUES (
                :id_item, :id_carrito, :codigo_producto, :cantidad, :subtotal_item
            )
        """, {
            "id_item": id_item,
            "id_carrito": id_carrito,
            "codigo_producto": codigo_producto,
            "cantidad": cantidad,
            "subtotal_item": subtotal_item
        })
        conexion.commit()
        print(f"Item carrito creado con éxito! → ID: {id_item}")
        return id_item
        
    except oracledb.DatabaseError as e:
        print(f"Error al insertar item carrito: {e}")
        conexion.rollback()
        #desasemos los cambios si no se pudo insertar
        return None
    finally:
        cursor.close()
        conexion.close()




def obtener_items_carrito():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM ITEM_CARRITO")
        items = cursor.fetchall()
        for I in items:
            print(I)

    except oracledb.DatabaseError as e:
        print(f"Error en la consulta: {e}")
        return None

    finally:
        cursor.close()
        conexion.close()






def cambiar_cantidad_item(id_item, nueva_cantidad, nuevo_subtotal):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE ITEM_CARRITO
            SET CANTIDAD = :nueva_cantidad,
                SUBTOTAL_ITEM = :nuevo_subtotal
            WHERE ID_ITEM = :id_item
        """, {
            "nueva_cantidad": nueva_cantidad,
            "nuevo_subtotal": nuevo_subtotal,
            "id_item": id_item
        })
        conexion.commit()
        print(f"Cantidad y subtotal del item {id_item} actualizados con éxito!")

    except oracledb.DatabaseError as e:
        print(f"Error al actualizar item carrito: {e}")
        conexion.rollback()

    finally:
        cursor.close()
        conexion.close()






def eliminar_item_carrito(id_item):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            DELETE FROM ITEM_CARRITO
            WHERE ID_ITEM = :id_item
        """, {
            "id_item": id_item
        })
        conexion.commit()
        print(f"Item carrito {id_item} eliminado con éxito!")

    except oracledb.DatabaseError as e:
        print(f"Error al eliminar item carrito: {e}")
        conexion.rollback()

    finally:
        cursor.close()
        conexion.close()

