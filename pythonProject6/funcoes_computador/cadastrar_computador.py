import json
import secrets


def cadastrar_computador(computadores):
        a = secrets.randbits(9)
        b = secrets.randbits(12)
        marca = input('Escreva a marca: ')
        modelo = input('Escreva o modelo: ')
        ano_de_fabrico = input('Escreva o ano de fabrico: ')
        ID = f'86{a}{b}'
        print(
        f'A marca do seu computador e: {marca} \nO Modelo do seu computador e: {modelo} \nAno de fabrico: {ano_de_fabrico}, \nO Codigo atribuido e: {ID}\nN.B.: Guarde o codigo atribuido pelo sistema.')

        computador = {
            "Marca": marca,
            "Modelo": modelo,
            "Idade": ano_de_fabrico,
            "ID": ID
        }
        computadores.append(computador)


def cadastrar_computador_nos_dados_json():
    dict_ds = {}
    with open('./base_de_dados.json','r') as ds:
        dict_ds = json.load(ds)

    with open('./base_de_dados.json', 'w') as ds:
        try:
            cadastrar_computador(dict_ds['computadores'])
            json.dump(dict_ds,ds)
        except Exception as _:
            json.dump(dict_ds,ds)