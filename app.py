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



opcao_escolhida = int(input('escolha uma opção'))
#print('você escolheu a opção', opcao_escolhida)
#print(f'você escolheu a opção {opcao_escolhida}')

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def escolher_opcao():
 if opcao_escolhida == 1:
    print('cadastrar restaurante')
 elif opcao_escolhida == 2:
    print('listar restaurantes')
 elif opcao_escolhida == 3:
    print('ativar restaurante')
 else:
    finaliza_app()
    
def main():
   os.system('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

   if __name__ == '__main__':
       main()

   