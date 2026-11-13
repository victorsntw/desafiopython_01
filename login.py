senha_correta = "python123"
tentativas = 0

while tentativas < 3:
    senha = input("Digite aqui a sua senha: ").strip()
    tentativas += 1

    if senha == senha_correta:
        print("Acesso liberado!")
        break
    elif tentativas == 3:
        print("Tentativa de número 3, conta bloqueada!")
    else:
        print(f"senha errada! tentativa {tentativas} de 3, tente novamente.")

    