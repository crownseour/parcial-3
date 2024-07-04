import random 
contador_10lts = 0
contador_20lts = 0
contador_6lts = 0

def registro(registro):
    while True:    
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        direccion = input("Ingrese su direccion: ")
        sector = input("Ingrese su sector: ")
        datos = {
            "Nombre": nombre,
            "Apellido": apellido,
            "Direccion": direccion,
            "Sector": sector
        }
        registro.append(registro)
        if datos == "":
            return False
        else:
            return True
        

def id(codigo):
    return codigo.radiant(10000, 99999)
    


def cantidad_cilindros(registro):
    while True:   
          print("1. Cilindros de 6lts")
          print("2. Cilindros de 10lts")
          print("3. Cilindros de 20lts")
          print("4. volver")
          secundaria = input("Elige una opcion de cilindro: ")
          if secundaria == "1":
              print("Has escogido cilindro de 6lts")
              cantidad = int(input("Ingresa una cantidad"))
              contador_6lts = contador_6lts + cantidad
              print(f"Has ingresado {contador_6lts} Cilindros de 6lts")
          elif secundaria == "2":
                print("Has escogido cilindro de 6lts")
                cantidad = int(input("Ingresa una cantidad"))
                contador_10lts = contador_10lts + cantidad
                print(f"Has ingresado {contador_10lts} Cilindros de 10lts")
          elif secundaria == "3":
               print("Has escogido cilindro de 6lts")
               cantidad = int(input("Ingresa una cantidad"))
               contador_20lts = contador_20lts + cantidad
               print(f"Has ingresado {contador_20lts} Cilindros de 20lts")
          elif secundaria == "4":
              print("Saliendo...")
              
          else: 
               print("la opcion ingresada es inválida")
    
          if cantidad == 0 and cantidad == "":
           print("La cantidad no debe quedar vacía")


def listar(registro):
    for cliente in registro:
        print(f"Nombre: {cliente["Nombre"]} {cliente["Apellido"]}")
        print(f"Dirección: {cliente["Direccion"]}")
        print(f"Sector: {cliente["Sector"]}")

print("No pude seguir el codigo")

    

        


