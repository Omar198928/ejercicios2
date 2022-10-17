from Modelos.Departamento import Departamento

class ControladorDepartamento():
    def __init__(self):
        print("Creando ControladorDepartamento")
    def index(self):
        print("Listar todos los Departamentos")
    def create(self,elDepartamento):
        print("Crear un Departamento")
    def show(self,id):
        print("Mostrando un Departamento con id ", id)

    def update(self, id, elDepartamento):
        print("Actualizando Departamento con id ", id)

    def delete(self, id):
        print("Elimiando Departamento con id ", id)
