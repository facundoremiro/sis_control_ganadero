from models.reg_pesadas import Regpesadas
from models.animals import Animal
def cargar_animal_nuevo():
    print("Ingrese los datos del nuevo animal:")
    fecha_input = input("año-mes-dia (Enter para hoy): ")
    fecha_session = fecha_input if fecha_input else None
    while True:
        caravana = input("Caravana o enter para terminar:")
        if not caravana: break

        sexo = input("Sexo (M/H): ")
        lote = input("Lote: ")
        peso = float(input("Peso: "))
        estado_corporal = int(input("Estado corporal del animal (1-5): "))
        animal_nuevo = Animal(caravana, sexo, lote)
        pesaje_inicial = Regpesadas(caravana, peso, estado_corporal, fecha_session)
        animal_nuevo.save()
        pesaje_inicial.save()
        
        print(f"Animal agregado: {caravana}, {peso}")
#if __name__ == "__main__": cargar_animal_nuevo()

def cargar_pesadas():
    if not Animal.hay_animales():
        print("No hay animales registrados. Por favor, agregue un animal primero.")
        return cargar_animal_nuevo()
    print("Ingrese los datos de los pesajes de los animales existentes:")

    fecha_input = input("año-mes-dia (Enter para hoy): ")
    fecha_session = fecha_input if fecha_input else None
    while True:
        caravana = input("Caravana o enter para terminar:")
        if not caravana: break

        if not Animal.find_by_caravana(caravana):
            print(f"Animal con caravana {caravana} no encontrado. Por favor, agregue el animal primero.")
            continue

        peso = float(input("Peso: "))
        estado_corporal = int(input("Estado corporal del animal (1-5): "))
        p = Regpesadas(caravana, peso, estado_corporal, fecha_session)
        p.save()

#if __name__ == "__main__": cargar_pesadas()
print("Bienvenidos al sistema de control ganadero")

while True:
    print("\nPresione 1 para mostrar menu de animales, 2 para registrar pesadas, 3 para agregar un animal nuevo, o 4 para salir.")
    input_opcion = input("Ingrese su opción: ")

    if input_opcion == "1":
        while True:
            print("Menu de animales:")
            print("1. Mostrar animales")
            print("2. Mostrar pesajes")
            print("3. Volver al menu principal")
            opcion_animal = input("Ingrese su opción: ")
            if opcion_animal == "1":
                while True:
                    print("Opciones para mostrar animales:")
                    print("1. Todos, 2, por caravana, 3. por lote, 4. por sexo, 5. volver al menu principal")
                    tipo = input("Ingrese su opción: ")
                    if tipo == "1":
                        Animal.mostrar_animales()
                    elif tipo == "2":
                        caravana = input("Ingrese la caravana del animal: ")
                        Animal.mostrar_animales(caravana=caravana)
                    elif tipo == "3":
                        lote = input("Ingrese el lote del animal: ")
                        Animal.mostrar_animales(lote=lote)
                    elif tipo == "4":
                        sexo = input("Ingrese el sexo del animal (M/H): ")
                        Animal.mostrar_animales(sexo=sexo)
                    elif tipo == "5":
                        print("Volviendo al menu de animales...")
                        break
                    else:
                        print("Opción inválida. Por favor, intente nuevamente.")
            elif opcion_animal == "2":
                Regpesadas.mostrar_pesajes()
            elif opcion_animal == "3":
                print("Volviendo al menu principal...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
    elif input_opcion == "2":
        cargar_pesadas()
    elif input_opcion == "3":
        cargar_animal_nuevo()
    elif input_opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
    


