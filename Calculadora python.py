def raizes(a,b,c):
    D = (b**2-4*a*c)
    
    x1 = (-b + D**(1/2))/(2*a)
    x2 = (-b - D**(1/2))/(2*a)
    


    if D > 0: print('\nO valor de x1 é: {0}'.format(x1),
                '\nO valor de x2 é: {0}'.format(x2))
    elif D== 0: print('\nOO valor de x1 é : {0}'.format(x1),"Ou",
                '\nO valor de x2 é: {0}'.format(x2))
    else: print('A equação não produz raizes reais.')

    mensagem = "\nRaizes Reais!\n " if type(raizes) == float or int else "As raizes não são reais"
    print(mensagem)


exibeMenu = print("""
******* Calculadora de Equações ****\n
        1 - Fazer cálculo\n
        0 - Sair
      """)
opcao = input('- Digite a sua opção:')
while opcao != 0:
        a = float(input('\n- Digite o coeficiente de a: '))
        b = float(input('- Digite o coeficiente de b: '))
        c = float(input('- Digite o coeficiente de c: '))
        raizes(a,b,c)
        
continuar = input('Deseja Continuar?: \n 1 - Sim\n2 - Não')
if continuar != 2: exibeMenu
