from gestor import cargar_datos,configurar_master,verificar_master, guardar_datos, hashear

datos = cargar_datos()

if not datos:
    print("====={ Registro de Contraseña }=====")
    key_0 = input("Ingrese la contraseña\n> ")
    configurar_master(key_0)
    print("contraseña creada con exito!")
else:
    print("====={ Login de Administracion }=====")
    key_1 = input("Ingrese la contraseña\n> ")
    resultado=verificar_master(key_1,datos["master"])
    if resultado:
        while True:
            print("\n1.Ver bóvedas\n2.Agregar credencial\n3.Buscar credencial\n4.Salir\n")
            opcion = input("opcion:\n> ")
            if opcion == "1":
                print("1.Redes Sociales\n2.Trabajo\n3.Bancos")
                opcion_1 = input("opcion:\n> ")
                if opcion_1 == "1":
                    resultado = datos["bovedas"]["Redes Sociales"]
                    print(resultado)
                elif opcion_1 == "2":
                    resultado = datos["bovedas"]["Trabajo"]
                    print(resultado)
                elif opcion_1 == "3":
                    resultado = datos["bovedas"]["Bancos"]
                    print(resultado)
                else:
                    print("Opcion Erronea")
                    continue
            elif opcion == "2":
                print("1.Redes Sociales\n2.Trabajo\n3.Bancos")
                opcion_2_1=input("opcion:\n> ")
                r_servicio = input("ingresar su servicio:\n> ").lower()
                r_username = input("ingresar su username:\n> ").lower()
                r_password = input("ingresar su password:\n> ").lower()
                nueva_credecial={
                    "servicio" : r_servicio,
                    "username" : r_username,
                    "password" : hashear(r_password)
                    }
                boveda={"1": "Redes Sociales", "2": "Trabajo", "3": "Bancos"}
                boveda_elegida=boveda[opcion_2_1]
                datos["bovedas"][boveda_elegida].append(nueva_credecial)
                guardar_datos(datos)
                print("credenciales agregadas con exito!")

            elif opcion == "3":
                buscar = input("Ingrese la credencial que desee buscar\n> ").lower()
                encontrado = False
                for boveda, credenciales in datos["bovedas"].items():
                    for c in credenciales:
                        if c["servicio"].lower() == buscar:
                            print(f"\nboveda : {boveda}")
                            print(f"servicios : {c['servicio']}")
                            print(f"username : {c['username']}")
                            encontrado = True
                if not encontrado:
                    print("servicio no encontrado")

            elif opcion == "4":
                print("saliendo...")
                break

            else:
                print("Opcion Invalida")
                continue
