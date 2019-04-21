import random #biblioteca de valores aleatórios

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
