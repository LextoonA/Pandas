import pandas as pd

jugadores_Liverpool = pd.Series (
    ["Alisson", "Luis Diaz", "Macalister", "Salah"],
)
# Creamos diccionario
liv_dict = {1: "Alisson", 7: "Luis Diaz", 10: "Macalister", 11: "Salah"}

#Creamos una serie de pandas usando el diccionario 
liv_jugadores_dict = pd.Series(liv_dict)
# Imprimimos la serie a partir del diccionario
print (liv_jugadores_dict)
# Imprimimos el valor en la posición (indice) 7 de la serie creada a partir del diccionario
print (liv_jugadores_dict[7])
print (liv_jugadores_dict[0:3])

# Diccionario con datos de jugadores
dict = {"jugador": ["Alisson", "Luis Diaz", "Macalister", "Salah"],
        "Altura": [1.93, 1.78, 1.76, 1.75],
        "Goles": [0,31,33,294]
}

# Crear un DataFrame con el diccionario e indices personalizados
df = pd.DataFrame (dict, index=[1,7,10,11])

#imprimir dataframe
print(df)


