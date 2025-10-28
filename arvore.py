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
    
        self.novo = None
        
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
        
        novo_no = self.novo_no(valor_para_inserir, altura=1)
        
        caminho = []

        #iniciar um ponteiro atual na raiz  e adicionar o nó atual à lista caminho
        no_atual = self.raiz

        while True:
            no_atual == caminho.append(no_atual)
            valor_para_inserir = no_atual.valor
            
            if no_atual.valor.esquerda is None:
                novo_no == no_atual.esquerda
                break
            elif no_atual.valor.esquerda is not None:
                no_atual == no_atual.esquerda
            
            elif no_atual.valor.direita is None:
                novo_no == no_atual.direita
                break
            elif no_atual.valor.direita is not None:
                no_atual == no_atual.direita
                
            else: 
                break
            
            for no_ancestral in reversed(caminho):
                no_ancestral.atualizar_altura()
                
                fator_balanceamento = Node.obter_balanceamento(no_ancestral)
                if fator_balanceamento > 1:
                    print(f"Desbalanceamento no node {no_ancestral.valor} (FB: {fator_balanceamento})")
                    esquerda_ancestral = no_ancestral.esquerda
                    if valor_para_inserir < esquerda_ancestral.valor:
                        print(f"Rotação simples à direita")
                        nova_sub_raiz = Arvore.rotacao_direita(no_ancestral)
                    else:
                        Arvore.rotacao_esquerda(esquerda_ancestral)
                        nova_sub_raiz = Arvore.rotacao_direita(no_ancestral)
                    self._atualizar_referencia_pai(caminho, no_ancestral, nova_sub_raiz)
                
                elif fator_balanceamento < -1:
                    ancestral_direita = no_ancestral.direita
                    if valor_para_inserir > ancestral_direita.valor:
                        print(f"Rotação simples à esquerda")
                        nova_sub_raiz = Arvore.rotacao_esquerda(no_ancestral)
                    else: 
                        Arvore.rotacao_direita(ancestral_direita)
                        nova_sub_raiz = Arvore.rotacao_esquerda(no_ancestral)
                    self._atualizar_referencia_pai(caminho, no_ancestral, nova_sub_raiz)
                                    

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

# Rotação Direita

    def rotacao_direita(self, Z):
        Y = Z.esquerda
        if Y is none:
            # Se não é possível rotacionar
            return Z

        T3 = Y.direita

        Y.direita = Z
        Z.esquerda = T3

        # self.atualizar_altura(Z)
        # self.atualizar_altura(Y)

        return Y

    # Rotação Esquerda

    def rotacao_esquerda(self, Z):
        Y = Z.direita
        if Y is None:
            #Se não é possível rotacionar
            return Z

        T2 = Y.esquerda

        Y.esquerda = Z
        Z.direita = T2

        # self.atualizar_altura(Z)
        # self.atualizar_altura(Y)

        return Y
    
    def imprimir_arvore(self, no=None, prefixo="", is_ultimo=True):
        if no is None:
            no = self.raiz
        
        if no is not None:
            print(prefixo + ("└── " if is_ultimo else "├── ") + f"{no.valor} (h:{no.altura}, fb:{Node.obter_fator_balanceamento(no)})")
            
            # Preparar prefixo para os filhos
            novo_prefixo = prefixo + ("    " if is_ultimo else "│   ")
            
            # Verificar se tem filhos
            tem_esquerda = no.esquerda is not None
            tem_direita = no.direita is not None
            
            # Imprimir filho da esquerda primeiro
            if tem_esquerda:
                self.imprimir_arvore(no.esquerda, novo_prefixo, not tem_direita)
            
            # Imprimir filho da direita
            if tem_direita:
                self.imprimir_arvore(no.direita, novo_prefixo, True)
    
   
if __name__ == "__main__":
    print("=" * 60)
    print(f"Passo D: ")
    print("=" * 60)
    
    print("\nTESTE 1: caso especial")
    print("\n" + "="*60)
    arvore_teste = Arvore()
    for valor in [1, 2 , 3]:
        print(f"Inserir:")
        arvore_teste.inserir(valor)
    
    print(f"Resultado:")
    arvore_teste.imprimir_arvore()
    
    print("\n" + "="*60)
    print("\nTESTE 2: rotação da sub-arvore")
    print("\n" + "="*60)
    print("Inserindo sequência: [10, 5, 15, 2, 7, 1]")
    arvore_teste2 = Arvore()
    for valor in [10, 5, 15, 2, 7, 1]:
        print(f"Inserir:")
        arvore_teste2.inserir(valor)
        
    print("\nResultado:")
    arvore_teste2.imprimir_arvore()
    
    print("\n" + "="*60)
    print("\nTESTE 3: Rotação dupla (LR)")
    print("Inserindo sequência que força rotação dupla: [10, 5, 7]")
    arvore3 = Arvore()
    for valor in [10, 5, 7]:
        print(f"\nInserindo {valor}:")
        arvore3.inserir(valor)
        
    print("\nResultado")
    arvore3.imprimir_arvore()

    print("\n" + "="*60)
    print("Passo D finalizado")
    print("="*60)
    
    
