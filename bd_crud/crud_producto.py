import oracledb
from conexion_oracle import obtener_conexion
def insertar_producto(codigo, nombre, precio_neto,estado): # type: ignore
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor() # type: ignore
        cursor.execute(""" 
            INSERT INTO PRODUCTO (
                CODIGO,
                NOMBRE,
                PRECIO_NETO,
                ESTADO
            ) VALUES (
                :codigo,
                :nombre,
                :precio_neto,
                :estado
            )
        """, {
            "codigo": codigo,
            "nombre": nombre,
            "precio_neto": precio_neto,
            "estado": estado, 
        })

        conexion.commit()
        print("Producto insertado correctamente")
    except oracledb.DatabaseError as e:
        print(f"Error al insertar  : {e}")

    finally:
        cursor.close()
        conexion.close()








def obtener_productos():
    try:
        conexion= obtener_conexion()
        cursor=conexion.cursor() # type: ignore
        cursor.execute("select * from PRODUCTO")
        productos=cursor.fetchall()
        for i in productos:
            print(i)
    except oracledb.DatabaseError as e:
        print(f"Error al obtener los productos: {e}")
    finally:
        cursor.close()
        conexion.close()









def cambiar_precio_producto(codigo, nuevo_precio):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor() # type: ignore
        cursor.execute("""
            UPDATE PRODUCTO
            SET PRECIO_NETO = :nuevo_precio
            WHERE CODIGO = :codigo
        """, {
            "nuevo_precio": nuevo_precio,
            "codigo": codigo
        })

        conexion.commit()
        print("Precio del producto actualizado correctamente")
    except oracledb.DatabaseError as e:
        print(f"Error al actualizar el precio del producto: {e}")

    finally:
        cursor.close()
        conexion.close()




def eliminar_producto(codigo):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor() # type: ignore
        cursor.execute("""
            DELETE FROM PRODUCTO
            WHERE CODIGO = :codigo
        """, {
            "codigo": codigo
        })

        conexion.commit()
        print("Producto eliminado correctamente")
    except oracledb.DatabaseError as e:
        print(f"Error al eliminar el producto: {e}")

    finally:
        cursor.close()
        conexion.close()