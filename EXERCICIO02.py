#EXERCICIO 01
lista_nomes = []
for i in range(4):
    nome = input("DIGITE O NOME A SER ARMAZENADO: ").strip().title()
    lista_nomes.append(nome)
print(f"NOMES QUE FORAM ARMAZENADOS: {lista_nomes}")

#EXERCICIO 02
lista_telefone = []
for i in range(4):
    telefone = input("DIGITE O NÚMERO TELEFONE: ").replace("(","").replace(")","").replace(" ","").replace("-","")
    lista_telefone.append(telefone)
print(f"LISTA DE TELEFONES: {lista_telefone}")

#EXERCICIO 03
lista_vendedor = []
for i in range(3):
    nome = input("DIGITE O NOME: ").lower().strip()
  
    if nome == "":
        print("INFORMAÇÃO INVALIDA!!!")
        continue
    else:
        lista_vendedor.append(nome)
print(f"LISTA DE VENDEDORES: {lista_vendedor}")