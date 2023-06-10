from data import DataBase


class Usuario:

    def __init__(self):
        self.online = False
        self.usuario = None
        self.id = None
        self.nombre = None
        self.apellido = None
        self.db = DataBase()

    def registrar(self, nombre, apellido, ):
        self.nombre = nombre
        self.apellido = apellido
        print(
            f'Registrado: \nnombre: {self.nombre}\napellido: {self.apellido}')

    def login(self, username, contrasenia):
        self.usuario = self.db.comando(
            "SELECT id_usuario, nombre FROM usuario WHERE username = '%s' AND contrasenia = '%s'" % (username, contrasenia))

        if self.usuario:
            self.id = self.usuario[0][0]
            self.online = True

        return self.usuario

    def __str__(self):
        print(f'Usuario online: {self.online}')


class Colaborador(Usuario):

    def __init__(self):
        es_colaborador = False

    def comentar(self, id_articulo, id_usuario, comentario):
        pass

    def registrar(self, nombre2, apellido2):
        super().registrar(nombre2, apellido2)
        self.es_colaborador = True

        print(f'Es colaborador: {self.es_colaborador}')
