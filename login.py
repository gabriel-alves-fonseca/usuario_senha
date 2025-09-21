tentativas = 0
lista_senhas = {}


print('Seja bem vindo ao sistema de login e senha')
while True:
    escolha = input('Selecione uma opção:\n'
    '1 - Para criar um novo usuário\n'
    '2 - Para alterar senha de usuário existente\n'
    '0 - Para sair')
    if not escolha.isnumeric() and escolha != '0' '1' '2':
        escolha_novamente = input('Selecione uma opção válida:\n'
        '1 - Para criar um novo usuário\n'
        '2 - Para alterar senha de usuário existente\n'
        '0 - Para sair')
    elif escolha == '1':
        login_user = input('Insira seu nome de usuário: ')
        while True:
            if not login_user.isalpha() or len(login_user) < 5:
                login_user= input('Insira apenas letras para o seu nome de usuário e no mínimo 5 caracteres: ')
            else:
                print(f'Nome de usuário aceito: {login_user}')
                break
            
        senha_user = input('Insira sua senha de usuário (mínimo 4 caracteres): ')
        if len(senha_user) < 4:
            senha_user= input('Sua senha precisa ter pelo menos 4 caracteres: ')
        else:
            print('Senha salva com sucesso')
    elif escolha == '2':
        busca_user = input('Selecione o nome de usuário que você quer alterar a senha')
        
    
   


    

    




















#for i in range(2):
 #   login_correto = input("insira um nome de usuário: ")
  #  senha_correta = input("insira uma senha para o usuário: ")
   # lista_senhas[login_correto] = login_correto,senha_correta

#while tentativas <= 2:
 #   login = input("digite seu login: ")
  #  senha = input("digite sua senha: ")
   # if  login == login_correto and senha == senha_correta:
    #    print("bem vindo, ", login_correto)
     #   break
    #else:
     #   tentativas += 1
      #  if tentativas <= 2:
       #     print(f"senha e/ou login incorretos. Você realizou {tentativas} tentativas. Tente novamente.")

    #if tentativas == 3 and senha != senha_correta or login != login_correto:
     #   print(f"Você realizou {tentativas} tentativas inválidas. Deve esperar 30 minutos para poder tentar novamente")