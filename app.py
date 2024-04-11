import os

restaurantes = ['chuchus house','lamen ichiraku']

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
        print(texto)
        print()

def cadastrar_novo_restaurante():
        exibir_subtitulo('cadastro do novo restaurante')
        nome_do_restaurante = input('digite o nome do novo restaurante')
        restaurantes.append(nome_do_restaurante) 
        print(f'o restaurante{nome_do_restaurante} foi cadastrado com sucesso!')
        voltar_ao_menu_principal()

def listar_restaurante():
      exibir_subtitulo('listando os restaurantes')

      for restaurante in restaurantes:
            print(f'*{restaurantes}')

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

   