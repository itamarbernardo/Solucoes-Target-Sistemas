#Para executar no VS Code, use a opcao Run Python File para permitir que o input seja capturado,
# sem precisar configurar o arquivo tasks.json para isso. 
palavra = str(input('Digite alguma palavra: '))

print(len(palavra))
palavra_inversa = '' 
for i in range(len(palavra)):
    palavra_inversa = palavra[i] + palavra_inversa
    
print(palavra_inversa)