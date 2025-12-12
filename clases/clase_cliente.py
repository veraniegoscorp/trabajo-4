from .clase_persona import persona
class cliente(persona):
    def __init__(self,nombre, email, rut, nivel,password,id_cliente=None): # type: ignore
        super().__init__(nombre, email, rut) # type: ignore
        self.id_cliente = id_cliente
        self.nivel = nivel
        self.password = password


    def tiene_id(self):
        return self.id_cliente is not None

    def AplicarDescuento(self):
        return 0.90 if self.nivel == "estudiante" else 0.0
#aqui se representa en el diagrama el extend como la relacion padre-hijo con persona
