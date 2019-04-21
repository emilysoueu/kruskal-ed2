def merge_sort(A):
	if int(len(A)) >1:
		meio = int(len(A)/2) #armazena o tamanho da metade do vetor
		esquerda = A[:meio] # primeira metade
		direita = A[meio:] # segunda metade

		#chama a função recursivamente pra ambos os lados
		merge_sort(esquerda) 
		merge_sort(direita)

		i,j,k = 0,0,0 

		while i < int(len(esquerda)) and j< int(len(direita)):
			if esquerda[i] < direita[j]:
				A[k]=esquerda[i]
				i+=1
			else:
				A[k]=direita[j]
				j+=1
			k+=1

		while i<len(esquerda):
			A[k] = esquerda[i]
			i+=1
			k+=1

		while j<len(direita):
			A[k] = direita[j]
			j+=1
			k+=1


arr = [3,8,1,9,12,2,11,7,5,4]
print('Not sorted: %s' %arr)


merge_sort(arr)
print('sorted: %s' %arr) 
			 


