# from data import DataBase

# database = DataBase()
# usuarios = database.comando('SELECT username, contrasenia FROM usuario')

# for usuario in usuarios:
#     print(usuario)


from usuario import Colaborador, Usuario

# colaborador = Colaborador()
# colaborador.registrar('Juan', 'Perez')

usuario = 'juangauto'
contrasena = 'Juan12Gau34'

usuario1 = Usuario()
usuario = usuario1.login(usuario, contrasena)

if usuario1.online:
    id_usuario = usuario[0][0]
    nombre_usuario = usuario[0][1]
    print(f'Bienvenido {nombre_usuario}')
else:
    print('Usuario o contraseña incorrecto')
