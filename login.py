tentativas = 0
lista_senhas = {}
for i in range(2):
    login_correto = input("insira um nome de usuário: ")
    senha_correta = input("insira uma senha para o usuário: ")
    lista_senhas[login_correto] = login_correto,senha_correta

while tentativas <= 2:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    if  login == login_correto and senha == senha_correta:
        print("bem vindo, ", login_correto)
        break
    else:
        tentativas += 1
        if tentativas <= 2:
            print(f"senha e/ou login incorretos. Você realizou {tentativas} tentativas. Tente novamente.")

    if tentativas == 3 and senha != senha_correta or login != login_correto:
        print(f"Você realizou {tentativas} tentativas inválidas. Deve esperar 30 minutos para poder tentar novamente")