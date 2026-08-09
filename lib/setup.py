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

print("Bienvenido al sistema de registro de pesadas, presiona + para agregar un animal nuevo, o = para registrar pesadas de animales existentes.")
input_opcion = input("Ingrese su opción: ")
if input_opcion == "+":
    cargar_animal_nuevo()
elif input_opcion == "=":
    cargar_pesadas()

