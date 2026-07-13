from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime

# El decorador @property proviene de Python y sirve para convertir un método de una clase en una propiedad de solo lectura.
# Validación Pydantic v2, @computed_field es un decorador que te permite definir propiedades o métodos que se calculan dinámicamente a partir de otros campos y se incluyen automáticamente en la respuesta JSON de tu API.
# getattr() es una función nativa de Python. Sirve  para obtener el valor de un atributo o propiedad de un objeto de forma dinamica.


# Crear el modelo transacciones(id, fecha, vr_total, cliente)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #cliente: Cliente #esta es la relacion con el cliente(objeto)
    #transacciones: list[Transaccion] = []
    
    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        
        # 1. Buscamos el atributo de forma segura
        transacciones = getattr(self, "transacciones", None)
        
        # 2. Si es None (como al crear), devolvemos 0.0 de inmediato
        if transacciones is None:
            return total_factura
            
        # 3. Si existen, recorremos la variable local "transacciones" (¡sin el self. adelante!)
        for transaccion in transacciones:
            total_factura += transaccion.vr_unitario * transaccion.cantidad
            
        return total_factura


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear relaciones virtuales con cliente, transacciones - NO en la bd
    cliente: Cliente = Relationship(back_populates="factura")
    transacciones: list[Transaccion] = Relationship(back_populates="factura")
    
    
#crear modelo para mostrar al usuario o el cliente
class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer
    #pero no es recomendable, por las buenas practicas  
    # transacciones: list[Transaccion] = []
    
    
class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []
    