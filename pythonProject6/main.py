from funcoes_computador import cadastrar_computador
from funcoes_computador import ver_comptador
from funcoes_computador import ver_computadores

while True:
                print('''
                1- cadastrar um computador
                2- ver um computador cadastrado
                3- ver  todos computadores cadastrados
                ''')
                entrada = input('Escolha a opcao do que deseja fazer: ')
                if entrada == '1':
                    cadastrar_computador.cadastrar_computador_nos_dados_json()
                elif entrada == '2':
                    ver_comptador.ver_computador_no_dados_json()
                elif entrada == '3':
                    ver_computadores.ver_computadores_no_json()
                elif entrada == '0':
                    break