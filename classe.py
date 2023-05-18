class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


    def andar(self):
        print(self.nascimento)

pessoa = Pessoa(nome='phillippe', nascimento='09/07/1988')
print(f'Seu nome é {pessoa.nome} e está nasceu em {pessoa.nascimento}')
