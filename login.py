senha_correta = "python123" # senha correta para o login salva em uma váriavel
tentativas = 0 # número de tentativas começa em 0

# enquanto o número de tentativas for menor que 3 ele repetirar até chegar no 3
while tentativas < 3:
    # pedido de senha para o usuário digtar
    senha = input("Digite aqui a sua senha: ").strip() # remoção de espaços pelo usuário
    tentativas += 1 # incremento de 1 a tentativas

    # se a senha for igual a senha correta o acesso é liberado com um print "Acesso liberado!"
    if senha == senha_correta:
        print("Acesso liberado!")
        break # aqui o programa para pois a senha foi correta.
    elif tentativas == 3: # se o número de tentativas chegar em 3 a conta é bloqueada e o programa para.
        print("Tentativa de número 3, conta bloqueada!")
    else:
        # aqui é para caso se a senha estiver errada mais a tentativa ainda não chegou em 3.
        print(f"senha errada! tentativa {tentativas} de 3, tente novamente.")

    
