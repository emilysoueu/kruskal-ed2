#@EmilyCosta
#16/04/2017

'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
#========================================================================================================#
#
#
#========================================================================================================#
class InsertionSort(object):
    def ordenar(self, colecao):     
		for i in range(1, len(colecao)):			
			for j in range (i-1,0,-1):
				if (colecao[j]['weight'])> (colecao[i]['weight']): #alteração aqui para o mode de apresentação
					(colecao[j+1]) = (colecao[j])
				else:
					(colecao[j+1]) = (colecao[i])
					break

        return colecao
#========================================================================================================#
#
#
#========================================================================================================#
def selection_sort(A):
	 for i in range (0, len(A) - 1) :
	 	minIndex = i
	 	for j in range (i+1, len(A)) :
	 		if A[j] < A[minIndex]:
	 			minIndex = j
	 		if minIndex != i:
	 			A[i],A[minIndex] = A[minIndex], A[i]
#========================================================================================================#
#
#
#========================================================================================================#
def shellSort(arr, n):
 	h = 1; #our steps for sorting
 	while (h < n/2):
 		h = 2*h+1; #calculate max step needed
 	while (h>=1):
 		for i in range (h,n):
 			temp = arr[i];
 			j = i;
 			while (j >= h and arr[j] < arr[j-h]):
 				arr[j] = arr[j-h];
 				j = j-h;
 			arr[j] = temp;
 		h/= 2;

myL = [3, 1 , 6, 2, 8, 4];

shellSort(myL, 6);
print (myL);
#========================================================================================================#
#
#
#========================================================================================================#
import random

def quicksort(arr, start, end, pivot_mode='random'):
	if start < end:
		split = partition(arr, start, end, pivot_mode)
		quicksort(arr, start, split-1, pivot_mode)
		quicksort(arr, split+1, end, pivot_mode)
	return arr

def partition(arr, start, end, pivot_mode):
	if pivot_mode == 'first':
		pivot = arr[start]
	else:
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

#========================================================================================================#
#
#
#========================================================================================================#
def merge_sort(A):
	merge_sort2(A, 0, len(A)-1)

def merge_sort2(A, first, last):
	if first < last:
		middle = (first+last)//2
		merge_sort2(A, first, middle)
		merge_sort2(A, middle+1, last)
		merge(A, first, middle,last)

def merge(A, first, middle, last):
	L = A[first:middle]
	R = A[middle:last+1]
	L.append(999999999)
	R.append(999999999)
	i = j = 0

	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] =L[i]
			i+= 1
		else:
			A[k] = R[j]
			j += 1

#========================================================================================================#
#
#
#========================================================================================================#
def heapsort(alist):
    build_max_heap(alist)
    for i in range(len(alist) - 1, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        max_heapify(alist, index=0, size=i)
 
def parent(i):
    return (i - 1)//2
 
def left(i):
    return 2*i + 1
 
def right(i):
    return 2*i + 2
 
def build_max_heap(alist):
    length = len(alist)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(alist, index=start, size=length)
        start = start - 1
 
def max_heapify(alist, index, size):
    l = left(index)
    r = right(index)
    if (l < size and alist[l] > alist[index]):
        largest = l
    else:
        largest = index
    if (r < size and alist[r] > alist[largest]):
        largest = r
    if (largest != index):
        alist[largest], alist[index] = alist[index], alist[largest]
        max_heapify(alist, largest, size)
#========================================================================================================#
#
#
#========================================================================================================#

def get_sortkey(n):
    """ Define the method to retrieve the key """
    return n
 
def counting_sort(tlist, k, get_sortkey):
 
    # Create a count list and using the index to map to the integer in tlist.
    count_list = [0]*(k)
 
    # iterate the tgt_list to put into count list
    for n in tlist:
        count_list[get_sortkey(n)] = count_list[get_sortkey(n)] + 1 
 
    # Modify count list such that each index of count list is the combined sum of the previous counts
    # each index indicate the actual position (or sequence) in the output sequence.
    for i in range(k):
        if i ==0:
            count_list[i] = count_list[i]
        else:
            count_list[i] += count_list[i-1]
 
    output = [None]*len(tlist)
    for i in range(len(tlist)-1, -1, -1):
        sortkey = get_sortkey(tlist[i])
        output[count_list[sortkey]-1] = tlist[i]
        count_list[sortkey] -=1
 
    return output
 
			 


