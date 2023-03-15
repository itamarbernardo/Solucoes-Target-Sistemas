#Para executar no VS Code, use a opcao Run Python File para permitir que o input seja capturado,
# sem precisar configurar o arquivo tasks.json para isso. 
numero = int(input('Digite um numero: '))

anterior1 = 0
anterior2 = 1
lista_fibonacci = []

#Vamos add os dois primeiros elementos da sequencia
lista_fibonacci.append(anterior1)
lista_fibonacci.append(anterior2)

cont = 0
#vamos percorrer até que o ultimo elemento da lista seja maior que o numero escolhido
while lista_fibonacci[-1] < numero:
    cont+=1
    proximo = anterior1 + anterior2    
    lista_fibonacci.append(proximo)
    #atualiza os anteriores
    anterior1 = anterior2
    anterior2 = proximo
    

#print(lista_fibonacci)

if numero in lista_fibonacci:
    print('O numero informado pertence a sequencia de fibonacci')
else:
    print('Este numero informado NAO pertence a sequencia de fibonacci')