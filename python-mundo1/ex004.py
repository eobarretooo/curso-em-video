nome = str(input("Qual seu nome: "))
idade = input("Qual sua idade: ")

print('o tipe é:', type(nome))
print('é alpha numerico?:', nome.isalnum())
print('é alfabetico?:', nome.isalpha())
print('é um numero?:', nome.isnumeric())
print('é em maiusculo?:', nome.isupper())
print('da para imprimir?:', nome.isprintable())

print("Agora o da idade")

print('o tipe é:', type(idade))
print('é alpha numerico?:', idade.isalnum())
print('é alfabetico?:', idade.isalpha())
print('é um numero?:', idade.isnumeric())
print('é em maiusculo?:', idade.isupper())
print('da para imprimir?:', idade.isprintable())
