'''
Codificacion de Software de Sistemas
2-I Torres Jimenez Job Esau
01/04/2025
'''
class AlumnosDelCBTIS246():
    def almacenar_a_un_estudiante_ejemplar(self, nombre_del_archivo):
        nombre = input("¿Como te llamas? ")
        edad = input("¿Cual es tu edad? ")
        fecha = input("Escribe tu fecha de nacimiento ")

        texto=[nombre+'\n',edad+'\n',fecha+'\n']
        with open(nombre_del_archivo, 'a') as fichero:
            fichero.writelines(texto)

    def leer_el_archivo_de_alumnos_ejemplares(self, nombre_del_archivo):
        with open('alumnos.txt', 'r') as fichero:
            for line in fichero.readlines():
                print(line, end='')

clase_de_2_I = AlumnosDelCBTIS246()
clase_de_2_I.almacenar_a_un_estudiante_ejemplar('alumnos.txt')
clase_de_2_I.leer_el_archivo_de_alumnos_ejemplares('alumnos.txt')
