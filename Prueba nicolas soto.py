from itertools import cycle

lista_datos=[]
nomlis=["DNI","nombre"]
cerlis=["nacimiento","estado conyugal","nacionalidad"]
n=-1

def dnisim(dni):
  dni1=dni.replace(".","").replace("-","")
  dni1=dni1[:-1]
  return dni1

def digito_verificador(dni1):

  reversed_digits = map(int, reversed(str(dni1)))

  factors = cycle(range(2, 8))

  s = sum(d * f for d, f in zip(reversed_digits, factors))

  return (-s) % 11

def grabar():

  while True:#DNI
    print("\033[0mIngrese su DNI:")
    dni=str(input())
    dni1=dnisim(dni)

    n_ver=int(dni[-1])
    n_ver1=digito_verificador(dni1)

    if n_ver == n_ver1:
      break
    else:
      print("\033[1;31mEl DNI ingresado no existe")

  while True:#Nombre
    print("\033[0mIngrese su nombre:")
    nombre=str(input()).lower()
    if len(nombre)>7:
      break
    else:
      print("\033[1;31mEl nombre ingresado debe tener al menos 8 caracteres")

  while True:#Edad
    print("\033[0mIngrese su edad:")
    edad=int(input())
    if edad<1:
      print("\033[1;31mPorfavor ingrese una edad valida:")
    else:
      edad=str(edad)
      break

  pais=str(input("Ingrese su país de nacimiento:\n")).lower()

  ciudad=str(input("Ingrese su ciudad de nacimiento:\n")).lower()

  datos=[dni1,nombre,edad,pais,ciudad]
  lista_datos.append(datos)
  print(f"\nLos datos de {nombre.capitalize()} se han guardado correctamente\n----------------------------------\nDNI:{dni1}\nNombre:{nombre.capitalize()}\nEdad:{edad}\nPais:{pais.capitalize()}\nCiudad:{ciudad.capitalize()}\n----------------------------------")

def search():
    bus=int(input("¿Que desea buscar?\n(1)DNI\n(2)Nombre\n"))-1
    global n
    if bus==0:
      dni=str(input("ingrese el DNI a buscar:\n"))
      buscar=dnisim(dni)
    if bus==1:
      buscar=str(input("ingrese el nombre a buscar:\n")).lower()

    for n in range(len(lista_datos)):
        if lista_datos[n][bus]==buscar:
            break
    else:
      print(f"No se ha encontrado un archivo con el {nomlis[bus]} dado")
      n=-1

def buscar():
    search()
    if n>-1:
      print(f"----------------------------------\nDNI:{lista_datos[n][0]}\nNombre:{lista_datos[n][1].capitalize()}\nEdad:{lista_datos[n][2]}\nPais:{lista_datos[n][3].capitalize()}\nCiudad:{lista_datos[n][4].capitalize()}\n----------------------------------")

def certificado():
  cer=int(input("Seleccione el tipo de certificado que desee imprimir\n(1) Certificado de nacimiento\n(2) Certificado de estado conyugal\n(3) Certificado de nacionalidad\n"))-1
  if cer<3 and cer>-1:
    search()
    if n>-1:
      print(f"----------------------------------\nCertificado de {cerlis[cer]}\nDNI:{lista_datos[n][0]}\nNombre:{lista_datos[n][1].capitalize()}\nEdad:{lista_datos[n][2]}\nPais:{lista_datos[n][3].capitalize()}\nCiudad:{lista_datos[n][4].capitalize()}\n----------------------------------")
    else:
      print("Opcion no valida")

def borrar():
  search()
  if n>-1:
    print(f"\n{lista_datos[n][1]} ha sido borrado\n")
    del lista_datos[n]
def salir():
    print("Hasta pronto!\nNicolás Soto\nV1.0")
    
print("Bienvenido")
while True:
    menu=int(input("Seleccione una opcion\n(1) Grabar\n(2) Buscar\n(3) Imprimir Certificado\n(4) Borrar\n(5) Salir\n"))
    if menu==1:
     grabar()
    if menu==2:
      buscar()
    if menu==3:
      certificado()
    if menu==4:
      borrar()
    if menu==5:
      salir()
      break
    if menu==9:#imprimir lista
       print(lista_datos)
    if menu==0:#cargar datos para probar funcionalidades
        lista_datos = [
            ["12345678", "juan perez", "35", "estados unidos", "nueva york"],
            ["10987654", "maria garcia", "27", "espana", "madrid"],
            ["18901234", "roberto silva", "42", "brasil", "rio de janeiro"],
            ["20123456", "ana lopez", "31", "mexico", "ciudad de mexico"],
            ["21987654", "david smith", "29", "reino unido", "londres"],
            ["11234567", "laura muller", "36", "alemania", "berlin"],
            ["19876543", "carlos torres", "24", "colombia", "bogota"],
            ["21012559", "nicolas soto", "21", "chile", "santiago"],
            ["20192837", "diego fernandez", "33", "argentina", "buenos aires"],
            ["17364829", "alessandra rossi", "28", "italia", "roma"]
        ]