import random
import time

lista = [10, 5, 15, 3, 1, 20, 25, 18]


class Node:
    # método construtor
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        # Raiz não existe!
        if self.raiz is None:
            self.raiz = Node(valor)
            # print(f"Criar a raiz com valor {valor}")
            return

        # Se existir uma raiz, o nó atual recebe o valor da raiz
        no_atual = self.raiz

        while True:
            # Se valor for menor que atual, olha para a esquerda do no_atual
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = Node(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            # Se valor for maior que atual, olha para a direita do no_atual
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)
                    break
                else:
                    no_atual = no_atual.direita

            # Se o valor é igual ao atual
            else:
                # ignorar
                break

    def buscar(self, valor):
        no_atual = self.raiz

        # Se não existe raiz
        if no_atual is None:
            return False

        while no_atual is not None:
            # Existe o valor na árvore
            if valor == no_atual.valor:
                return True
            # Valor é menor
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            # Valor é maior
            else:
                no_atual = no_atual.direita
        # Valor não existe na árvore
        return False
    
    def obter_altura(self, node):
        if node is None:
            return 0
        else: 
            return node.altura
        
    def atualizar_altura(self, node):
        altura_esquerda = obter_altura(node.esquerda)
        altura_direita = obter_altura(node.direita)
        node.altura = 1 + max(altura_esquerda, altura_direita)
        
    def obter_balanceamento(self, node):
        if node is None:
            return 0
        
        resultado = obter_altura(node.esquerda) - obter_altura(node.direita)
        
        if resultado > 1:
            return resultado
        elif resultado < -1:
            return resultado
        else: 
            return resultado
    
