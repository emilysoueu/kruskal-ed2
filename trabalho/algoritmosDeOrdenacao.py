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


import random, math


#======================================================================================#
#   							Q U I C K S O R T
#======================================================================================#

#(pivo mediana)
class quick_sort_mid(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self, colecao):
        self.sort(self,colecao, 0, len(colecao) - 1)

        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.comparacao +=1
            p = self.partition(self,colecao, left, right)
            self.atribuicao +=1
            self.sort(self,colecao, left, p-1)
            self.sort(self,colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        mid = (right + left) // 2
        pivot = right
        self.atribuicao +=2
        
        if int(colecao[left]['weight']) < int(colecao[mid]['weight']):
            self.comparacao +=1
            if int(colecao[mid]['weight']) < int(colecao[right]['weight']):
                self.comparacao +=1
                pivot = mid
                self.atribuicao +=1
        elif int(colecao[left]['weight']) < int(colecao[right]['weight']):
            self.comparacao +=1
            pivot = left
            self.atribuicao +=1
        return pivot


    def partition(self, colecao, left, right):
        pindex = self.get_pivot(self,colecao, left, right)
        pvalue = colecao[pindex]
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex]
        aux = left
        self.atribuicao +=5

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.comparacao +=1
                aux += 1
                self.atribuicao +=1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
                self.atribuicao +=2
        colecao[left], colecao[aux] = colecao[aux], colecao[left]
        self.atribuicao +=2

        return (aux)

#(pivo inicio)
class quick_sort_beg(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self, colecao):
        self.sort(self,colecao, 0, len(colecao) - 1)

        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.comparacao +=1
            p = self.partition(self,colecao, left, right)
            self.atribuicao +=1

            self.sort(self,colecao, left, p-1)
            self.sort(self,colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = right
        self.atribuicao +=1
        return pivot


    def partition(self, colecao, left, right):
        pindex = self.get_pivot(self,colecao, left, right)
        pvalue = colecao[pindex]
        colecao[pindex], colecao[left] = colecao[left], colecao[pindex]
        aux = left

        self.atribuicao +=5

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.comparacao +=1
                aux += 1                
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
                self.atribuicao +=3

        colecao[left], colecao[aux] = colecao[aux], colecao[left]
        self.atribuicao +=2

        return (aux)

#(pivo fim)
class quick_sort_end(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self, colecao):
        self.sort(self,colecao, 0, len(colecao) - 1)

        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao

    def sort(self, colecao, left, right):
        if left<right:
            self.comparacao +=1
            p = self.partition(self,colecao, left, right)
            self.atribuicao +=1
            self.sort(self,colecao, left, p-1)
            self.sort(self,colecao, p + 1, right)

        
    def get_pivot(self, colecao, left, right):
        pivot = left     
        self.atribuicao +=1
        return pivot


    def partition(self, colecao, left, right):
        pindex = self.get_pivot(self,colecao, left, right)
        pvalue = colecao[pindex]
        aux = left
        self.atribuicao +=3

        for i in range(left, right + 1):
            if int(colecao[i]['weight']) < int(pvalue['weight']):
                self.comparacao +=1
                aux += 1
                colecao[i], colecao[aux] = colecao[aux], colecao[i]
                self.atribuicao +=3
        colecao[left], colecao[aux] = colecao[aux], colecao[left]
        self.atribuicao +=2

        return (aux)

#======================================================================================#
#   							I N S E R T I O N
#======================================================================================#


class insert_sort(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self, colecao):
        for i in range(1, len(colecao)): # [i] percorrer da pos 1 até a última pos de colecao
            '''print('Vetor ',i,': %s' %colecao) #teste 0'''
            curNum = colecao[i] #coleção
            self.atribuicao += 1 # ou conta duas atribuições (for e cur)
            '''print('curNum = ',curNum) #teste 1'''
            for j in range (i-1,-1,-1):# [j] percorre da primeira pos            
                
                '''print('[J] = ', j)'''
                if colecao[j]['weight']>curNum['weight']: # procura para frente até encontrar alguém menor que o atual num
                    self.comparacao += 1
                    temp = colecao[j+1]
                    colecao[j+1] =colecao[j]
                    colecao[j] = temp
                    self.atribuicao +=3
                    '''
					print(colecao[j],' >= ',curNum, '= true')  #teste 2
					print('temp = ',temp)
					'''
                else:
                    colecao[j+1] = curNum
                    self.comparacao += 1
                    break
        print("Comparacoes:", self.comparacao)
        print("Atribuicoes:", self.atribuicao)
        return colecao
#======================================================================================#
#   					 		S E L E C T I O N
#======================================================================================#


class select_sort(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self,colecao):
        for i in range (0, len(colecao) - 1) :
            minIndex = i
            self.atribuicao +=2
            for j in range (i+1, len(colecao)):
                self.atribuicao +=1
                if colecao[j]['weight'] < colecao[minIndex]['weight']:
                    self.comparacao +=1
                    minIndex = j
                    self.atribuicao +=1
                if minIndex != i:
                    colecao[i],colecao[minIndex] = colecao[minIndex], colecao[i]
                    self.atribuicao +=1
        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao
#======================================================================================#
#   							 S H E L L S O R T
#======================================================================================#


class shell_sort(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self,colecao):
        h=1
        self.atribuicao +=1
        for h in range (1, int(len(colecao)), 3*h+1):
            while (h>=1):
                h = int((h-1)/3) #fazer cast não dar prob de float
                i=h
                self.atribuicao +=2
                while (i<len(colecao)):
                    self.comparacao +=1
                    aux = colecao[i]
                    j=i
                    self.atribuicao +=2
                    while (j >= h and int(aux['weight']) < int(colecao[j-h]['weight'])):
                        self.comparacao +=1
                        colecao[j] = colecao[j-h]
                        j = j-h
                        self.atribuicao +=2
                    colecao[j] = aux
                    i = i+1
                    self.atribuicao +=2
        h = h/2
        self.atribuicao +=1


        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao

#======================================================================================#
#   							H E A P S O R T
#======================================================================================#

class heap_sort(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self,colecao):
        def buil_max_heap(colecao):
            for i in range (len(colecao)-1,0,-1):
                colecao[0], colecao[i] = colecao[i], colecao[0]
                self.atribuicao +=2
                self.max_heapify(colecao,index=0,size=1)

        print("Comparacoes: ",self.comparacao)
        print("Atribuicoes: ",self.atribuicao)
        return colecao

    def parent(i):
        return (i-1)//2

    def low(i):
        return 2*1+1

    def hi(i):
        return 2*i+2

    def buil_max_heap(colecao):
        length = len(colecao)
        start = parent(length-1)
        self.atribuicao +=2


        while start >= 0:
            self.comparacao +=1
            max_heapify(colecao,index= start, size = length)
            start = start -1
            self.atribuicao +=1

    def max_heapify(colecao, index, size):
        l = low(index)
        r = hi(index)
        self.atribuicao +=2

        if (l<size and colecao[l]['weight'] >colecao[index]['weight']):
            self.comparacao +=1
            largest = l 
            self.atribuicao += 1
        else:
            largest = index
            self.atribuicao +=1

        if (r < size and colecao[r]['weight'] >colecao[largest]['weight']):
            self.comparacao +=1
            largest = r 
            self.atribuicao +=1
        if (largest != index):
            colecao[largest], colecao[index] = colecao[index], colecao[largest]
            self.atribuicao +=2
            max_heapify(colecao, largest, size)

#======================================================================================#
#   							C O U N T S O R T
#======================================================================================#
class count_sort(object):
    comparacao = 0
    atribuicao = 0  
    def ordenar(self,colecao):

        tamanho = int(len(colecao))
        maior = int(colecao[0]['weight'])
        menor = int(colecao[0]['weight'])
        self.atribuicao +=3

        for k in colecao:
            if int(k['weight']) > maior:
                self.comparacao += 1
                maior = int(k['weight'])
                self.atribuicao +=1
                if int(k['weight']) < menor:
                    self.comparacao += 1
                    menor = int(k['weight'])
                    self.atribuicao +=1

        media = maior - menor +1
        A = [0]*media
        saida =[0]* tamanho
        self.atribuicao +=3
		

		# passo 1 ----> contagem do número de cada elemento do intervalo
        for i in range(0,tamanho):
            A[int(colecao[i]['weight'])-menor]+=1;
            self.atribuicao +=1

		#passo 2 -----> Agora será feito o complemento de casas de cada valor
        for i in range (1,int(len(A))):
            A[i] += A[i-1]
            self.atribuicao +=1

		#passo 3 -------->  alocação dos valores no vetor ordenado.
        for i in range(tamanho-1,-1,-1):
            saida [A[int(colecao[i]['weight'])-menor]-1] = colecao[i]
            self.atribuicao +=1			
            A[int(colecao[i]['weight']) - menor]-= 1
            self.atribuicao +=1
 
		#passo 4  --------> passar o conteúdo do vetor final para o vetor original.
        for i in range(0,tamanho):
            colecao[i] = saida[i]
            self.atribuicao +=1
        
        print("Comparacoes: ", self.comparacao)
        print("Atribuicoes: ", self.atribuicao)
        return colecao



#======================================================================================#
#   							M E R G E S O R T
#======================================================================================#

class merge_sort(object):
    comparacao = 0
    atribuicao = 0
    def ordenar(self, colecao):
        if len(colecao) > 1:
            self.comparacao +=1
            meio = int(len(colecao)/2)
            esquerda = colecao[:meio]
            direita = colecao[meio:]
            self.atribuicao +=3

            self.ordenar(self, esquerda)
            self.ordenar(self, direita)

            i = j = k = 0
            self.atribuicao +=3

            while i < len(esquerda) and j < len(direita):
                self.comparacao +=1
                if int(esquerda[i]['weight']) < int(direita[j]['weight']):
                    self.comparacao +=1
                    colecao[k] = esquerda[i]
                    i+=1
                    self.atribuicao +=2
                else:
                    colecao[k] = direita[j]
                    j+=1
                    self.atribuicao +=2
                k+=1
                self.atribuicao +=1

            while i < len(esquerda):
                self.comparacao +=1
                colecao[k] = esquerda[i]
                i+=1
                k+=1
                self.atribuicao +=3
            while j < len(direita):
                self.comparacao +=1
                colecao[k] = direita[j]
                j+=1
                k+=1
                self.atribuicao +=3

            print("Comparacoes: ", self.comparacao)
            print("Atribuicoes: ", self.atribuicao)
            return colecao



	