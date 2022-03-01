# Função Inicial
def main():
    print ("Se deseja fazer o calculo de pagamento extra baseado em:", end = "\n")
    print ("Horas trabalhadas. Digite 1")
    print ("Dias trabalhados. Digite 2")
    escolha()

# Fução de Escolha
def escolha():
    escolha = int (input(": "))
    if escolha != 1 and escolha != 2:
        escolha()
    if escolha == 1:
        porhoras()
    if escolha == 2:
        pordias()

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

# Calculo de pagamento extra, levando o salário diário como parâmetro 
def pordias():
    salario = float (input ("\nDigite o seu sálario: "))
    dias = float (input ("Digite a quantidade de dias que normalmente trabalha: "))
    diasextra = float (input ("Digite a quantidade de dias extra trabalhados: "))
    salariodia = salario / dias
    extra = salariodia * diasextra
    salarioTotal = salario + extra
    print ("\nO valor de cada dia trabalhado é: R$", salariodia, end = "\n")
    print ("O valor extra a receber para", diasextra, "dias extras trabalhados é R$:", extra)
    print ("Seu sálario total esse mês é :", salarioTotal)

# Inicialização do programa
main()
