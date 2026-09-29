aluno = input('Digite seu nome: ')
livro = input('Qual foi o livro alugado: ')
dias = int(input('Informe a quantidade de dias em atraso: '))
multa_1 = 1.50
multa_2 = 2.00
multa_3 = 3.00

if dias > 0 and dias <= 3:
  multa = multa_1 * dias
  print(f'{aluno}, a entrega do livro {livro} teve atraso de {dias} dias. A multa por dia é R$ {multa_1:.2f}. Total a ser pago é R$ {multa:.2f}.')
elif dias >= 4 and dias <= 7:
  multa = multa_2 * dias
  print(f'{aluno}, a entrega do livro {livro} teve atraso de {dias} dias. A multa por dia é R$ {multa_2:.2f}. Total a ser pago é R$ {multa:.2f}.')
else:
  multa = multa_3 * dias
  print(f'{aluno}, a entrega do livro {livro} teve atraso de {dias} dias. A multa por dia é R$ {multa_3:.2f}. Total a ser pago é R$ {multa:.2f}.')