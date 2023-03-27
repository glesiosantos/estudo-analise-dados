print('Bem-vindo a Calculadora')

a = float(input('Insira primeiro número: '))
b = float(input('Insira o segundo número: '))
operador = input('Selecione uma operação (+ , - , * , /): ')
resultado = 0

if(operador == '+'):
  resultado = a + b
  
elif(operador == '-'):
  resultado = a - b
  
elif(operador == '*'):
  resultado = a * b
  
elif(operador == '/'):
  resultado = a / b
else:
  print('Operação inválida')  


print('Primeiro número informado: ', a)
print('Segundo número informado: ', b)
print('Operação selecionada: ', operador)
print('Resultado da operação: ', resultado)