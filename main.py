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

populacao = int(sys.argv[2])
mutacao_chance = float(sys.argv[3])
geracoes = int(sys.argv[4])

print 'populacao', populacao ,'mutacao_chance', mutacao_chance ,'geracoes', geracoes

# teste = AG(tam_populacao = populacao, num_horas_do_dia = 15, compromissos = compromissos, grade = grade, mutacao_chance = mutacao_chance, geracoes = geracoes)
# # teste.print_semana()
# teste.run()

import pandas as pd


r = {}
for i in range(10):
    teste = AG(tam_populacao = populacao, num_horas_do_dia = 15, compromissos = compromissos, grade = grade, mutacao_chance = mutacao_chance, geracoes = geracoes)
    r[i] = teste.run()
# for i in r.keys():
#     print i,len(r[i])

df = pd.DataFrame(r)
df['average'] = df[df.columns].sum(numeric_only=True, axis=1)/len(df.columns)

nome = sys.argv[1].split('.')[0]+'_'+sys.argv[2]+'_'+sys.argv[3]+'_'+sys.argv[4]

print 'CSV CRIADO ',nome
print df.describe()

df.to_csv(nome+'.csv')
