"""Debes utilizar todo lo que sabes sobre los strings, las listas y sus métodos o funciones para transformar el siguiente texto:
thorlanzó su martillo#flashha fallado por un pie! -gritóLoki Laufeyson#dos pies-le   corrigió Hulk#flashmenea   la   cabeza   como   disgustado...-agrega   
el comentaristaEn:Thor lanzó su martillo...-¡Flash ha fallado por un pie!-gritó LokiLaufeyson.
-Dos pies le corrigió Hulk.-Flashmenea la cabeza como disgustado... -
agrega el comentarista.Es prohibido modificar directamente el texto."""

#contains the text
string = """thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado... -agrega el comentarista"""
#split the text according to '#'
splitted_string = string.split("#")
#empty list to store capitalized lines
capitalized_str = []

#Capitalize each line and adds it to capitalized_str list
capitalized_str.append(splitted_string[0].capitalize())
capitalized_str.append(splitted_string[1].capitalize())
capitalized_str.append(splitted_string[2].capitalize())
capitalized_str.append(splitted_string[3].capitalize())

#Converts loki to Loki
capitalized_str[1] = capitalized_str[1].replace("loki", "Loki")
#Converts laufeyson to Laufeyson
capitalized_str[1] = capitalized_str[1].replace("laufeyson", "Laufeyson")
#Converts hulk to Hulk
capitalized_str[2] = capitalized_str[2].replace("hulk", "Hulk")

#Inserts '-' in position 1 for capitalized string
capitalized_str.insert(1,'-')
#Inserts '-' in position 2 for capitalized string
capitalized_str.insert(3,'-')
#Inserts '-' in position 3 for capitalized string
capitalized_str.insert(5,'-')

# stores the modified string with the desire output format
modified_string = f"""{capitalized_str[0]}\n\
    {capitalized_str[1]}{capitalized_str[2]}
    {capitalized_str[3]}{capitalized_str[4]}
    {capitalized_str[5]}{capitalized_str[6]}
"""
# shows the modified string
print(modified_string)