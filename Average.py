#Caso 1
#Captura de datos y asignación de variables
N = input('Dame tu nombre: ')
CE = int(input('Captura la calificación de Español: '))
CM = int(input('Captura la calificación de Matemáticas: '))
CH = int(input('Captura la calificación de Historia: '))
CI = int(input('Captura la calificación de Inglés: '))
CD = int(input('Captura la calificación de Deporte: '))

#Cálculo
P = (CE + CM + CH + CI + CD)/5

#Despliegue del resultado
print('{} tu promedio es: {}'.format(N, P))

if P < 7:
    print('Reprobado')
else:
    print('Aprobado')
