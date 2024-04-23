import os

restaurantes = [{'nome': 'chuchus house','categoria':'alimento','ativo':False},
                {'nome':'chuchus house','categoria':'verdura','ativo':True},
                {'nome':'pancada sushi','categoria':'sushi','ativo':False}
                ]                         
def exibir_nome_do_programa():
        ''' está exibindo o nome do programa
        '''
        print(""" LAMEN DO ICHIRAKU 
              """)
def exibir_opcoes():
        '''está exibindo o nome do programa
        input:
        -escolha de opções
        '''
        print("1-cadastrar restaurante")
        print("2-listar restaurante")
        print("3-ativar restaurante")
        print("4-sair")
        
def finaliza_app():
        '''está finalizando o aplicativo
        '''
        exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
        ''' volta ao menu principal
        input:
        -digite a tecla "enter"
        '''
        input('\n Digite a tecla "Enter" para voltar ao menu principal')
        main()

def opcao_invalida():
        '''mostra ao usuário que a opção escolhida é inválida
        -volta ao menu principal
        '''
        print('opção inválida!\n')
        voltar_ao_menu_principal()

#print('você escolheu a opção', opcao_escolhida)
#print(f'você escolheu a opção {opcao_escolhida}')

def exibir_subtitulo(texto):
        '''exibe o suntítulo do texto
        '''
        os.system('clear')
        linha = '*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

def cadastrar_novo_restaurante():
        '''esta função é responsável por cadastrar um novo restaurante
        input:
        -nome do retaurante
        -categoria
        output:
        -adicionar um novo restaurante a lista de restaurantes
           '''

        exibir_subtitulo('cadastro do novo restaurante')
        nome_do_restaurante = input('digite o nome do novo restaurante')
        categoria = input(f'digite a categoria do restaurante {nome_do_restaurante}:')
        dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
        restaurantes.append(dado_do_restaurante)
        print(f'o restaurante{nome_do_restaurante} foi cadastrado com sucesso!')
        voltar_ao_menu_principal()

def listar_restaurante():
      '''está listando um restaurante
      -nome do restaurante
      -categoria do restaurante
      -volta ao  menu principal
      '''

      exibir_subtitulo('listando os restaurantes')

      print(f'{"nome do restaurante".ljust(22)}| {"categoria".ljust(20)} | status ')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)}| {ativo}')

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      ''' alterna o estado do restaurante
      input:
      -nome alterado
      -restaurante encontrado
      output:
      - o restaurante foi encontrado
      - o restaurante não foi encontrado

      - volta ao menu principl
      '''
      exibir_subtitulo('alternando estado do restaurante')
      nome_restaurante = input('digite o nome do restaurante que deseja alterar o estado:')
      restaurante_encontrado = False 

      for restaurante in restaurantes:
       if nome_restaurante == restaurante['nome']:
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['nome']
        mensagem  = f'o restaurante {nome_restaurante} foi avisado com sucesso' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
        print(mensagem)

      if not restaurante_encontrado:
            print('o restaurante não foi encontrado')
      voltar_ao_menu_principal()

def escolher_opcao():
      '''  serve para que o usuario possa selecionar opções
      input:
      - cadastrar restaurante
      -listar restaurante
      -alternar estado do restaurante
      -finaliza app

      excessão:
      -opção inválida
    '''
try:
        opcao_escolhida = int(input('escolha uma opção'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida ==4:
            finaliza_app()    
        else:
            opcao_invalida()
except:
    opcao_invalida()

def main():
        ''' define o app como um todo
        -exibe nome do programa
        -exibe opções
        -exibe escolha de opções
        '''
        os.system('clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()
