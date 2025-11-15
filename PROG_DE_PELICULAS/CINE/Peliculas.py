import csv
import os

# Archivos que nos sugerio
FUNCIONES = "Funciones.csv"
VENTAS_FILE = "Ventas.csv"

# Función para registrar una nueva función
def registrar_funcion():
    codigo = input("Código de la función: ")
    pelicula = input("Nombre de la película: ")
    hora = input("Hora: ")
    precio = float(input("Precio del boleto: "))
    boletos = int(input("Cantidad de boletos disponibles: "))
    
    with open(FUNCIONES, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([codigo, pelicula, hora, precio, boletos])
    print("✅ Función registrada correctamente.\n")

# Función para listar todas las funciones
def listar_funciones():
    print("\n--- FUNCIONES DISPONIBLES ---")
    with open(FUNCIONES, newline="") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            print(f"Código: {fila['codigo']} | Película: {fila['pelicula']} | Hora: {fila['hora']} | Precio: ${fila['precio']} | Boletos: {fila['boletos_disponibles']}")
    print()

# Función para vender boletos
def vender_boletos():
    codigo = input("Ingrese el código de la función: ")
    cantidad = int(input("Cantidad de boletos: "))
    
    funciones = []
    encontrado = False
    total = 0
    
    with open(FUNCIONES, newline="") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["codigo"] == codigo:
                encontrado = True
                boletos_disponibles = int(fila["boletos_disponibles"])
                if cantidad > boletos_disponibles:
                    print("❌ Error: No hay suficientes boletos disponibles.\n")
                    return
                total = cantidad * float(fila["precio"])
                fila["boletos_disponibles"] = str(boletos_disponibles - cantidad)
            funciones.append(fila)
    
    if not encontrado:
        print("❌ Error: La función no existe.\n")
        return

    # Actualizar archivo de funciones
    with open(FUNCIONES, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["codigo", "pelicula", "hora", "precio", "boletos_disponibles"])
        writer.writeheader()
        writer.writerows(funciones)
    
    # Registrar venta
    with open(VENTAS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([codigo, cantidad, total])
    
    print(f"✅ Venta registrada. Total a pagar: ${total:.2f}\n")

# Función para mostrar resumen de ventas
def resumen_ventas():
    total_boletos = 0
    total_dinero = 0
    with open(VENTAS_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            total_boletos += int(fila["cantidad"])
            total_dinero += float(fila["total"])
    print(f"\n--- RESUMEN DE VENTAS ---\nTotal boletos vendidos: {total_boletos}\nTotal dinero recaudado: ${total_dinero:.2f}\n")

# Menú principal
def menu():
    while True:
        print("=== SISTEMA DE CINE ===")
        print("1. Registrar función nueva")
        print("2. Listar funciones disponibles")
        print("3. Vender boletos")
        print("4. Ver resumen de ventas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_funcion()
        elif opcion == "2":
            listar_funciones()
        elif opcion == "3":
            vender_boletos()
        elif opcion == "4":
            resumen_ventas()
        elif opcion == "5":
            print("👋 Gracias por usar el sistema.")
            break
        else:
            print("❌ ERROR\n")
menu()
