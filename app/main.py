from fastapi import FastAPI, HTTPException, status
from .modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from .modelos.facturas import Factura, FacturaCrear, FacturaEditar
from .modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from .enrutadores.clientes import rutas_clientes
from .enrutadores.facturas import rutas_facturas
from .enrutadores.transacciones import rutas_transacciones

app = FastAPI()


lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# incluir ruta de clientes
app.include_router(rutas_clientes, tags=["Clientes"])

# incluir ruta de facturas
app.include_router(rutas_facturas, tags=["Facturas"])

# incluir ruta de transacciones
app.include_router(rutas_transacciones, tags=["Transacciones"])

