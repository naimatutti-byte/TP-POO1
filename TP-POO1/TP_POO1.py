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
def main():
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
            print(Especies)
if __name__ == "__main__" :
    main()