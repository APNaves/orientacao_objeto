from pessoa import Pessoa
import json

arquivo = open("arquivo.json", "r")
lista = list(json.load(arquivo))

for pessoa in lista:
    pessoa_obj = Pessoa(
        pessoa["nome"],
        pessoa["nascimento"]
    )

    if pessoa_obj.idade == -1:
        print('invalida\n')
        continue
        raise ValueError

    print('\n')
    print(f"\nO seu nome é {pessoa_obj.nome}, a sua idade é {pessoa_obj.idade}")

pergunta = input('Deseja adcionar uma pessoa a lista? \n')

if pergunta.upper() == 'S':
    nome = input('Qual o nome da nova pessoa? \n')
    nascimento = input('Qual a data de nascimento da nova pessoa? \n')

    pessoa_nova = Pessoa(nome, nascimento)
    lista.append(pessoa_nova.to_dict())

print('fim!')

with open('arquivo.json', 'w+') as f:
    f.write(json.dumps(lista, indent=4))
