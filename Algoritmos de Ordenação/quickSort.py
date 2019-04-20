# Escolher o pivo
#Separe os elementos menores que o pivo para a esquerda e os elementos maiotrs que o pivo para a direita
# Recursivamente execute o mesmo procedimento para os elementos a esquerda do pivo
# recursivamente execute o mesmo procedimento para os elementos a direita do pivo


#pivo: primeiro
#pivo: último
#pivo: mediana entre primeiro, meio e fim


#Separar o vetor
	#Definir [i] e [j] começando pela esquerda e direita, respectivamente
	#faça uma varreddura com a variável [i] para a direita até que encontre um elementov[i] maior que o pivo
	#faça uma varredira com a variavél [j] para a esquerda até que encontre um elemento v[j] menor que o pivô
	#troque v[i] com v[j]

import random

def quicksort(arr, start, end, pivot_mode='random'):
	if start < end:
		split = partition(arr, start, end, pivot_mode)
		quicksort(arr, start, split-1, pivot_mode)
		quicksort(arr, split+1, end, pivot_mode)
	return arr

def partition(arr, start, end, pivot_mode):
	if pivot_mode == 'first': #Pivo Inicio
		pivot = arr[start]
	elif pivot_mode == 'end':#Pivo fim
		pivot = arr[end]
	elif pivot_mode == 'median' #Pivo mediana entre inicio, central e fim
		half = int((start+end)/2)
		s = A[star]
		half = A[half]
		e = A[end]
	else: #pivo aleatório
		pivot_index = random.randrange(start,end)
		pivot = arr[pivot_index]
		arr[pivot_index], arr[start] = arr[start], arr[pivot_index] # place the pivot at the beginning
	i = start + 1

	for j in range(start+1,end+1):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[start], arr[i-1] = arr[i-1], arr[start]
	return i-1

#------------------------------------------------------------
'''
def quick_sort(A, L, R):
	if (L < R):
		j = separar(A,L,R)
		quicksort(A,L,j-1)
		quicksort(A,j+1,R)

def separar(A,L,R):
	i = L+1
	j = R
	pivo = A[L]

	while(i<=j):
		if A[i] <= pivo #acha em [i] a primeira posição maior que o pivo
			i++
		elif A[j] >pivo: #acha em [j] a primeira posição menor que o pivo		
			j--
		elif i<=j : #efetuar a troca
			trocar(A,i,j)
			i++
			j--

	trocar(A,L,j)
	return j

def trocar(V,i,j):
	aux = V[i]
	V[i]= V[j]
	V[j]= aux
'''
#--------------------------------------------------------------



