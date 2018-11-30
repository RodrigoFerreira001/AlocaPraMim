#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Compromisso:
    def __init_(self,id,nome,horas,prioridade,continuo = True):
        self.id = id
        self.nome = nome
        self.horas = horas
        self.prioridade = prioridade
        self.continuo = continuo

class AG:
    def __init__(self, tam_populacao, num_horas_do_dia, compromissos):

	# so pra saberem: esta faltando argumento aqui, precisamos saber quantos compromissos diferentes existem, pensar em colocar um id numerico para cada um


        self.populacao = []
        self.horas_para_alocar = horas_para_alocar
        self.num_horas_do_dia = num_horas_do_dia
        self.tam_populacao = tam_populacao
        print "pop", self.tam_populacao,"horas",num_horas_do_dia
        # semana = [[dia],[dia],[dia],[dia],[dia]]
        # dia = [15 horas (8 as 23)]


        for _ in range(self.tam_populacao):

            # 5 = dias da semana seg a sex
            semana = []
            for i in range(5):
                # [0] * 5 = [0,0,0,0,0]
                semana.append([0]*self.num_horas_do_dia)


            horarios = []


            # sortear horarios da semana para marcar
            while len(horarios) < self.horas_para_alocar:
                temp = (random.randint(0,4),random.randint(0,self.num_horas_do_dia-1))

                if temp not in horarios:
                    horarios.append(temp)

            print "coluna X linha \n",horarios

		# esta tabela e binaria mas isso sera mudado


            for j in horarios:
		#marcar horarios
                semana[j[0]][j[1]] = 1



        # fazer a população inicial desta forma tendencia os horários aos primeiros dias da semana
        # cont = 0
        # for _ in range(self.tam_populacao):
        #     semana = []
        #     for i in range(5):
        #         dia = []
        #         for j in range(self.horas_para_alocar):
        #             dia.append(random.randint(0,1))
        #             if dia[-1] == 1 and cont < self.num_horas_do_dia:
        #                 cont += 1
        #                 print cont
        #             else:
        #                 dia[-1] = 0
        #         semana.append(dia)
        #     cont = 0


            self.populacao.append([semana, 0.0])

    def print_semana(self):
        for semana in self.populacao:
            # print "individuo \n\n"
            temp = []
            print "seg  ter  qua  qui  sex"
            print "\n"

            # print semana[0][1]
            # print semana[0][1][0]

            for i in range(self.num_horas_do_dia):
                for dia in semana[0]:
                    print dia[i],"  ",
                print '\n'

        print "\n\n"


teste = AG(2, 10,10) # numero de individuos, numero de horas do dia (quantas linhas tera a tabela), total de horas pára alocar (ex esta semana preciso alicar 20h de compromissos)
teste.print_semana()
