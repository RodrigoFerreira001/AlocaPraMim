import sys
from Compromisso import Compromisso
from Ag import AG

source = open(sys.argv[1])
grade = []
compromissos = []

for i in range(11):
    line = source.readline()
    dias = line.strip('\n').split('\t')
    grade.append(dias)

for line in source.readlines():
    tmp = line.strip('\n').split(';')
    print tmp
    c = Compromisso(int(tmp[0]),tmp[1],int(tmp[2]),int(tmp[3]), tmp[4])
    # '1;tp rv;2;0;/'
    compromissos.append(c)

for compromisso in compromissos:
    print compromisso.id, compromisso.nome, compromisso.horas, compromisso.prioridade, compromisso.continuo
# print "grade \n\n",grade,"\n\n grade"


teste = AG(6, 11, compromissos = compromissos, grade = grade, mutacao_chance = 0.2, geracoes = 50)
# teste.print_semana()
teste.run()
