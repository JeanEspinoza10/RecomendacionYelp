from app import api
from flask_restx import Resource
from flask import request
from app.controllers.machine_controller import MachineL


# Documentacion para el endpoint
machine_ns = api.namespace(
    name="Machine",
    description="",
    path="/ml"

)

# Creando el endpoint

'''

def Get(categoria: str) : Debe devolver el estado de acuerdo a la valoración

'''

@machine_ns.route("/<string:categoria>")
class Machine(Resource):
    def get(self,categoria):
        controller = MachineL()

        return controller.Recomendacion(categoria)

@machine_ns.route("/actualizar")
class MachineDatabase(Resource):
    def put(self):
        controller = MachineL()
        return controller.actualizarDatabase()