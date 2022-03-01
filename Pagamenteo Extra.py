# Função Inicial
def main():
    print ("Se deseja fazer o calculo de pagamento extra baseado em:", end = "\n")
    print ("Horas trabalhadas. Digite 1")
    escolha()

# Fução de Escolha
def escolha():
    escolha = int (input(": "))
    if escolha == 1:
        porhoras()

# Calculo de pagamento extra, levando o salário hora como parâmetro 
def porhoras():
    salario = float (input ("\nDigite o seu sálario: "))
    horasnormais = float (input ("Digite a quantidade de horas normalmente trabalhadas: "))
    horasextra = float (input ("Digite a quantidade de horas extra trabalhadas: "))
    salarioHora = salario / (horasnormais*4)
    Extra = salarioHora * horasextra
    salarioTotal = salario + Extra
    print ("\nO valor de cada hora trabalhada é: R$", salarioHora, end = "\n")
    print ("O valor extra a receber para", horasextra, "horas extras trabalhadas é: R$", Extra)
    print ("Seu sálario total esse mês é : R$", salarioTotal)

main()
