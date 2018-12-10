#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class AG:
    def __init__(self, tam_populacao, num_horas_do_dia, compromissos, grade, geracoes, mutacao_chance):


        print "recebi: "

        horasParaAlocar = sum([c.horas for c in compromissos])

        horasDisponiveis = sum([1 for i in grade for j in i if j=='0'])

        print "horas Para Alocar",horasParaAlocar,'horas Disponiveis na semana',horasDisponiveis

        # grade transposta para que linhas = horas colunas = dias
        self.geracoes = geracoes
        self.mutacao_chance = mutacao_chance
        self.grade = map(list, zip(*grade))
        self.populacao = []
        self.num_horas_do_dia = num_horas_do_dia
        self.tam_populacao = tam_populacao
        self.compromissos = compromissos

        self.best = []
        self.best.append([0,0.0])

        # semana = [[dia],[dia],[dia],[dia],[dia]]
        # dia = [15 horas (8 as 23)], depende de num_horas_do_dia considerado


        # Inicializar populacao
        for _ in range(self.tam_populacao):

            # 5 = dias da semana seg a sex
            semana = []
            for i in range(5):
                # [0] * 5 = [0,0,0,0,0]
                semana.append([0]*self.num_horas_do_dia)

            self.populacao.append(semana)

        # sortear horarios da semana para marcar
        for semana in self.populacao:
            compromissoAlocados = self.get_compromissos(compromissos,horasDisponiveis)
            print [i.id for i in compromissoAlocados]
            for c in compromissoAlocados:
                horarios = []
                while len(horarios) < c.horas:
                    temp = (random.randint(0,4),random.randint(0,self.num_horas_do_dia-1))

                    if temp not in horarios:
                        horarios.append(temp)

                for j in horarios:
                    semana[j[0]][j[1]] = c.id

        temp = []
        for semana in self.populacao:
            temp.append([semana,0.0])


        self.populacao = temp[:]
        # print self.populacao

    def get_compromissos(self, compromissos, horasDisponiveis):

        h = 0
        compromissoAlocados = []

        temp = sorted(compromissos,key = lambda X:X.prioridade, reverse = True)

        while h < horasDisponiveis:

            c = random.sample(temp,1)[0]
            # print "**--**"*10
            # print c,c.horas,c.nome
            if c not in compromissoAlocados:
                h += c.horas
                compromissoAlocados.append(c)

        # print h
        if h > horasDisponiveis:
            compromissoAlocados = compromissoAlocados[:-1]
        # print [c.id for c in compromissoAlocados]
        return compromissoAlocados


    def print_semana(self):
        for semana in self.populacao:
            # print "individuo \n\n"
            print "fit",semana[1]
            temp = []
            print "seg  ter  qua  qui  sex"
            print "\n"

            # print semana[0]
            # print semana[0][1][0]

            for i in range(self.num_horas_do_dia):
                for dia in semana[0]:
                    print dia[i],"\t",

                print '\n'

        print "\n\n"

        print 'MELHOR SOLUCAO'
        s = max(self.populacao, key = lambda X:X[1])

        dt = {c.id : c.nome for c in self.compromissos}
        dt[0] = '-'*10

        print "fit",s[1]
        # print dt
        temp = []
        # "+" "*5+"
        print "seg"+" "*14+"ter"+" "*14+"qua"+" "*14+"qui"+" "*14+"sex"
        print "\n"



        for i in range(self.num_horas_do_dia):
            for dia in s[0]:
                print dt[dia[i]]+' '*(10-len(dt[dia[i]]))+'\t',

            print '\n'



    def crossover(self):
        # Inicializar filhos
        # 5 = dias da semana seg a sex
        new_pop = []
        while len(new_pop) < self.tam_populacao:
            f1 = []
            f2 = []

            for i in range(5):
                # [0] * 5 = [0,0,0,0,0]
                f1.append([0]*self.num_horas_do_dia)
                f2.append([0]*self.num_horas_do_dia)

            # print '___'*10
            # print 'antes',self.num_horas_do_dia
            # print "F1",len(f1),len(f1[0])
            # print "F2",len(f2),len(f2[0])

            p = random.sample(self.populacao, 2)
            pai1 = max(p,key = lambda X:X[1])

            p = random.sample(self.populacao, 2)
            pai2 = max(p,key = lambda X:X[1])
            # p = sorted(p , key = lambda X:X[1], reverse = True)
            # pai2 = p[1]
            # print 'escolhidos', pai1[1], pai2[1]

            #  coletando compromissos unicos de cada grade
            temp = []
            for i,dia in enumerate(pai1[0]):
                for j,hora in enumerate(dia):
                    if pai1[0][i][j] != 0 and pai1[0][i][j] not in temp:
                        temp.append(pai1[0][i][j])
                    if pai2[0][i][j] != 0 and pai2[0][i][j] not in temp:
                        temp.append(pai2[0][i][j])

            # print 'TEMP' , temp

            # escrevedo primeira metade dos compromissos
            for i,dia in enumerate(pai1[0]):
                for j,hora in enumerate(dia):
                    # print i,j , pai1[0][i][j] , pai1[0][i]
                    if pai1[0][i][j] in temp[:len(temp)/2]:
                        # print '--'*10
                        f1[i][j] = pai1[0][i][j]
                        # print pai1
                        # print "\n\n",f1

            for i,dia in enumerate(pai2[0]):
                for j,hora in enumerate(dia):
                    # print i,j , pai2[0][i][j] , pai2[0][i]
                    if pai2[0][i][j] in temp[:len(temp)/2]:
                        # print '--'*10
                        f2[i][j] = pai2[0][i][j]
                        # print pai1
                        # print "\n\n",f1
            # print'PRIMEIRA METADE DOS FILHOS'
            # print 'f1:',f1
            # print '\n\n f2:',f2
            #

            # escrevedo segunda metade dos compromissos
            for i,dia in enumerate(pai1[0]):
                for j,hora in enumerate(dia):
                    # print i,j , pai1[0][i][j] , pai1[0][i]
                    if pai1[0][i][j] in temp[len(temp)/2:]:
                        if f2[i][j] == 0:
                            f2[i][j] = pai1[0][i][j]
                        else:
                            flag = 0
                            # procurando proximo intervalo vazio
                            for k in range(i,len(f2))+range(0,i):
                                for l in range(j,len(f2[0]))+ range(0,j):
                                    if flag == 1:
                                        break
                                    if f2[k][l] == 0:
                                        f2[k][l] = pai1[0][i][j]
                                        flag = 1


            for i,dia in enumerate(pai2[0]):
                for j,hora in enumerate(dia):
                    # print i,j , pai2[0][i][j] , pai2[0][i]
                    if pai2[0][i][j] in temp[len(temp)/2:]:
                        if f1[i][j] == 0:
                            f1[i][j] = pai2[0][i][j]
                        else:
                            flag = 0
                            # procurando proximo intervalo vazio
                            for k in range(i,len(f1))+range(0,i):
                                for l in range(j,len(f1[0]))+ range(0,j):
                                    if flag == 1:
                                        break
                                    if f1[k][l] == 0:
                                        f1[k][l] = pai2[0][i][j]
                                        flag = 1

            # print "__*__"*10
            # print "Depois"
            # print '\n'
            # print "F1",len(f1),len(f1[0])
            # print "F2",len(f2),len(f2[0])

            new_pop.append([f1,0.0])
            new_pop.append([f2,0.0])

            # elitismo de 1
            a = max(self.populacao,key = lambda X:X[1])
            new_pop.append(a)

        # print "CRUZAMENTO: "
        # print "pai1",pai1,"\n\n"
        # print "pai2",pai2,"\n\n"
        # print "f1",f1,"\n\n"
        # print "f2",f2,"\n\n"


        # print "nova pop gerada"
        self.populacao = new_pop[:]
        # print  self.populacao


        # print '--'*20,temp[:len(temp)/2],temp[len(temp)/2:]
        # print pai1,"\n\n",pai2,"\n\n", f2


    def mutacao(self):
        # print "MUTACAO \n\n"
        # print semana
        for semana in self.populacao:
            # comp = self.compromissos[:]
            # comp = [c for c in self.compromissos]
            if random.random() <= self.mutacao_chance:

                compromissoMutado = []
                for i,dia in enumerate(semana[0]):
                    for j,hora in enumerate(dia):
                        if semana[0][i][j] != 0 and semana[0][i][j] not in compromissoMutado:
                            compromissoMutado.append(semana[0][i][j])

                compromissoMutado = compromissoMutado[random.randint(0,len(compromissoMutado)-1)]

                # print'mutacao compromissos'
                # print compromissoMutado
                # print [c.id for c in self.compromissos]
                for c in self.compromissos:
                    if c.id == compromissoMutado:
                        compromissoMutado = c

                # print "compromisso mutado:",compromissoMutado.id,compromissoMutado.nome,compromissoMutado.horas

                novoHorario = []
                # print'antes do while :'
                # print semana
                # print '\n\n'
                while len(novoHorario) < compromissoMutado.horas:
                    temp = (random.randint(0,4),random.randint(0,self.num_horas_do_dia-1))

                    # print'mutacao temp:',temp,novoHorario,semana
                    if semana[0][temp[0]][temp[1]] == 0:
                        # print'mutacao: horas no dia',self.num_horas_do_dia
                        novoHorario.append(temp)


                for i,dia in enumerate(semana[0]):
                    for j,hora in enumerate(dia):
                        if semana[0][i][j] == compromissoMutado.id:
                            semana[0][i][j] = 0

                for j in novoHorario:
                    semana[0][j[0]][j[1]] = compromissoMutado.id

                # print "MUTADO\n\n"
                # print semana
                print "mutacao OK"
                # return semana


    def fitness(self):
        # fit = 1/ penalidades

        compromissosContinuos = [c.id for c in self.compromissos if c.continuo == True]

        # contando penalidades

        for semana in self.populacao:
            # print semana
            penalidade = 0
            compromissosAlocados = []

            for i,dia in enumerate(semana[0]):
                # print "__"*10, "i:" ,i , dia
                for j,hora in enumerate(dia):
                    # print i,j,self.grade[i][j],semana[0][i][j],len(self.grade)
                    # print '*----*'*10
                    # print 'i',i,'j',j,len(dia),len(semana[0]),len(self.grade),len(self.grade[0])
                    if (i < len(self.grade) and j < len(self.grade[0])) and (self.grade[i][j] == '-' and semana[0][i][j] != 0):
                        # penalidade += 2.0
                        penalidade += 0.15

                    if semana[0][i][j] in compromissosContinuos:
                        if ((j-1 >= 0 and j+1 <= 4 and i-1 >= 0 and i+1 <= self.num_horas_do_dia -1)
                         and (semana[0][i][j-1] != semana[0][i][j] or semana[0][i][j+1] != semana[0][i][j])):
                            # penalidade += 1.0
                            penalidade += 0.10

                    if semana[0][i][j] != 0 and semana[0][i][j] not in compromissosAlocados:
                        compromissosAlocados.append(semana[0][i][j])

            # print 'calc fit'
            # print [c.prioridade for c in self.compromissos if c.id in compromissosAlocados]
            # print [c.id for c in self.compromissos if c.id in compromissosAlocados]
            # print sum([c.prioridade for c in self.compromissos if c.id in compromissosAlocados])

            #  fit = soma das prioridades / pelas penalidades

            a = sum([c.prioridade for c in self.compromissos if c.id in compromissosAlocados])
            h = sum([c.horas for c in self.compromissos if c.id in compromissosAlocados])
            print 'soma das prioridades',a,'soma das horas',h,'penalidade m1:',a * penalidade,'m2:',1+penalidade
            semana[1] = (a+h - (a * penalidade))
            # semana[1] = 1 / (1 + penalidade)



    def run(self):
        cont = 0
        while cont < self.geracoes:
            print "GERACAO     ",cont

            self.fitness()

            self.best.append(max(self.populacao, key = lambda X:X[1]))

            self.crossover()

            self.mutacao()

            cont += 1

        self.fitness()

            # for _ in range(self.geracoes):
            #     self.best = sorted(self.populacao,key = lambda X:X[1])[-1]

        self.print_semana()
        print [c[1] for c in self.best]
        # self.mutacao(self.populacao[0])
        # print self.grade
#  --------------------------------------------------------
