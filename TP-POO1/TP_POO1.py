def RegistrarMascota(Especies):
    NombresMascotas = []
    Especie = str(input("Ingrese la especie de la mascota : "))
    while True:
        Mascota = str(input("Ingrese el nombre de la mascota : "))
        NombresMascotas.append(Mascota)
        Continuar = str(input("Desea agregar otra mascota de la misma especie (s/n) : "))
        if Continuar != "s":
            break
    Especies[Especie] = NombresMascotas
def RegistrarMascota(Especies,Propietarios):
    if not Propietarios:
        print("No hay propietarios registrados")
    else:
        while True:
            DatosMascota = []
            ID = int(input("Ingrese el ID de la mascota : "))
            Especie = str(input("Ingrese la especie de la mascota : "))
            Mascota = str(input("Ingrese el nombre de la mascota : "))
            Edad = int(input("Ingrese la edad de la mascota : "))
            DatosMascota.append(Especie)
            DatosMascota.append(Mascota)
            DatosMascota.append(Edad)

            while True:
                NombrePropietario = str(input("Ingrese nombre del propietario : "))
                PropietarioEncontrado = False
                for DNI, Datos in Propietarios.items():
                    if NombrePropietario == Datos[0]:
                        PropietarioEncontrado = True
                        break
                if PropietarioEncontrado == True:
                    DatosMascota.append(NombrePropietario)
                    print("Propietario encontrado.")
                    break
                else:
                    print("Propietario no encontrado.")
            Especies[ID] = DatosMascota
            Continuar = str(input("Desea agregar otra mascota de la misma especie (s/n) : "))
            if Continuar != "s":
                break
        

def RegistrarPropietario(Propietarios):
    DatosPropietario = []
    Propietario = str(input("Ingrese su nombre : "))
    DatosPropietario.append(Propietario)
    
    while True:
        DNI = int(input("Ingrese su DNI : "))
        if DNI < 10000000 or DNI >99999999:
            print("DNI invalido.\n")
        else:
            break
    Propietarios[DNI] = Propietario
    while True:
        NumeroTelefono = int(input("Ingrese el numero de telefono : "))
        if NumeroTelefono < 100000000 or NumeroTelefono > 999999999:
            print("El numero de telefono es invalido, vuelva a ingresar.")
        else:
            DatosPropietario.append(NumeroTelefono)
            break
    while True:
        CorreoElectronico = str(input("Ingrese el correo electronico : "))
        if "@gmail.com" not in CorreoElectronico:
            print("El correo electronico no es valido")
        else:
            DatosPropietario.append(CorreoElectronico)
            break
    Propietarios[DNI] = DatosPropietario

def main():
    Propietarios = {}
    Especies = {}
    while True:
        print("""\n\tMENU VETERINARIA
        -------------------------------------
        1. Registrar Mascota
        2. Registrar Propietario
        3. Agendar Cita
        4. Cancelar Cita
        5. Ver Historial
        6. Ver Registros
        7. Salir
        -------------------------------------
        """)
        Opcion = int(input("Elija opcion : "))
        if Opcion == 1:
            RegistrarMascota(Especies)
            RegistrarMascota(Especies,Propietarios)
            print(Especies)
        elif Opcion == 2:
            RegistrarPropietario(Propietarios)
            print(Propietarios)

if __name__ == "__main__" :
    main()