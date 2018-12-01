import sys
from Compromisso import Compromisso

source = open(sys.argv[1])
grade = []
compromissos = []

for i in range(11):
    line = source.readline()
    dias = line.strip('\n').split('\t')
    grade.append(dias)

for line in source.readlines():
    tmp = line.strip('\n').split(';')
    c = Compromisso(int(tmp[0]),tmp[1],int(tmp[2]),int(tmp[3]), tmp[4])
    # '1;tp rv;2;0;/'
    compromissos.append(c)


for compromisso in compromissos:
    print compromisso.id, compromisso.nome, compromisso.horas, compromisso.prioridade, compromisso.continuo