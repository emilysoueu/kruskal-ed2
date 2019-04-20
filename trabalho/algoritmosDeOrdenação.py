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


import random

#======================================================================================#
#   							I N S E R T I O N
#======================================================================================#

class insertion_sort(object):
	def ordenar(self, colecao):
		for i in range(1, len(colecao)): # [i] percorrer da pos 1 até a última pos de colecao
			'''print('Vetor ',i,': %s' %colecao) #teste 0'''
			curNum = colecao[i] #coleção
			'''print('curNum = ',curNum) #teste 1'''
			for j in range (i-1,-1,-1):# [j] percorre da primeira pos
				'''print('[J] = ', j)'''
				if colecao[j]['weight']>curNum['weight']: # procura para frente até encontrar alguém menor que o atual num
					temp = colecao[j+1]
					colecao[j+1] =colecao[j]				
					colecao[j] = temp
					'''
					print(colecao[j],' >= ',curNum, '= true')  #teste 2
					print('temp = ',temp)
					'''
				else:
					colecao[j+1] = curNum
					break
		return colecao
#======================================================================================#
#   					 		S E L E C T I O N
#======================================================================================#


class selection_sort(object):
	def ordenar(self,colecao):
		for i in range (0, len(colecao) - 1) :
		 	minIndex = i
		 	for j in range (i+1, len(colecao)):
		 		if colecao[j]['weight'] < colecao[minIndex]['weight']:
		 			minIndex = j
		 		if minIndex != i:
		 			colecao[i],colecao[minIndex] = colecao[minIndex], colecao[i]
		return colecao
#======================================================================================#
#   							 S H E L L S O R T
#======================================================================================#


class shell_sort(object):
	def ordenar(self,colecao):
		h=1
		for h in range (1, int(len(colecao)), 3*h+1):
			while (h>=1):
				h = int((h-1)/3) #fazer cast não dar prob de float
				i=h
				while (i<len(colecao)):
					aux = colecao[i]
					j=i
					while (j >= h and int(aux['weight']) < int(colecao[j-h]['weight'])):
						colecao[j] = colecao[j-h]
						j = j-h
					colecao[j] = aux
					i = i+1
		h = h/2
		return colecao

#======================================================================================#
#   							H E A P S O R T
#======================================================================================#

class heapsort(object):

	def ordenar(self,colecao):
		def build_max_heap(colecao):

			for i in range(len(colecao) - 1, 0, -1):
				colecao[0], colecao[i] = colecao[i], colecao[0]
				self.max_heapify(colecao, index=0, size=i)

			return colecao
	
	def parent(i):
		return (i - 1)//2
	
	def left(i):
		return 2*i + 1
	
	def right(i):
		return 2*i + 2
	
	def build_max_heap(colecao):
		length = len(colecao)
		start = parent(length - 1)
		while start >= 0:
			max_heapify(colecao, index=start, size=length)
			start = start - 1
	
	def max_heapify(colecao, index, size):
		l = left(index)
		r = right(index)
		if (l < size and colecao[l]['weight'] > colecao[index]['weight']):
			largest = l
		else:
			largest = index
		if (r < size and colecao[r]['weight'] > colecao[largest]['weight']):
			largest = r
		if (largest != index):
			colecao[largest], colecao[index] = colecao[index], colecao[largest]
			max_heapify(colecao, largest, size)

#======================================================================================#
#   							C O U N T S O R T
#======================================================================================#


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


#======================================================================================#
#   							M E R G E S O R T
#======================================================================================#
class merge_sort(object):
	def ordenar(self, colecao):
		merge_sort2(colecao, 0, len(colecao)-1)

	def merge_sort2(colecao, first, last):
		if first < last:
			middle = (first+last)//2
			merge_sort2(colecao, first, middle)
			merge_sort2(colecao, middle+1, last)
			merge(colecao, first, middle,last)

	def merge(colecao, first, middle, last):
		L = colecao[first:middle]
		R = colecao[middle:last+1]
		L.append(999999999)
		R.append(999999999)
		i = j = 0

		for k in range (first, last+1):
			if L[i] <= R[j]:
				colecao[k] =L[i]
				i+= 1
			else:
				colecao[k] = R[j]
				j += 1


#======================================================================================#
#   							Q U I C K S O R T
#======================================================================================#

class  quicksort(object):
	def ordenar(self,arr, start, end, pivot_mode='random'):
		if start < end:
			split = self.partition(arr, start, end, pivot_mode)
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