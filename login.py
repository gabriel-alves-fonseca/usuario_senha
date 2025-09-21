tentativas_troca_senha = 3
dados_user = {}


print('Seja bem vindo ao sistema de login e senha')
while True:
    escolha = input('Selecione uma opção:\n'
    '1 - Para criar um novo usuário\n'
    '2 - Para alterar senha de usuário existente\n'
    '0 - Para sair')
    if escolha not in ['0', '1', '2']:
        escolha_novamente = input('Selecione uma opção válida:\n'
        '1 - Para criar um novo usuário\n'
        '2 - Para alterar senha de usuário existente\n'
        '0 - Para sair')
    elif escolha == '0':
        print('Saindo... Obrigado por acessar nosso sistema')
        break
    elif escolha == '1':
        login_user = input('Insira seu nome de usuário: ')
        while True:
            if not login_user.isalpha() or len(login_user) < 5:
                login_user= input('Insira apenas letras para o seu nome de usuário e no mínimo 5 caracteres: ')
            else:
                print(f'Nome de usuário aceito: {login_user}')
                break
            
        senha_user = input('Insira sua senha de usuário (mínimo 4 caracteres): ')
        while True:
            if len(senha_user) < 4:
                senha_user= input('Sua senha precisa ter pelo menos 4 caracteres: ')
            else:
                print('Senha salva com sucesso')
                break
        dados_user[login_user] = senha_user

    elif escolha == '2':
        busca_user = input('Selecione o nome de usuário que você quer alterar a senha: ')
        
        while True:
            if not busca_user in dados_user:
                busca_user = input('Nome de usuário não encontrado. Tente novamente: ')
            else:
                senha_atual = input(f'Usuário {busca_user} encontrado. Digite agora a senha atual: ')
                
                while tentativas_troca_senha > 0:
                    if senha_atual == dados_user[busca_user]:
                        nova_senha = input('Senha e login aceitos. Agora digite a nova senha para seu usuário (mínimo 4 caracteres): ')
                        while True:
                            if len(nova_senha) < 4:
                                nova_senha = input('Senha precisa ter 4 caracteres os mais: ')
                            
                            
                            
                            
                            else:
                                print('Nova senha salva com sucesso')
                                break
                    else:
                        tentativas_troca_senha -= 1
                        senha_atual = input(f'Senha incorreta para o usuário. Você ainda tem {tentativas_troca_senha} tentativas. Tente novamente: ')
                        if tentativas_troca_senha < 1:
                            print('Você excedeu o número de tentativas válidas. Tente novamente mais tarde')
                            break
                        



                