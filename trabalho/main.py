import argparse #abrir o progrmama passando os argumentos via linha de comando

from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":



	parser =argparse.ArgumentParser()
	parser.add_argument("input", type=str, required=True, dest='arq',help="nome do arquivo de leitura")
	parser.add_argument("output", type=str, required=True, dest='save', help="Nome do arquivo de Saída")
	parser.add_argument("algoritmo", dest='insert', action='store_true', help="Algoritmo de ordenacao")
	
	args = parser.parse_args()
	
	#teste
	if args.algoritmo == "insert":
		algoritimoDeOrdenacao = insert_sort()

	if args.arq == "arquivoJson":
		args.arq = './grafos/7vertices.json'

	if args.save == "arquivoDeSaida":
		args.save = './arvores_geradas/insert.txt'
	
	'''
	args.arq = arquivoJson
    arquivoDeSaida = args.save
    '''

	
	

	'''
    arquivoJson = './grafos/7vertices.json'
    arquivoDeSaida = './arvores_geradas/quickbeg.txt'
    '''

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)


    print("funcionou")
