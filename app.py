import csv

class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = float(puntuacion)

lista_libros=[]


with open("libros.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)
        nuevo_libro= Libro(
            fila["titulo"],
            fila["autor"],
            fila["genero"],
            fila["puntuacion"]
        )
        lista_libros.append(nuevo_libro)
    

#libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5)
#libro2 = Libro("1984", "George Orwell", "Ciencia Ficción", 4.3)
#libro3 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7)
#libro4 = Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2)
#libro5 = Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4)
#libro6 = Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1)
#libro7 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6)
#libro8 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8)
#libro9 = Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4)
#libro10 = Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)

#lista_libros.append(libro1)
#lista_libros.append(libro2)
#lista_libros.append(libro3) 
#lista_libros.append(libro4)
#lista_libros.append(libro5)
#lista_libros.append(libro6)
#lista_libros.append(libro7)
#lista_libros.append(libro8)
#lista_libros.append(libro9)
#lista_libros.append(libro10)

salir= False

while salir==False:
    print("====================================")
    print("Bienvenido a la biblioteca virtual")
    print("1. Agregar libros")
    print("2. Buscar libros por genero")
    print("3. Recomendar libros")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        puntuacion = input("Ingrese la puntuación del libro (0-5): ")
        nuevo_libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado exitosamente.")
    elif opcion == "2":
        generos_disponibles = sorted(set(libro.genero.lower() for libro in lista_libros))
        for numero, genero in enumerate(generos_disponibles, start=1):
            print(f"{numero}. {genero.capitalize()}")
        genero_seleccionado = input("Seleccione un género por número: ")
        if not genero_seleccionado.isdigit():
            print("Opción no válida. Por favor, seleccione un número válido.")
            continue
        genero_seleccionado = int(genero_seleccionado)
        if genero_seleccionado < 1 or genero_seleccionado > len(generos_disponibles):
            print("Opción no válida. Por favor, seleccione un número válido.")
            continue
        genero_buscar = list(generos_disponibles)[genero_seleccionado - 1]
        libros_encontrados = [libro for libro in lista_libros if libro.genero.lower() == genero_buscar]
        if libros_encontrados: 
            print(f"Libros encontrados en el género '{genero_buscar.capitalize()}':")
            for libro in libros_encontrados:
                print(f"- {libro.titulo} por {libro.autor} (Puntuación: {libro.puntuacion})")
        else:
            print(f"No se encontraron libros en el género '{genero_buscar.capitalize()}'.")
    elif opcion == "3":
        generos_disponibles = sorted(set(libro.genero.lower() for libro in lista_libros))
        for numero, genero in enumerate(generos_disponibles, start=1):
            print(f"{numero}. {genero.capitalize()}")
        genero_seleccionado = input("Seleccione un género por número: ")
        if not genero_seleccionado.isdigit():
            print("Opción no válida. Por favor, seleccione un número válido.")
            continue
        genero_seleccionado = int(genero_seleccionado)
        if genero_seleccionado < 1 or genero_seleccionado > len(generos_disponibles):
            print("Opción no válida. Por favor, seleccione un número válido.")
            continue
        genero_buscar = list(generos_disponibles)[genero_seleccionado - 1]
        libros_encontrados = [libro for libro in lista_libros if libro.genero.lower() == genero_buscar]
        if libros_encontrados:
            libro_mayor = max(libros_encontrados, key=lambda libro: libro.puntuacion)
            print(f"- {libro_mayor.titulo} por {libro_mayor.autor} (Puntuación: {libro_mayor.puntuacion})")
        else:
            print(f"No se encontraron libros en el género '{genero_buscar.capitalize()}'.")
    elif opcion == "4":
        print("Saliendo de la biblioteca virtual...")
        salir = True
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")