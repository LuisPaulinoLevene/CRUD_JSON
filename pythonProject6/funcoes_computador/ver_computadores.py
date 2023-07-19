import json
def ver_computadores(computadores):
    for computador in computadores:
        print(computador)

def ver_computadores_no_json():
    dict_ds ={}
    with open('./base_de_dados.json', 'r') as ds:
        dict_ds = json.load(ds)
        ver_computadores(dict_ds['computadores'])