preco_fabrica = float(input('Digite o preço de custo do carro: '))
percentual_lucro_distribuidor = float(input('Digite a porcentagem da margem de lucro do distribuidor: '))
percentual_imposto = float(input('Digite a porcentagem do imposto devido sobre o valor do carro: '))
lucro_distribuidor = preco_fabrica * (percentual_lucro_distribuidor / 100)
valor_imposto = preco_fabrica * (percentual_imposto /100)
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto
print('O lucro sobre o carro do distribuidor é de: ',lucro_distribuidor,'reais')
print('O valor do imposto devido é de: ', valor_imposto,'reais')
print('O preço final do carro é de:', preco_final,'reais')
