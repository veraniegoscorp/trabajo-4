"""esta es la clase de persona para el proyecto"""
"""esta cuenta con: una clase padre en este caso persona que hereda a su clase hija en este caso cliente"""
class persona:
    def __init__(self,nombre,email,rut):
        #nombre eh email devuelven srt y rut un float
        self.nombre=str(nombre)
        self.email=str(email)
        self.rut=str(rut)
    def get_resume(self):
        #convierte los datos en str
        return f"{self.nombre},{self.email},{self.rut}"