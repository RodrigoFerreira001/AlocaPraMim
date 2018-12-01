class Compromisso:
    def __init__(self,id,nome,horas,prioridade,continuo):
        self.id = id
        self.nome = nome
        self.horas = horas
        self.prioridade = prioridade
        self.continuo = True if continuo == '/' else False