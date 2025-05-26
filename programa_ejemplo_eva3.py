usuarios= {}
op = 1
while op < 3:
    usuario_ok=False
    print("1._iniciar sesion:")
    print("2._Registrarse:")
    print("3._salir:")
    op=int(input("Ingrese opcion seleccionada"))
    match op:
        case 1:
            id_usuario=input("Ingrese el nombre del usuario")
            if id_usuario in usuarios:
                clave=input("ingrese su contraseña")
                if clave== usuarios[id_usuario]:
                   usuario_ok=True
                else:
                   print("Contraseña del usuario invalida")
            else:
                print("el usuario no existe. Debe registrarse")
        case 2:
             id_usuario=input("ingrese el nombre del usuario")
             if id_usuario in usuarios:
                print("el usuario ya existe")
             else:
                clave= input("Ingrese su clave")
                usuarios[id_usuario] = clave
                
        case 3:
                print("Cierre de sesion")              
    if  usuario_ok == True:
        

print(usuarios)