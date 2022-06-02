"""
Realizar un programa que permita ingresar grados Fahrenheit
y muestre por pantalla el  dato en  grados centígradoso  pasar  de  grados centígrados
a  grados  Fahrenheit(puede realizar cualquiera de los dos programas).
"""
fahrenheit_degrees = float(input("ingrese la medida en grados Fahrenheit: "))
#Do the convertion from F° to C°
celcius_degrees = (fahrenheit_degrees-32)*5/9
#Shows the input measure in Celcius
print(f"La temperatura, en grados celcius es de: {celcius_degrees}°")