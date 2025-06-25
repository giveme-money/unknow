maestros = {
    "pacientes": {},
    "farmacos": {},
    "insumos": {},
    "productos": {},
    "prestaciones": {},
    "proveedores": {}
}

def menu_maestros():
    while True:
        print("\n--- menu maestros ---")
        print("1. crear")
        print("2. modificar")
        print("3. bloquear")
        print("4. volver")
        opcion = input("elige una opcion: ")

        if opcion == "1":
            tipo = input("tipo (pacientes, farmacos, insumos, productos, prestaciones, proveedores): ")
            if tipo not in maestros:
                print("tipo no valido")
                continue
            codigo = input("codigo: ")
            descripcion = input("descripcion: ")
            maestros[tipo][codigo] = {"descripcion": descripcion, "estado": "activo"}
            print("registro creado")

        elif opcion == "2":
            tipo = input("tipo: ")
            codigo = input("codigo: ")
            if tipo in maestros and codigo in maestros[tipo]:
                nueva_desc = input("nueva descripcion: ")
                maestros[tipo][codigo]["descripcion"] = nueva_desc
                print("registro modificado")
            else:
                print("registro no encontrado")

        elif opcion == "3":
            tipo = input("tipo: ")
            codigo = input("codigo: ")
            if tipo in maestros and codigo in maestros[tipo]:
                maestros[tipo][codigo]["estado"] = "bloqueado"
                print("registro bloqueado")
            else:
                print("registro no encontrado")

        elif opcion == "4":
            break

        else:
            print("opcion no valida")