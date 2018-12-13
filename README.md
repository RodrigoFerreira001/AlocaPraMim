# AlocaPraMim
Algoritmo Genético para a Alocação de Tarefas

Requsitos:
-python 2.7
-biblioteca pandas para geração do arquivo csv de saída

Executar:

-> python main.py "arquivo de teste" tamanho da populacao, taxa de mutacao, numero de geracoes

exemplo:

-> python main.py teste.txt 10 0.2 100

o arquivo de teste devera seguir os modelos dos arquivos "teste.txt" e "teste_maior.txt"

o arquvo de teste é composto por:

uma matriz que representa a grade horária em que: 

'0' representa um horario livre 
'-' representao uma restricao

exemplo:
0	-	0	-	0
0	-	0	-	0
0	-	0	-	0
0	-	0	-	0
-	-	-	-	-
-	-	-	-	0
-	-	-	-	0
-	0	-	0	0
-	0	-	0	0
0	0	0	0	0
0	0	0	0	0
0	0	0	0	0
0	0	0	0	0
0	0	0	0	0
0	0	0	0	0

a matriz deve conter 5 colunas representado o intervalo de Segunda a Sexta-feira
o número de linhas corresponde ao numero de horas no dia, cada linha representa 1 hora
caso o numero de linhas seja diferente de 15 o parâmetro 'num_horas_do_dia' na linha 36 do arquivo 'main.py' devera ser alterado



compromissos:
cada linha devera conter um compromisso com id e nomes unicos
os atributos de cada compromisso devem ser separados por ';'. São eles:

id;nome;duracao;prioridade;divisível

send:
id e nome, identificadores do compromisso

duracao, numero de horas que o compromisso durará (mínimo 1 hora)

prioridade, nível de importancia daquele compromisso. Varia de 1 a 3, sendo em 3 máximo

divisível, define se o compromisso deverá ser necessariamente alocado de forma contínua ou não
'/' = pode ser dividido, '-' = deverá ser contínuo

exemplos:

1;tp rv;2;3;/
2;tp bio;4;3;-
3;academia;4;1;/

Os arquivos 'teste.txt' e 'teste_maior.txt' foram os arquivos testado nesta implementação

Saída:

Será gerado um arquivo .CSV em que cada coluna representa uma execução e a última coluna a média das execuções. E cada linha uma geracao. O AG é executado 10 vezes.
O arquivo de saida tera o nome do arquivo de entrada, seguido dos parametros de entrada na orde:
tamanho da população, indice de mutacao, numero de gerações.
Exemplo:

Entrada -> python main.py teste.txt 10 0.2 100
Saida: teste_10_0.2_100.csv







