#escribir una solucion que pregunte al usuario
#su nombre y apellido, desplegar el texto en 
#pantalla invertido con un espacio entre ellos

nombre = input("cual es tu nombre")
apellido = input("cual es tu apellido")
print(nombre[::-1] ,apellido[::-1])


#Crear una solucion que le pregunte al usuario 
#su nombre y edad. Entonces escribir un mensaje
#que le diga el año en el que puede llegar a tener
#100 años de edad

edad = int(input("cuantos años tienes"))
nombre = input("como te llamas")
print("en 100 años tendras" ,edad+100)
