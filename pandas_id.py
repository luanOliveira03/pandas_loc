import pandas as pd
carros = pd.read_csv('veiculos/marcas-carro-tratada.csv')

marca = 'CHEVROLET'

resultado = carros.loc[carros['nome'] == marca]
print(resultado)

marca = 'HONDA'

resultado = carros.loc[carros['nome'] == marca]
print(resultado)

marca = 'DAIHATSU'

resultado = carros.loc[carros['nome'] == marca]
print(resultado)