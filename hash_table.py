# Participantes: Bruno Wellar e Gustavo Py
import statistics
import unicodedata

nomes = [
    "João", "João Silva","Ana Clara", "Ana Cláudia",
    "Andressa", "André", "Roberta", "Roberto", "Carla","Karl",
    "Marcos", "Marcus", "Pablo", "Pabllo", "Fernanda", "Fernando",
    "Gabriela", "Gabriel", "Juliana", "Juliano"
]

class HashTable():
  def __init__(self, size=10) -> None:
    #tamanho da tabela (default 10 pra teste)
    self.size = size
    
    #inicia a tabela
    #lista com listas internas com tuplas (chave valor) 
    self.tabela = [[] for _ in range(size)] 
    
    #inicia as colisões em 0 e sempre que inserir um novo elemento
    #e o indice já estiver ocupado, aumenta
    self.colisoes = 0

  def _normalizar_chave(self, key: str) -> str:
    """
    Normaliza a chave removendo espaços, acentos e convertendo para minúscula.
    """
    #remove os espaços da chave
    sem_espacos = key.replace(" ", "")
    
    #converte tudo para minúscula
    minuscula = sem_espacos.lower()
    
    #remove os acentos utilizando normalização unicode
    #NFD separa os caracteres base dos acentos
    nfd = unicodedata.normalize('NFD', minuscula)
    
    #filtra apenas os caracteres que não são marcas diacríticas (acentos)
    #categoria 'Mn' = Nonspacing Mark (acentos, til, cedilha, etc)
    sem_acentos = ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
    
    return sem_acentos

  def _hash(self, key: str) -> int:
    #primeiro, como funciona a nossa hash?
    #vamos ignorar os espaços e acentos, converter tudo para minusculo
    #e utilizar numero primo para o calculo, alem de fazer o modulo
    #pelo tamanho da tabela.

    n_primo = 17
    
    #trata a "Key" pra não ter diferença entre "Gabriel", " gabriel" e "Gabriél"
    #agora usando a função de normalização que remove acentos também
    chave_tratada = self._normalizar_chave(key)
    
    #calculamos o valor do hash 
    valor_hash = 0
    
    #para cada caractere na chave tratada
    for indice, caractere in enumerate(chave_tratada):
      #ord() retorna o valor unicode do caractere
      #esse calculo faz o seguinte:
      #pega o indice do caractere na string (0,1,2,3...)
      #soma com o tamanho da chave tratada
      #multiplica pelo nosso numero primo e
      #multiplica pelo valor unicode do caractere
      valor_hash += (indice + len(chave_tratada)) * n_primo * ord(caractere)
      
    #agora so fazemos o modulo pelo tamanho da tabela 
    #e ta feito o pagode
    return valor_hash % self.size

  def insert(self, key: str, valor):
    #vamos inserir o chave-valor, sendo chave o nome e o valor
    #podendo ser qualquer coisa
    #no final vai retornar onde ele foi inserido

    #inicia descobrinho a posiçao na tabela
    posicao = self._hash(key) 
    
    #posição do dado na estrutura de dados
    tabela = self.tabela[posicao] 

    #verificamo se já existe algumacoisa nessa posiçao

    for i, (k,v) in enumerate(tabela):
      if k == key:
        #se já existe, atualiza o valor pelo novo
        tabela[i] = (key,valor)
        return
    
    if len(tabela) > 0:
      #se ja tem algo nessa posiçao, é colisao
      #então aumenta o contador
      self.colisoes += 1

    #se não achou a chave, insere o novo par (chave, valor)
    tabela.append((key,valor))
    
    #retorna onde foi inserido
    return posicao

  def load_factor(self) -> float:
    #o load factor é basicamente quantos elementos
    #temos dividido pelo tamanho da tabela
    
    #soma o tamanho de cada par na tabela 
    total_elementos = sum(len(par) for par in self.tabela)
    
    return total_elementos / self.size
        
#grafico de distribuição da hash
  def avaliar_hash(self):
        """
        Avalia a qualidade da função hash através de métricas estatísticas
        """
        #calcula a ditrubuiçao dos elementos
        #pegando o tamanho de cada par na tabela 
        distribuicao = [len(par) for par in self.tabela]
        #pega o total de elementos inseridos
        elementos_total = sum(distribuicao)
        #posiçoes vazias e ocupadas
        #o calculo de ocupadas é contando quantos indices
        #tem valor maior que 0 na distribuicao
        posicoes_ocupadas = sum(1 for x in distribuicao if x > 0)
        #já do de cazias é o tamanho total menos as ocupadas
        posicoes_vazias = self.size - posicoes_ocupadas
        
        #pior caso
        maior_cadeia = max(distribuicao)
        
        print(f"\n{'='*60}")
        print("ANÁLISE DE QUALIDADE DA FUNÇÃO HASH")
        print(f"{'='*60}")
        print(f"Tamanho da tabela:              {self.size}")
        print(f"Total de elementos inseridos:   {elementos_total}")
        print(f"Posições ocupadas:              {posicoes_ocupadas} ({posicoes_ocupadas/self.size*100:.1f}%)")
        print(f"Posições vazias:                {posicoes_vazias} ({posicoes_vazias/self.size*100:.1f}%)")
        print(f"-" * 60)
        print(f"Load Factor:                    {self.load_factor():.2f}")
        print(f"Número de colisões:             {self.colisoes}")
        print(f"Maior cadeia (pior caso):       {maior_cadeia} elementos")
        print(f"{'='*60}")
       
        print(f"\nDISTRIBUIÇÃO VISUAL:")
        print(f"{'-'*60}")
        for i, count in enumerate(distribuicao):
            barra = "█" * count
            print(f"Posição {i:2d}: {barra} ({count})")
        print(f"{'='*60}\n")
        
if __name__ == "__main__":
    #cria a hash table com tamanho 10 (pra testes)
    tabela_hash = HashTable() #default é 10
    
    print("Inserindo nomes na tabela hash...")
    print("-" * 40)
    
    for nome in nomes:
        #insere o nome mas com o valor vazio (dict vazio)
        posicao = tabela_hash.insert(nome, {})
        print(f"Nome '{nome}' inserido na tabela na posição {posicao}.")
    
    print("-" * 40)
    print(f"Número de colisões ocorridas: {tabela_hash.colisoes}")
    load = tabela_hash.load_factor()
    print(f"Load factor da tabela: {load:.2f}")
    print("-" * 40)
    
    tabela_hash.avaliar_hash()