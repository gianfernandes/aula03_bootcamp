valida_nome = False
valida_salario = False
valida_bonus = False

while(valida_nome is False):
  try:
    nome = input("Digite seu nome: ")

    if len(nome) == 0:
      raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
      raise ValueError("O nome não deve conter números.")
    else:
      valida_nome = True
      print("Nome válido:", nome)
  except ValueError as e:
      print(e)

while(valida_salario is False):
  try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
      print("Por favor, digite um valor positivo para o salário.")
    else:
      valida_salario = True
  except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

while(valida_bonus is False):
  try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
      print("Por favor, digite um valor positivo para o bônus.")
    else:
      valida_bonus = True
  except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_final = bonus_recebido * 1.2
kpi = (salario + bonus_final) / 1000
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")