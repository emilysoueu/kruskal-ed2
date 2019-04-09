import random #biblioteca de valores aleatórios

''' #muitos bugs
def bubble_sort(v): #recebe um vetor como parâmetro
	fim = len(v) -1 # saber quantos elementos tem no vetor

	while fim>0:
		i = 0
		#percorrendo o vetor de 0 (valor inicial) até o fim
		while i<fim:
			if v[i] > v[i+1]:
				#realizando a troca dos valores
				temp = v[i]
				v[i] = v[i+1]
				v[i+1] = temp
		fim -= 1
'''

def bubble_sort(vetor):
     elementos = len(vetor)-1 #importante para não checar fora do vetor
     ordenado = False
     while not ordenado:
         ordenado = True
         for i in range(elementos):
             if vetor[i] > vetor[i+1]:
                 vetor[i], vetor[i+1] = vetor[i+1],vetor[i]
                 ordenado = False   


vetor = list(range(0,10))
random.shuffle(vetor)
#print (vetor)


bubble_sort(vetor)
print(vetor)
