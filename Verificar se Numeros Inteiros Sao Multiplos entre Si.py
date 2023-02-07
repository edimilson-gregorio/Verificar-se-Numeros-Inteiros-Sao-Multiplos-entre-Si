a = int(input("Insira o primeiro valor inteiro: "))
b = int(input("Insira o segundo valor inteiro: "))

if a % b == 0 or b % a == 0:
  print("São Múltiplos")
else:
  print("Não são Múltiplos")
