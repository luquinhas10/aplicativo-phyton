import os

print(""" LAMEN DO ICHIRAKU 
""")

print("1-cadastrar restaurante")
print("2-listar restaurante")
print("3-ativar restaurante")
print("4-sair")
#https://fsymbols.com/pt/letras/

opcao_escolhida = int(input('escolha uma opção'))
#print('você escolheu a opção', opcao_escolhida)
#print(f'você escolheu a opção {opcao_escolhida}')

def finaliza_app():
    os.system('cis')
    print('encerrando o programa\n')

if opcao_escolhida == 1:
    print('cadastrar restaurante')
elif opcao_escolhida == 2:
    print('listar restaurantes')
elif opcao_escolhida == 3:
    print('ativar restaurante')
else:
    finaliza_app()