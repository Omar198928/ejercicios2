from Modelos.Materia import Materia
class ControladorMateria():
    def __init__(self):
        print("Creando ControladorMateria")
    def index(self):
        print("Listar todas las Materias")
    def create(self,elMateria):
        print("Crear una Materia")
    def show(self,id):
        print("Mostrando una Materia con id ", id)

    def update(self, id, elMateria):
        print("Actualizando Materia con id ", id)

    def delete(self, id):
        print("Eliminando Materia con id ", id)