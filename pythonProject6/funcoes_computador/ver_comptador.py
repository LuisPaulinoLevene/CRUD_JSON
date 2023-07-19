import json
def ver_computador(computadores):
    ID = input('Escreva o codigo computador: ')
    for computador in computadores:
        if computador['ID'] == ID:
            print(computador)

def ver_computador_no_dados_json():
    dict_ds ={}
    with open('./base_de_dados.json', 'r') as ds:
        dict_ds = json.load(ds)
        ver_computador(dict_ds['computadores'])