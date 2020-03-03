print("ejercicio 5:")
print("introduce 2 números enteros para calcular su resta y cociente.")
x = int(input("introduce el primer número entero: "))
y = int(input("introduce el segundo número entero: "))
z = x // y
print("El cociente de la división es: " + str(z))
z = x - y
print("La resta es: " + str(z))

........................................................................................................................................
print("ejercicio 6:")
print("Calculador de la ecuación ax+b=0 ")
a = float(input("introduce a :"))
b = float(input("introduce b :"))
z = (-b / a)
print("La solución es: " + str(z))

........................................................................................................................................

print("ejercicio 7: ")
x = float(input("inserte un número para saber si es positivo: "))

if x > 0:
    print ("El número " + str(x) + " es positivo")
elif x == 0:
    print(" El número es 0")
else:
    print("El número no es positivo")

........................................................................................................................................

print("ejercicio 8:")
x = float(input("Inserte un número: "))
if -1.0 < x < 1.0 :
    print("El número " + str(x) + " se encuentra en el intervalo (-1.0,1.0).")
else:
    print("El número " + str(x) + " no se encuentra en el intervalo (-1.0,1.0)")

........................................................................................................................................

print("ejercicio 9")
print("Introduzca un punto de la forma (x,y): ")
x = float(input("introduzca x: "))
y = float(input("introduzca y: "))
if x > 0 and y > 0:
    print("El punto (" + str(x)+","+ str(y) + ") se encuentra en el primer cuadrante.")
if x > 0 and y < 0:
    print("El punto (" + str(x)+","+ str(y) + ") se encuentra en el cuarto cuadrante.")
if x < 0 and y > 0:
    print("El punto (" + str(x)+","+ str(y) + ") se encuentra en el segundo cuadrante.")
if x < 0 and y < 0:
    print("El punto (" + str(x)+","+ str(y) + ") se encuentra en el tercer cuadrante")

    
........................................................................................................................................

print("ejercicio 10")
x = float(input("introduzca las horas: "))
y = float(input("introduzca los minutos: "))
z = float(input("introduzca las segundos: "))
if x >= 24:
    print("formato de horas introducido erroneamente.")
if y >= 60:
    print("formato de minutos introducido erroneamente.")
if z >= 60:
    print("formato de segundos introducido erroneamente.")
if x < 24 and y < 60 and z < 60:
    print("Ha introducido una hora valida: " + str(x) + " horas, " + str(y) + " minutos y " + str(z) + " segundos.")

........................................................................................................................................

print("ejercicio 11:")
x = int(input("introduce un año para saber si es bisiesto: "))
y = x % 4
z = x % 400
s = x % 100
if y == 0:
    if s == 0 :
        if z == 0:
            print("El año es bisiesto.")
        else:
            print("El año no es bisiesto.")
    else: print("El año es bisiesto.")
else: print("El año " + str(x) + " no es bisiesto.")

........................................................................................................................................

print("Ejercicio 13")
x = int(float(input("Introduzca la nota: ")))
if x == 0 or x < 5.0:
    print("Suspenso.")
if 5.0 <= x < 7.0:
    print("Aprobado.")
if 7.0 <= x < 8.5:
    print("Notable.")
if 8.5 <= x < 9.5:
    print("Excelente")
if 9.5 <= x <= 10.0:
    print("matricula de honor.")
if x < 0.0 or x >10.0:
    print("Introduzca un número correcto (entre 0 y 10).")

........................................................................................................................................

print("ejercicio 14:")
print("Convertidor de años a años caninos")
x = (float(input("Introduzca los años: ")))
print(x)
if x <= 2:
    z = x * 10.5
    print("La edad de su perro es: " + str(z))
if x > 2:
    y = 4 * x + 13
    print("La edad de su perro es: " + str(y))

........................................................................................................................................
print("Ejercicio 15")
x = float(input("Introduce un número entero para saber si es multiplo de 2: "))
if x % 2 == 0:
    print("El número es múltiplo de 2.")
if x % 2 != 0:
    print("El número no es múltiplo de 2."
........................................................................................................................................

........................................................................................................................................
print("Ejercicio 16")
print("Introduce 2 números enteros para determinar si uno es múltiplo del otro.")
x = int(input("Primer número: "))
y = int(input("Segundo número: "))
if x % y == 0:
    print("El número " + str(x) + " es múltiplo de " + str(y) + ".")
if y % x == 0:
    print("El número " + str(y) + " es múltiplo de " + str(x) + ".")
if x % y != 0 and y % x != 0:
    print("No son múltiplos.")

........................................................................................................................................


print("ejercicio 17")
x = int(input("introduzca su año de nacimiento para saber su horóscopo chino: "))
y = x % 12
if y == 0:
    print("su horóscopo chino es Mono")
if y == 1:
    print("su horóscopo chino es Gallo.")
if y == 2:
    print("su horóscopo chino es Perro.")
if y == 3:
    print("su horóscopo chino es Cerdo.")
if y == 4:
    print("su horóscopo chino es Rata.")
if y == 5:
    print("su horóscopo chino es Buey.")
if y == 6:
    print("su horóscopo chino es Tigre.")
if y == 7:
    print("su horóscopo chino es Conejo.")
if y == 8:
    print("su horóscopo chino es Dragón.")
if y == 9:
    print("su horóscopo chino es Serpiente.")
if y == 10:
    print("su horóscopo chino es Caballo.")
if y == 11:
    print("su horóscopo chino es Cabra.")
else:
    print("Introduzca bien el año")


