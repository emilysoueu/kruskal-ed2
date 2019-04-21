#Ordenar da direita pra esquerda até que todos os números esteja em suas posições corretas

def insertion_sort(A):
	for i in range(1, len(A)): # [i] percorrer da pos 1 até a última pos de A
		print('Vetor ',i,': %s' %A) #teste 0
		curNum = A[i]
		print('curNum = ',curNum) #teste 1
		for j in range (i-1,-1,-1):# [j] percorre da primeira pos
			print('[J] = ', j)
			if A[j]>curNum: # procura para frente até encontrar alguém menor que o atual num
				temp = A[j+1]
				A[j+1] =A[j]				
				A[j] = temp
				print(A[j],' >= ',curNum, '= true')  #teste 2
				print('temp = ',temp)
			else:
				A[j+1] = curNum
				break

arr = [3,8,1,9,12,2,11,7,5,4]
print('Not sorted: %s' %arr)


insertion_sort(arr)
print('sorted: %s' %arr) 