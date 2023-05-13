class Clientes:
  
    def __init__(self, idcliente, nombre, apellido, correo, fecha_registro, saldo):
        self.idcliente=idcliente
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.fecha_registro=fecha_registro
        self.saldo=saldo

    def mostrar_saldo(self):
        agregar=int(input("monto para agregar: "))
        print(f"el nuevo saldo de {self.nombre}{self.apellido} tras haber agregado {agregar} es de {agregar+self.saldo}")



class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.sku=sku
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.impuesto=1.19

    def mostrar_producto(self,producto):
        print(f" producto categoria {producto.categoria} costó en total{producto.valor_neto * self.impuesto}")   



class Vendedor:
    def __init__(self, run, nombre, apellido, seccion):
        self.run=run
        self.nombre=nombre
        self.apellido=apellido
        self.seccion=seccion
        self.comision=0.05
        
    def venta(self,producto):
        neto=producto.valor_neto
        com_prod=neto*self.comision
        print(f"la comisión de la venta es {com_prod}, de codigo {producto.sku} de producto {producto.categoria}")
        producto.stock=producto.stock-1
        print(f" el stock actual es de {producto.stock}")


class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais):
        self.rut=rut
        self.nombre=nombre_legal
        self.razon_social=razon_social
        self.pais=pais
        
    def rel_producto(self,producto):
        print(f"nosotros {self.razon_social} hemos vendido el producto {producto.categoria}, {producto.proveedor}")

#cliente creado
juan=Clientes(1, "juan" , "rojas","gmail",25-5-1992, 5000)
juan.mostrar_saldo()

#productos creados
zapatilla=Producto("sku1","j","zapatilla", "nike", 10, 50000)
chalas=Producto("sku2", "p","chalas","wq",5,10000)
neto=5000
zapatilla.mostrar_producto(zapatilla)
#vendedor
pepito=Vendedor(12,"juna", "style", 8)
#stock y venta producto zapatilla
print(f"el stock zapatillas es de {zapatilla.stock}")
pepito.venta(zapatilla)
#pepito.venta(chalas)
#comentario clase proveedor
prov=Proveedor(99999999-1, "Nike Air Max Plus", "Nike", "EEUU")
prov.rel_producto(producto=zapatilla)