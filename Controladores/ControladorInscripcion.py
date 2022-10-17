from Modelos.Inscripcion import Inscripcion
class ControladorInscripcion():
    def __init__(self):
        print("Creando ControladorInscipcion")
    def index(self):
        print("Listar todas las inscripciones")
    def create(self,elInscripcion):
        print("Crear una inscripcion")
    def show(self,id):
        print("Mostrando una inscripcion con id ", id)

    def update(self, id, elInscripcion):
        print("Actualizando inscripcion con id ", id)

    def delete(self, id):
        print("Eliminando inscripcion con id ", id)
