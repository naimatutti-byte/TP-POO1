
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

def VerRegistros(Especies, Propietarios):
    print("\n--- REGISTROS DE PROPIETARIOS ---")
    if not Propietarios:
        print("No hay propietarios registrados.")
    else:
        for DNI, Datos in Propietarios.items():
            print(f"DNI: {DNI}, Nombre: {Datos[0]}, Telefono: {Datos[1]}, Correo: {Datos[2]}")

    print("\n--- REGISTROS DE MASCOTAS ---")
    if not Especies:
        print("No hay mascotas registradas.")
    else:
        for ID, Datos in Especies.items():
            print(f"ID: {ID}, Especie: {Datos[0]}, Nombre: {Datos[1]}, Edad: {Datos[2]}, Propietario: {Datos[3]}")

def AgendarCita(ReservaCita, RegistroMascota):
    DatosCita = []
    Cita = str(input("Desea reservar una cita? (s/n): "))
    if Cita.lower() == "s":
        if not RegistroMascota:
            print("Debe registrar primero una mascota.")
            return
        else:
            while True:
                ID = int(input("Ingrese el ID de la mascota para agendar cita: "))
                if ID in RegistroMascota:
                    Fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
                    Motivo = input("Ingrese el motivo de la cita: ")
                    if ID in ReservaCita:
                        ReservaCita[ID].append([Fecha, Motivo])
                    else:
                        ReservaCita[ID] = [[Fecha, Motivo]]
                    print("Cita agendada correctamente.")
                    break
                    break
                else:
                    print("Mascota no encontrada. Intente de nuevo.")
    else:
        return

def CancelarCita(ReservaCita):
    if not ReservaCita:
        print(" No hay citas agendadas.")
        return
    else:
        ID = int(input("Ingrese el ID de la mascota para cancelar la cita: "))
        if ID in ReservaCita:
            del ReservaCita[ID]
            print("Cita cancelada con exito.")
        else:
            print("No existe cita para esa mascota.")

def VerHistorial(Especies):
    if not Especies:
        print("No hay mascotas registradas.")
        return
    
    ID = int(input("Ingrese el ID de la mascota para ver su historial: "))
    if ID in Especies:
        Datos = Especies[ID]
        print(f"\nHistorial de la Mascota ID {ID}:")
        print(f"Especie: {Datos[0]}")
        print(f"Nombre: {Datos[1]}")
        print(f"Edad: {Datos[2]}")
        print(f"Propietario: {Datos[3]}")
    else:
        print("Mascota no encontrada.")

def VerReportes(ReservaCitas, RegistroMascota):
    print("\n\tReportes de veterinaria")
    print("\t--------------------------------")

    if not ReservaCitas:
        print("\tNo hay citas registradas.")
        return

    print("\tListado de Citas:")
    for ID, ListaCitas in ReservaCitas.items():
        if ID in RegistroMascota:
            NombreMascota = RegistroMascota[ID][1]
        else:
            NombreMascota = "Desconocido"
        print(f"\n\tMascota: {NombreMascota} (ID: {ID})")
        print(f"\tTotal de citas: {len(ListaCitas)}")

        for Fecha, Motivo in ListaCitas:
            print(f"\t  - Fecha: {Fecha} | Motivo: {Motivo}")


def main():
    Propietarios = {}
    ReservarCita = {}
    RegistroMascota = {}
    while True:
        print("""\n\tMENU VETERINARIA
        -------------------------------------
        1. Registrar Mascota
        2. Registrar Propietario
        3. Agendar Cita
        4. Cancelar Cita
        5. Ver Historial
        6. Ver Registros
        7. Ver Reportes
        8. Salir
        -------------------------------------
        """)
        Opcion = int(input("Elija opcion : "))
        if Opcion == 1:
            RegistrarMascota(RegistroMascota,Propietarios)
        elif Opcion == 2:
            RegistrarPropietario(Propietarios)
        elif Opcion == 3:
            AgendarCita(ReservarCita,RegistroMascota)
        elif Opcion == 4:
            CancelarCita(ReservarCita)
        elif Opcion == 5:
            VerHistorial(RegistroMascota)
        elif Opcion == 6:
            VerRegistros(RegistroMascota,Propietarios)
        elif Opcion == 7:
            VerReportes(ReservarCita,RegistroMascota)
        elif Opcion == 8:
            return
        else:
            print("Opcion no existe")

if __name__ == "__main__" :
    main()