"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import itertools
from collections import Counter
from datetime import datetime
from operator import itemgetter


with open ("data.csv", "r") as file:
        datos = file.readlines()
datos = [line.replace('\t','|').replace('\n','') for line in datos]
datos = [line.split('|')for line in datos]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
def sumar_segunda_columna(datos):
    suma = 0
    for fila in datos:
        suma += int(fila[1])
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
from collections import Counter

def contar_registros(datos):
    contador = Counter([fila[0] for fila in datos])
    lista_tuplas = sorted([(letra, contador[letra]) for letra in contador])
    return lista_tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
def sumar_por_letra(datos):
    suma_por_letra = {}
    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])
        if letra in suma_por_letra:
            suma_por_letra[letra] += valor
        else:
            suma_por_letra[letra] = valor
    resultado = sorted(suma_por_letra.items())
    return resultado


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
from datetime import datetime

def contar_por_mes(datos):
    conteo_por_mes = {}
    for fila in datos:
        fecha = datetime.strptime(fila[2], '%Y-%m-%d')
        mes = fecha.strftime('%Y-%m')
        if mes in conteo_por_mes:
            conteo_por_mes[mes] += 1
        else:
            conteo_por_mes[mes] = 1
    resultado = sorted(conteo_por_mes.items())
    return resultado


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
def max_min_por_letra(datos):
    max_min_por_letra = {}
    for fila in datos:
        letra = fila[0]
        valor = int(fila[1])
        if letra in max_min_por_letra:
            maximo, minimo = max_min_por_letra[letra]
            maximo = max(maximo, valor)
            minimo = min(minimo, valor)
            max_min_por_letra[letra] = (maximo, minimo)
        else:
            max_min_por_letra[letra] = (valor, valor)
    resultado = sorted(max_min_por_letra.items())
    return resultado


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
def min_max_values(datos):
    # Inicializar diccionario de resultados
    result = {}

    # Iterar sobre los datos
    for fila in datos:
        # Decodificar diccionario
        dic = eval(fila[4])

        # Iterar sobre las claves del diccionario
        for clave in dic.keys():
            # Obtener valor asociado a la clave
            valor = dic[clave]

            # Actualizar valores máximos y mínimos
            if clave not in result:
                result[clave] = {'max': valor, 'min': valor}
            else:
                if valor > result[clave]['max']:
                    result[clave]['max'] = valor
                if valor < result[clave]['min']:
                    result[clave]['min'] = valor

    # Convertir diccionario de resultados en lista de tuplas
    result_list = [(clave, result[clave]['min'], result[clave]['max']) for clave in sorted(result.keys())]

    return result_list


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
def asociar_letras(datos):
    diccionario = {}
    for fila in datos:
        valor_col2 = fila[1]
        letra_col1 = fila[0]
        if valor_col2 not in diccionario:
            diccionario[valor_col2] = [letra_col1]
        else:
            diccionario[valor_col2].append(letra_col1)
    lista_tuplas = [(valor, letras) for valor, letras in diccionario.items()]
    return lista_tuplas



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
def lista_tuplas(datos):
    # Crear diccionario vacío
    diccionario = {}

    # Iterar sobre los datos
    for fila in datos:
        # Obtener la segunda columna y la primera columna de la fila
        valor = int(fila[1])
        letra = fila[0]

        # Si el valor no está en el diccionario, agregarlo con una lista vacía
        if valor not in diccionario:
            diccionario[valor] = []

        # Si la letra no está en la lista de letras para este valor, agregarla
        if letra not in diccionario[valor]:
            diccionario[valor].append(letra)

    # Ordenar las claves del diccionario y generar las tuplas
    tuplas = [(valor, sorted(diccionario[valor])) for valor in sorted(diccionario)]

    return tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
def contar_claves(datos):
    conteo = {}
    for fila in datos:
        diccionario = dict(item.split(":") for item in fila[4].split(","))
        claves = diccionario.keys()
        for clave in claves:
            if clave not in conteo:
                conteo[clave] = 1
            else:
                conteo[clave] += 1
    return conteo



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
def contar_elementos(datos):
    conteos = {}
    for fila in datos:
        letra = fila[0]
        if letra not in conteos:
            conteos[letra] = [0, 0]
        conteos[letra][0] += 1
        conteos[letra][1] += len(fila[3]) + len(fila[4])
    lista_tuplas = [(letra, conteos[letra][0], conteos[letra][1]) for letra in sorted(conteos)]
    return lista_tuplas



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
def suma_columna_2_por_letra_columna_4(datos):
    resultados = {}
    for fila in datos:
        letra = fila[3]
        valor = int(fila[1])
        if letra in resultados:
            resultados[letra] += valor
        else:
            resultados[letra] = valor
    return sorted(resultados.items())


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
def sumar_columna5_por_columna1(datos):
    resultado = {}
    for fila in datos:
        columna1 = fila[0]
        columna5 = int(fila[4])
        if columna1 not in resultado:
            resultado[columna1] = 0
        resultado[columna1] += columna5
    return resultado
