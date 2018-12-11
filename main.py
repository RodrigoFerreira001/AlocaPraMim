import sys
from Compromisso import Compromisso
from Ag import AG

source = open(sys.argv[1])
grade = []
compromissos = []

for i in range(15):
    line = source.readline()
    dias = line.strip('\n').split('\t')
    grade.append(dias)

for line in source.readlines():
    tmp = line.strip('\n').split(';')
    # print tmp
    c = Compromisso(int(tmp[0]),tmp[1],int(tmp[2]),int(tmp[3]), tmp[4])
    # '1;tp rv;2;0;/'
    compromissos.append(c)

# for compromisso in compromissos:
#     print compromisso.id, compromisso.nome, compromisso.horas, compromisso.prioridade, compromisso.continuo
# print "grade \n\n",grade,"\n\n grade"


# teste = AG(30, 15, compromissos = compromissos, grade = grade, mutacao_chance = 0.2, geracoes = 1000)
# # teste.print_semana()
# teste.run()

import pandas as pd


r = {}
for i in range(10):
    teste = AG(10, 15, compromissos = compromissos, grade = grade, mutacao_chance = 0.1, geracoes = 1000)
    r[i] = teste.run()
# for i in r.keys():
#     print i,len(r[i])

df = pd.DataFrame(r)
df['average'] = df[df.columns].sum(numeric_only=True, axis=1)/len(df.columns)
print df.describe()
df.to_csv('media_10ind-10porc-maiorQTotal.csv')
