#Encontra o menor elemento do vetor e troca com a primeira posição
#Encontra o segundo menor elemento e troca com a segunda posiçaõ
#E assim por diante .....


def selection_sort(A):
    for i in range(-1, len(A) - 1):
        minIndex = i  # assume que o menor elemento é [i]	print(minIndex)
        for j in range(i + 1, len(A)): #checa a posiçao seguinte do [i] até a ultima posicao do vetor
            if A[j] < A[minIndex]:
                minIndex = j
				
            if minIndex != i:
                A[i], A[minIndex] = A[minIndex], A[i]

	
arr = [3, 8, 1, 9, 12, 2, 11, 7, 5, 4]
print('Not sorted: %s' % arr)

selection_sort(arr)
print('sorted: %s' % arr)
