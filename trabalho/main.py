#!/usr/bin/env python3

import argparse #abrir o progrmama passando os argumentos via linha de comando
import time

from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input", type=str, help="Nome do arquivo de Entrada")
	parser.add_argument("output", type=str, help="Nome do arquivo de Saída")
	parser.add_argument("algoritmo", type=str, help="Algoritmo de ordenacao")

	args = parser.parse_args()

	algoritmos = {
		'insert_sort': insert_sort,
		'select_sort': select_sort,
		'shell_sort': shell_sort,
		'heap_sort': heap_sort,
		'count_sort': count_sort,
		'merge_sort': merge_sort,
		'quick_sort_end': quick_sort_end,
		'quick_sort_beg':quick_sort_beg,
		'quick_sort_mid': quick_sort_mid
	}
	start = time.time()

	grafo = Grafo()
	grafo.estabelecerAlgoritmoDeOrdenacao(algoritmos[args.algoritmo])
	grafo.carregarGrafo(args.input)

	arvoreGeradoraMinima =  grafo.executarKruskal() 
	SalvarArvoreGeradoraMinimaEmArquivo(args.output, arvoreGeradoraMinima)
	stop = time.time()

	print("Tempo de execucao: ",stop-start)

	#'./arvores_geradas/insert.txt'