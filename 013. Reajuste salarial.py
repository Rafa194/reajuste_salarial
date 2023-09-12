salario = float(input('Qual o salario do funcionario? '))
reajuste = salario * (15/100)
salario_reajuste = salario + reajuste
print('O funcionario que ganhava R${:.2f}, com 15% de aumento'
      ' passará a receber R${:.2f}.'.format(salario, salario_reajuste))