"""A  partir  delejercicio  anterior, crea  un  programa  para  calcular  la  nota  final  de  un estudiante  universitario.  
Para  ello,  el  usuario  debe  ingresar 3  notas  y  el  valor porcentual de cada nota, realiza y devuelve la media por pantalla."""
#Empty list to store the student's grades
grades_list = []
#Empty list to store the grade weight (%)
grades_weight =[]


#Stores the value for 1 grade
grade = float(input(f"Ingrese el valor de la nota 1: "))
#Stores the weight for i_th grade
weight = float(input(f"Ingrese el peso de la nota 1: "))
#adds grade value to grades_list
grades_list.append(grade)
#adds weight value to weight_list
grades_weight.append(weight)

#Stores the value for 2 grade
grade = float(input(f"Ingrese el valor de la nota 2: "))
#Stores the weight for i_th grade
weight = float(input(f"Ingrese el peso de la nota 2: "))
#adds grade value to grades_list
grades_list.append(grade)
#adds weight value to weight_list
grades_weight.append(weight)

#Stores the value for 3 grade
grade = float(input(f"Ingrese el valor de la nota 3: "))
#Stores the weight for i_th grade
weight = float(input(f"Ingrese el peso de la nota 3: "))
#adds grade value to grades_list
grades_list.append(grade)
#adds weight value to weight_list
grades_weight.append(weight)

#Acummulator to store the total of adding all grades
#Adds the respective value for each grade
sum = grades_weight[0]*grades_list[0] + grades_weight[1]*grades_list[1] +grades_weight[2]*grades_list[2]
#Performs average calculation
mean = sum/len(grades_list)
#Prints student's grades average
print(f"su promedio es: {mean}")