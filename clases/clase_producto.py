class producto():
    def __init__(self,codigo,nombre,precio_neto): # type: ignore
        self.codigo=int(codigo) # type: ignore
        self.nombre=str(nombre) # type: ignore
        self.precio_neto=int(precio_neto) # type: ignore
        self.iva=0.19
    def calcular_iva(self):
        return self.precio_neto+(self.precio_neto*self.iva)
                  
    def __str__(self):
        return f"{self.codigo}.{self.nombre}-_-{self.precio_neto}"
    