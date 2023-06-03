from datetime import date

hoje = date.today()

class Pessoa:
    def __init__(self, nome, nascimento):

        if not isinstance(nascimento, str):
            print(nascimento, type(nascimento))
            raise TypeError
        
        self.nome = nome
        self.nascimento = nascimento
        self.idade = self.calcular_idade()

    def to_dict(self) -> dict:
        return vars(self) #função que recebe um objeto e retorna em dicionario.

    def calcular_idade(self):
        nascimento = self.nascimento

        if len(nascimento) != 10:
            print("erro")
            return -1
            
        for caracter in self.nascimento:
            if caracter not in "/0123456789":
                return -1
        
        nascimento = nascimento.split('/') 
        
        nascimento = {
            "dia":int(nascimento[0]),
            "mes":int(nascimento[1]),
            "ano":int(nascimento[2])
        }
        
        match nascimento["mes"]:
            case  1|3|5|7|8|10|12:  # meses de 31 dias
                if nascimento["dia"] < 1 or nascimento["dia"] >31:
                    print("erro na dia,digite a data novamente")
                    return -1
            case 4|6|9|11:  # meses de 30 dias 
                if nascimento["dia"] < 1 or nascimento["dia"] > 30:
                    print("erro na dia,digite a data novamente")   
                    return -1
            case _:  # meses de 29 dias(se o dia for menor ou maior que 29 ou seja se for 30 acima)
                if nascimento["dia"] < 1 or nascimento["dia"] > 29:
                    print("erro na dia,digite a data novamente")
                    return -1                    
        
        idade = int(hoje.year - nascimento["ano"])
        
        if hoje < date(hoje.year, nascimento["mes"], nascimento["dia"]):
            idade -= 1  # idade = idade - 1
        
        return idade
