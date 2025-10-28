import random
import time

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

    def obter_altura(self, node):
        if node is None:
            return 0
        return node.altura

    def atualizar_altura(self):
        altura_esq = self.obter_altura(self.esquerda)
        altura_dir = self.obter_altura(self.direita)
        self.altura = 1 + max(altura_esq, altura_dir)

    def obter_balanceamento(self):
        return self.obter_altura(self.esquerda) - self.obter_altura(self.direita)


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, node, valor):
        if node is None:
            return Node(valor)

        # Inserção normal de árvore binária
        if valor < node.valor:
            node.esquerda = self._inserir_rec(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._inserir_rec(node.direita, valor)
        else:
            return node  # evita duplicata

        # Atualiza altura
        node.atualizar_altura()

        # Calcula balanceamento
        fb = node.obter_balanceamento()

        # Rotação simples à direita
        if fb > 1 and valor < node.esquerda.valor:
            return self.rotacao_direita(node)

        # Rotação simples à esquerda
        if fb < -1 and valor > node.direita.valor:
            return self.rotacao_esquerda(node)

        # Rotação dupla esquerda-direita
        if fb > 1 and valor > node.esquerda.valor:
            node.esquerda = self.rotacao_esquerda(node.esquerda)
            return self.rotacao_direita(node)

        # Rotação dupla direita-esquerda
        if fb < -1 and valor < node.direita.valor:
            node.direita = self.rotacao_direita(node.direita)
            return self.rotacao_esquerda(node)

        return node

    def rotacao_direita(self, z):
        y = z.esquerda
        t3 = y.direita

        y.direita = z
        z.esquerda = t3

        z.atualizar_altura()
        y.atualizar_altura()

        return y

    def rotacao_esquerda(self, z):
        y = z.direita
        t2 = y.esquerda

        y.esquerda = z
        z.direita = t2

        z.atualizar_altura()
        y.atualizar_altura()

        return y

    def imprimir_arvore(self, no=None, prefixo="", is_ultimo=True):
        if no is None:
            no = self.raiz

        if no is not None:
            print(prefixo + ("└── " if is_ultimo else "├── ") +
                  f"{no.valor} (h:{no.altura}, fb:{no.obter_balanceamento()})")

            novo_prefixo = prefixo + ("    " if is_ultimo else "│   ")
            tem_esq = no.esquerda is not None
            tem_dir = no.direita is not None

            if tem_esq:
                self.imprimir_arvore(no.esquerda, novo_prefixo, not tem_dir)
            if tem_dir:
                self.imprimir_arvore(no.direita, novo_prefixo, True)


if __name__ == "__main__":
    print("=" * 60)
    print(f"Passo D: ")
    print("=" * 60)

    print("\nTESTE 1: caso especial")
    arvore_teste = Arvore()
    for valor in [1, 2, 3]:
        print(f"Inserir: {valor}")
        arvore_teste.inserir(valor)
    print("Resultado:")
    arvore_teste.imprimir_arvore()

    print("\n" + "=" * 60)
    print("\nTESTE 2: rotação da sub-arvore")
    arvore_teste2 = Arvore()
    for valor in [10, 5, 15, 2, 7, 1]:
        arvore_teste2.inserir(valor)
    print("Resultado:")
    arvore_teste2.imprimir_arvore()

    print("\n" + "=" * 60)
    print("\nTESTE 3: Rotação dupla (LR)")
    arvore3 = Arvore()
    for valor in [10, 5, 7]:
        arvore3.inserir(valor)
    print("Resultado:")
    arvore3.imprimir_arvore()
