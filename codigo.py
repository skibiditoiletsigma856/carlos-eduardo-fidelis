numeroA = float
numeroB = float

def soma(numeroA, numeroB):
 
  numeroA = int(input("Digite o primeiro número:"))
  print("Primeiro número:", numeroA)
  numeroB = int(input("Digite o segundo número:"))
  print("Segundo número:", numeroB)
  resultado = numeroA + numeroB
  print("somando os dois números...", resultado)
  
def subtracao(numeroA, numeroB):
  numeroA = int(input("Digite o primeiro número:"))
  print("Primeiro número:", numeroA)
  numeroB = int(input("Digite o segundo número:"))
  print("Segundo número:", numeroB)
  resultado = numeroA - numeroB
  print("Subtraindo os dois números...", resultado)

def multiplicacao(numeroA, numeroB):
  numeroA = int(input("Digite o primeiro número:"))
  print("Primeiro número:", numeroA)
  numeroB = int(input("Digite o segundo número:"))
  print("Segundo número:", numeroB)
  resultado = numeroA * numeroB
  print("Multiplacando os dois números", resultado)

def divisao(numeroA, numeroB):
  
  numeroA = int(input("Digite o primeiro número:"))
  print("Primeiro número:", numeroA)
  numeroB = int(input("Digite o segundo número:"))
  print("Segundo número:", numeroB)
  resultado = numeroA / numeroB
  print("dividindo os dois números...", resultado)

def raizquadrada(numeroA):
  numeroA = float(input("Digite o primeiro número:"))
  print("Primeiro número:", numeroA)
  resultado = numeroA ** 0.5
  print("calculando a raiz quadrado fica...",
  resultado)
  
opcao = input("digite qual calculo deseja +, -, r, *, M ")

if opcao == "+":
  soma(numeroA, numeroB)
if opcao == "/":
  divisao(numeroA, numeroB)
if opcao == "-":
  subtracao(numeroA, numeroB)
if opcao == "R" or "r":
  raizquadrada(numeroA)
if opcao == "M" or "m":
  multiplicacao(numeroA, numeroB)

main.py
Exibindo main.py…
