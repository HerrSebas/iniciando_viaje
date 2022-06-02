"""
La siguiente matriz (o lista con listas anidadas) debe cumplir queel cuarto elemento de cada fila se la suma de los tres primeros elementos de la fila respectiva.
Si nota las sumas que se encuentran están erróneas,debe modificarlas dando 2soluciones, una con append y otra con slicing
"""
matriz =[[2,4,3,6],
         [8,3,4,5],
         [7,1,3,10],
         [9,2,1,4]
         ]

matriz[0][3] = matriz[0][0] + matriz[0][1] + matriz[0][2]
matriz[1][3] = matriz[1][0] + matriz[1][1] + matriz[1][2]
matriz[2][3] = matriz[2][0] + matriz[2][1] + matriz[2][2]
matriz[3][3] = matriz[3][0] + matriz[3][1] + matriz[3][2]

print(matriz)
#append aproach

matrix = [[2,4,3],
         [8,3,4],
         [7,1,3],
         [9,2,1]
         ]
matrix[0].append(matrix[0][0] + matrix[0][1] + matrix[0][2])
matrix[1].append(matrix[1][0] + matrix[1][1] + matrix[1][2])
matrix[2].append(matrix[2][0] + matrix[2][1] + matrix[2][2])
matrix[3].append(matrix[3][0] + matrix[3][1] + matrix[3][2])
print(matrix)