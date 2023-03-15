#Obs: os valores dos dados em .json e .xml sao diferentes, portanto darao resultados distintos
import json
import sys

arquivo = open('dados.json')

menor_valor = sys.float_info.max
maior_valor = 0

cont_zeros = 0
soma_faturamento = 0

dados_dicionario = json.loads(arquivo.read())


for i in range(len(dados_dicionario)):
    if dados_dicionario[i]['valor'] != 0:
        
        soma_faturamento = soma_faturamento + dados_dicionario[i]['valor']
                
        if(dados_dicionario[i]['valor'] < menor_valor):
            menor_valor = dados_dicionario[i]['valor']
        
        if(dados_dicionario[i]['valor'] > maior_valor):
            maior_valor = dados_dicionario[i]['valor']

    else:
        cont_zeros+=1
    
      

print('Menor valor de faturamento ocorrido no mes foi de: ', menor_valor)
print('Maior valor de faturamento ocorrido no mes foi de: ', maior_valor)

#Agora fazemos a media ignorando os dias com faturamento zero 
media_faturamento = soma_faturamento/( len(dados_dicionario) - cont_zeros)
cont_dias_superior_media = 0

for i in range(len(dados_dicionario)):
    if dados_dicionario[i]['valor'] > media_faturamento:
        cont_dias_superior_media += 1

print(soma_faturamento)
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ', cont_dias_superior_media)

arquivo.close()

