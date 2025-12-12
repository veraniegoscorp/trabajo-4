import oracledb
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="db.env")
#cargamos las variables desde el .env

# Obtener las variables
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
dsn = os.getenv("DB_DSN")

def obtener_conexion():
    try :
        conexion=oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        print("Conexión exitosa a la base de datos Oracle")
        return conexion
    except oracledb.Error as e:
        print(f"Error de conexión a la base de datos Oracle: {e}")
        return None
if __name__ == "__main__":
    obtener_conexion()