usuario1 = {
    "nombre": "Julio",
    "apellido": "Teran",
    "telefono": 287
}

usuario2 = {
    "nombre" : "Maria",
    "apellido": "Orellana",
    "telefono": 511594
}

usuario3 = {
    "nombre" : "Hugo",
    "apellido" : "Muñoz",
    "telefono" : 352
}

listaUsuarios = [usuario1,usuario2,usuario3]
# print(usuario1)
# print(usuario1["nombre"])
# print(listaUsuarios[1])



for indice in listaUsuarios:
    for clave, valor in indice.items():
        print(f'{clave} : {valor}')

