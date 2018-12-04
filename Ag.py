#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class AG:
    def __init__(self, tam_populacao, num_horas_do_dia, compromissos, grade):


        print "recebi: "

        horasParaAlocar = sum([c.horas for c in compromissos])

        horasDisponiveis = sum([1 for i in grade for j in i if j=='0'])

        print [c.nome for c in compromissos],"alocar",horasParaAlocar,horasDisponiveis

        # grade transposta para que linhas = horas colunas = dias
        self.grade = map(list, zip(*grade))
        self.populacao = []
        self.num_horas_do_dia = num_horas_do_dia
        self.tam_populacao = tam_populacao
        self.geracoes = 50
        self.best = [0,0.0]

        # semana = [[dia],[dia],[dia],[dia],[dia]]
        # dia = [15 horas (8 as 23)], depende de num_horas_do_dia considerado

        # tratar caso existam mais horas para alocar do que horas na semana
        h = 0
        compromissoAlocados = []
        if horasParaAlocar < horasDisponiveis :
            compromissoAlocados = compromissos[:]

        else:
            temp = sorted(compromissos,key = lambda X:X.prioridade, reverse = True)

            while h < horasDisponiveis:

                c = temp.pop(0)

                h += c.horas
                compromissoAlocados.append(c)

            print h
            compromissoAlocados = compromissoAlocados[:-1]
            print [c.id for c in compromissoAlocados]


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

        self.compromissos = compromissoAlocados
        self.populacao = temp[:]

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

    def crossover(self):
        f1 = []
        f2 = []
        # Inicializar filhos
        # 5 = dias da semana seg a sex
        semana = []
        for i in range(5):
            # [0] * 5 = [0,0,0,0,0]
            f1.append([0]*self.num_horas_do_dia)
            f2.append([0]*self.num_horas_do_dia)

        pai1, pai2 = random.sample(self.populacao, 2)
        temp = [c.id for c in self.compromissos]


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

        # escrevedo segunda metade dos compromissos
        for i,dia in enumerate(pai1[0]):
            for j,hora in enumerate(dia):
                # print i,j , pai1[0][i][j] , pai1[0][i]
                if pai1[0][i][j] in temp[len(temp)/2:]:
                    if f2[i][j] == 0:
                        f2[i][j] = pai1[0][i][j]
                    else:
                        # procurando proximo intervalo vazio
                        for k in range(i,len(f2)):
                            for l in range(j,len(f2[0])):
                                if f2[k][l] == 0:
                                    f2[k][l] = pai1[0][i][j]

        for i,dia in enumerate(pai2[0]):
            for j,hora in enumerate(dia):
                # print i,j , pai2[0][i][j] , pai2[0][i]
                if pai2[0][i][j] in temp[len(temp)/2:]:
                    if f1[i][j] == 0:
                        f1[i][j] = pai2[0][i][j]
                    else:
                        # procurando proximo intervalo vazio
                        for k in range(i,len(f1)):
                            for l in range(j,len(f1[0])):
                                if f1[k][l] == 0:
                                    f1[k][l] = pai2[0][i][j]

        # print "CRUZAMENTO: "
        # print "pai1",pai1,"\n\n"
        # print "pai2",pai2,"\n\n"
        # print "f1",f1,"\n\n"
        # print "f2",f2,"\n\n"


        print "crossover OK"
        return [f1,0.0],[f2,0.0]

        # print '--'*20,temp[:len(temp)/2],temp[len(temp)/2:]
        # print pai1,"\n\n",pai2,"\n\n", f2


    def mutacao(self,semana):
        # print "MUTACAO \n\n"
        # print semana

        comp = self.compromissos[:]
        # comp = [c for c in self.compromissos]
        compromissoMutado = comp[random.randint(0, len(comp)-1)]

        # print "compromisso mutado:",compromissoMutado.id,compromissoMutado.nome,compromissoMutado.horas

        novoHorario = []
        while len(novoHorario) < compromissoMutado.horas:
            temp = (random.randint(0,4),random.randint(0,self.num_horas_do_dia-1))

            if temp not in novoHorario and semana[0][temp[0]][temp[1]] == 0:
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
        return semana


    def fitness(self):
        # fit = 1/ penalidades

        compromissosContinuos = [c.id for c in self.compromissos if c.continuo == True]

        # contando penalidades

        for semana in self.populacao:
            # print semana
            penalidade = 0

            for i,dia in enumerate(semana[0]):
                for j,hora in enumerate(dia):
                    # print i,j,self.grade[i][j],semana[0][i][j],len(self.grade)
                    if self.grade[i][j] == '-' and semana[0][i][j] != 0:
                        penalidade += 0.20

                    if semana[0][i][j] in compromissosContinuos:
                        if semana[0][i][j-1] != semana[0][i][j] or semana[0][i][j+1] != semana[0][i][j]:
                            penalidade += 0.10

            semana[1] = 1/ penalidade

    def run(self):

        self.fitness()
        # for _ in range(self.geracoes):
        #     self.best = sorted(self.populacao,key = lambda X:X[1])[-1]


        self.print_semana()
        # self.crossover()
        # self.mutacao(self.populacao[0])
        # print self.grade
#  --------------------------------------------------------

# teste = AG(2, 10,10) # numero de individuos, numero de horas do dia (quantas linhas tera a tabela), total de horas pára alocar (ex esta semana preciso alicar 20h de compromissos)
# teste.print_semana()
