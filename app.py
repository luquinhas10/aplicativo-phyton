import os

restaurantes = [{'nome': 'chuchus house','categoria':'alimento','ativo':False},
                {'nome':'chuchus house','categoria':'verdura','ativo':True},
                {'nome':'pancada sushi','categoria':'sushi','ativo':False}
                ]                         
def exibir_nome_do_programa():
        print(""" LAMEN DO ICHIRAKU 
              """)
def exibir_opcoes():
        print("1-cadastrar restaurante")
        print("2-listar restaurante")
        print("3-ativar restaurante")
        print("4-sair")
        
def finaliza_app():
        exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
        input('\n Digite a tecla "Enter" para voltar ao menu principal')
        main()

def opcao_invalida():
        print('opção inválida!\n')
        voltar_ao_menu_principal()

#print('você escolheu a opção', opcao_escolhida)
#print(f'você escolheu a opção {opcao_escolhida}')

def exibir_subtitulo(texto):
        os.system('clear')
        linha = '*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

def cadastrar_novo_restaurante():
        exibir_subtitulo('cadastro do novo restaurante')
        nome_do_restaurante = input('digite o nome do novo restaurante')
        categoria = input(f'digite a categoria do restaurante {nome_do_restaurante}:')
        dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
        restaurantes.append(dado_do_restaurante)
        print(f'o restaurante{nome_do_restaurante} foi cadastrado com sucesso!')
        voltar_ao_menu_principal()

def listar_restaurante():
      exibir_subtitulo('listando os restaurantes')

      print(f'{"nome do restaurante".ljust(22)}| {"categoria".ljust(20)} | status ')
      for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)}| {ativo}')

      voltar_ao_menu_principal()

def escolher_opcao():
 try:
        opcao_escolhida = int(input('escolha uma opção'))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('ativar restaurante')
        elif opcao_escolhida ==4:
            finaliza_app()    
        else:
            opcao_invalida()
 except:
    opcao_invalida()

def main():
        os.system('clear')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()

if __name__ == '__main__':
    main()
