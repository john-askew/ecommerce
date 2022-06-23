import re


class Carro:
    def __init__(self, request):
        self.request = request  
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = Carro
    
    def agregar(self, producto):
        if str(producto.id not in self.carro.keys()):
            self.carro[producto.id] = {
                'producto_id' :producto.id,
                'name': producto.nombre,
                'cantidad': 1,
                'precio': str(producto.precio),
                'imagen': producto.imagen.url
            }

        else: 
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1
                    self.guardar()
                    break

    def guardar(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar()

    def disminuir(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad'] - 1
                if value['cantidad'] < 1:
                    self.eliminar(producto)
                else:
                    self.guardar()
                break
            else:
                print("No existe el Producto")


    def limpiar(self):
        self.session['carro'] = {}
        self.session.modified = True