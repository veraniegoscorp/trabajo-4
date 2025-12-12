from .clase_producto import producto
class item_carrito():
    def __init__(self,producto:'producto',cantidad): # type: ignore
        self.producto=producto
        self.cantidad=int(cantidad) # type: ignore
        self.subtotal=self.calcular_subtotal()

    def calcular_subtotal(self):
        return self.producto.calcular_iva()*self.cantidad
#item carrito es dependiente de producto porque lo usa osea el self.producto=producto hace referencia a eso
#no hereda ni es parte permanente de el pero lo usa de ahi la dependencia

#la agregacion es porque el producto puede existir por si solo mientras que carrito lo nesesita para existir

