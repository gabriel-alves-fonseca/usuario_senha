print('-- Bem vindo ao sistema de senhas --')
dados_user = {}
tentativas = 3




while True:
    escolha = input ('1 - Cadastrar novo usuário\n' \
      '2 - Alterar senha de usuário cadastrado\n' \
      '0 - Sair\n' \
      'Escolha sua opção:')
    if escolha not in ['0','1','2']:
        escolha = input('Opção inválida.\n' \
        '1 - Cadastrar novo usuário\n' \
        '2 - Alterar senha de usuário cadastrado\n' \
        '0 - Sair\n' \
        'Escolha sua opção: ')
    elif escolha == '0':
        print('Saindo... Obrigado por usar nosso sistema')
        break
    
    elif escolha == '1':
        login_user = input('Insira seu nome de usuário: ')
        while True:
            if len(login_user) < 4 or not login_user.isalpha():
                login_user = input('Tente novamente. Nome de usuário deve ter 5 caracteres ou mais e deve ser apenas letras: ')
            else:
                print(f'Usuário {login_user} criado com sucesso!')
                break
        senha_user = input('Insira agora a senha do usuário: ')
        while True:
            if not len(senha_user) >=4:
                senha_user = input('Senha muito curta. Deve ter no mínimo 4 caracteres. Tente novamente: ')
            else:
                dados_user [login_user] = senha_user
                print('Senha salva com sucesso')
                break
    
    elif escolha == '2':
        
        busca_user = input('Para realizar a troca de senha, você deve fornecer o nome de usuário cadastrado: ')
        
        while True:
            if busca_user not in dados_user:
                busca_user = input('Nome de usuário não encontrado. Tente novamente: ')
            else:
                break
        while tentativas > 0:
            teste_senha = input('Insira a senha atual do usuário: ')
            
            if teste_senha == dados_user[busca_user]:
                nova_senha = input(f'Insira agora a nova senha para o usuário {busca_user}: ')    
                while len(nova_senha) < 4:
                    nova_senha = input('Senha muito curta. Deve possuir no mínimo 4 caracteres. Tente novamente: ')
            
                dados_user[busca_user] = nova_senha
                print('Senha nova cadastrada com sucesso!')
                break

                
                
                
            else:
                tentativas -= 1
                if tentativas >0:   
                    print(f'Senha inválida. Você tem {tentativas} tentativas restantes.')
        
        if tentativas == 0:
            print('Limite de tentativas excedido. Tente novamente em 30 minutos!')

