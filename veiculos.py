import pandas as pd
carros = pd.read_csv('veiculos/marcas-carros.csv')
print(carros.head())

caminhao = pd.read_csv('veiculos/marcas-caminhao.csv')
print(caminhao.head())

motos = pd.read_csv('veiculos/marcas-motos.csv')
print(motos.head())

nautica = pd.read_csv('veiculos/marcas-nautica.csv')
print(nautica.head())