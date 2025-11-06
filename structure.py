from arbol_user import user_arbol
from arbol_libro import libro_arbol

usuarios = []
libros = []

arb_user = user_arbol()
arb_user.insert_user({"nuip": 123, "name": "Juan Perez", "password": "1234", "editor": False})

arb_libro = libro_arbol()
arb_libro.insert_libro({
    "isbn": "978-0141439600",
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "state": "active"
})
arb_libro.insert_libro({
    "isbn": "978-0307476463",
    "title": "1984",
    "author": "George Orwell",
    "state": "active"
})
arb_libro.insert_libro({
    "isbn": "978-0061120084",
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "state": "active"
})
arb_libro.insert_libro({
    "isbn": "978-0743273565",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "state": "active"
})
arb_libro.insert_libro({
    "isbn": "978-1503280786",
    "title": "Moby Dick",
    "author": "Herman Melville",
    "state": "active"
})

def menu_user():
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Consultar Libros")
        print("2. Ver Perfil")
        print("3. Prestar Libro")
        print("4. Cerrar Sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ver_libros()
        elif opcion == "2":
            print("Mostrando perfil...")
        elif opcion == "3":
            print("Prestando libro...")
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def registar_usuario():
    while True:

        nuip = int(input("Ingresa tu numero de identificacion: "))
        name = input("Ingresa tu nombre completo: ")
        password = input("Ingresa tu contraseña: ")
    
        usuario ={
            "nuip":nuip,
            "name":name,
            "password": password,
            "editor": False
        }
        if arb_user.buscar(nuip):
            print("El nuip ya existe. Intenta con otro.")
        else:
            arb_user.insert_user(usuario)
            usuarios.append(usuario)
            print("Usuario registrado exitosamente.")
            
        op_exit = input("¿Desea registrar otro usuario? (yes/no): ").lower()
        if op_exit == "no":
            break
        
def buscar_usuario():
    nuip = int(input("Ingresa el numero de identificacion del usuario a buscar: "))
    usuario = arb_user.buscar(nuip)
    if usuario:
        return usuario
    else:
        return None
    
def inicio_sesion():
    nuip = int(input("Ingresa tu numero de identificacion: "))
    password = input("Ingresa tu contraseña: ")
    
    usuario = arb_user.buscar(nuip)
    if usuario and usuario["password"] == password:
        print("Inicio de sesión exitoso.")
        menu_user()
        return usuario
    else:
        print("Credenciales incorrectas.")
        return None
    
def consultar_libro():
    title = input("Ingresa el nombre del libro a buscar: ")
    libro = arb_libro.consultar_por_nombre(title)
    if libro:
        print(f"Libro encontrado: \n ISBN: {libro['isbn']}, Título: {libro['title']}, Autor: {libro['author']}, Estado: {libro['state']}")
    else:
        print("Libro no encontrado.")
        
def ver_libros():
    print("Listado de libros:")
    libros = arb_libro.listar()
    for libro in libros:
        print(f"ISBN: {libro['isbn']}, Título: {libro['title']}, Autor: {libro['author']}, Estado: {libro['state']}")
    print("Quieres consultar un libro en específico?")
    opcion = input("Ingresa 'yes' para consultar o 'no' para regresar al menú: ").lower()
    if opcion == "yes":
        consultar_libro()
    
while True:
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Buscar usuario")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        registar_usuario()
    elif opcion == "2":
        inicio_sesion()
    elif opcion == "3":
        usuario = buscar_usuario()
        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado.")
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
        
        

    

    
#print(arb_user.listar())
        

