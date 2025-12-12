from bd_crud.crud_clientes import *
from bd_crud.crud_carrito import *
from clases.clase_cliente import cliente


def crear_nuevo_cliente():
    print("=== Registro de Nuevo Cliente ===")
    nombre = input("Nombre: ")
    email = input("Email: ")
    rut = input("RUT (formato 12.345.678-9): ")
    nivel = input("Nivel (General/estudiante): ").capitalize()
    if nivel not in ["General", "Estudiante"]:
        nivel = "General"
    contrasena_hash = input("Contraseña: ")

    try:
        id_generado = insertar_cliente(rut, nombre, email, contrasena_hash, nivel)
        
        nuevo_cliente = cliente(nombre, email, rut, nivel, contrasena_hash, id_generado)
        print(f"Cliente creado con ID: {id_generado}")

    except Exception as e:
        print(f"Error al crear cliente: {e}")






if __name__ == "__main__":
    # Menú simple para pruebas
    while True:
        print("\n1. Crear cliente")
        print("2. Listar clientes")
        print("3. Salir")
        op = input("Opción: ")
        if op == "1":
            crear_nuevo_cliente()
        elif op == "2":
            seleccionar_clientes()
        elif op == "3":
            break
