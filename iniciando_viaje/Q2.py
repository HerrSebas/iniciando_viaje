"""
Realizar un programa que le solicite a 3 usuariosingresar por teclado información personal, la  informaciónde  cada  usuario  se  debe guardaren  una  estructura  de colección  inmutable, luego  mostrar  por  pantallala  información  de  los  usuarios agrupada en unaestructura de colección mutable.
La información para solicitares:
a.Nombres y apellidos.
b.Ocupación.
c.Edad.
d.Ciudad.
e.Número de contacto.
f.Correo electrónico.

"""
#Empty list to store all users information
users_list = []

 #Empty list for every user
user_one = []
user_two = []
user_three = []

#The folowwing block gets information from user_1 and stores it in users_list
#Prompts for user´s name and stores it
name = input("Ingrese su nombre: ")
#Adds user's name to his/her list
user_one.append(name)
#Prompts for user´s profession and stores it
profession = input("Ingrese su ocupación: ")
#Adds user's profession to his/her list
user_one.append(profession)
#Prompts for user´s age and stores it
age = input("ingrese su edad: ")
#Adds user's age to his/her list
user_one.append(age)
#Prompts for user´s location and stores it
location = input("En qué ciudad se encuentra?: ")
#Adds user's location to his/her list
user_one.append(location)
#Prompts for user´s contact and stores it
contact = input("Ingrese su número de telefono: ")
#Adds user's contact to his/her list
user_one.append(contact)
#Prompts for user´s email and stores it
email = input("ingrese su correo electronico: ")
#Adds user's email to his/her list
user_one.append(email)
#converts single_user_list to tuple
user_one_tuple = tuple(user_one)
#adds each user´s tuple to users_list
users_list.append(user_one_tuple)

print("____________")
#Same procedure from user_one but to get user_two information
name = input("Ingrese su nombre: ")
user_two.append(name)
profession = input("Ingrese su ocupación: ")
user_two.append(profession)
age = input("ingrese su edad: ")
user_two.append(age)
location = input("En qué ciudad se encuentra?: ")
user_two.append(location)
contact = input("Ingrese su número de telefono: ")
user_two.append(contact)
email = input("ingrese su correo electronico: ")
user_two.append(email)
user_two_tuple = tuple(user_two)
users_list.append(user_two_tuple)

print("____________")
#Same procedure from user_one but to get user_three information
name = input("Ingrese su nombre: ")
user_three.append(name)
profession = input("Ingrese su ocupación: ")
user_three.append(profession)
age = input("ingrese su edad: ")
user_three.append(age)
location = input("En qué ciudad se encuentra?: ")
user_three.append(location)
contact = input("Ingrese su número de telefono: ")
user_three.append(contact)
email = input("ingrese su correo electronico: ")
user_three.append(email)
user_three_tuple = tuple(user_three)
users_list.append(user_three_tuple)
#prints the list with all users
print(users_list)

    