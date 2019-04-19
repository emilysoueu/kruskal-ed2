#Derivado do algoritmo de inserção
#Faz as trocas a uma certa distância (que diminui a cada passada)
#Primeiro compara elementos separados por "h" posições e os ordena
#Posteriormente vai diminuindo a distância de comparação até zerar h



def shell_sort(A,n):
	h=1
	for h in range (1, len(A), 3*h+1):
		while (h>=1):
			h = int((h-1)/3) #tem q fazer cast pra não dar prob de float
			i=h
			while (i<n):
				aux = A[i]
				j=i
				while (j >= h and aux < A[j-h]):
					A[j] = A[j-h]
					j = j-h
				A[j] = aux
				i = i+1
	h = h/2

arr = [3, 8, 1, 9, 12, 2, 11, 7, 5, 4]
print('Not sorted: %s' % arr)

shell_sort(arr,10)
print('sorted: %s' % arr)