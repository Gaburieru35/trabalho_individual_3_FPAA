# Caminho Hamiltoniano - Projeto de Análise de Algoritmos

## Descrição do Projeto

Este projeto implementa um algoritmo para encontrar um **Caminho Hamiltoniano** em um grafo. Um Caminho Hamiltoniano é aquele que visita **todos os vértices exatamente uma vez**. Utilizamos a abordagem de **Backtracking** para tentar construir esse caminho.

### Lógica do Algoritmo

- Iniciamos com o primeiro vértice fixado.
- Em cada passo, tentamos adicionar um novo vértice ao caminho.
- Verificamos se é seguro adicionar o vértice:
  - Deve haver uma aresta entre o último vértice no caminho e o novo vértice.
  - O vértice ainda não pode ter sido visitado.
- Se em algum ponto não for possível adicionar vértices, fazemos **backtracking** e tentamos outras possibilidades.

# Explicação do Algoritmo de Caminho Hamiltoniano

Este documento explica a implementação de um algoritmo de backtracking para encontrar um Caminho Hamiltoniano em um grafo. Um Caminho Hamiltoniano é um caminho que visita cada vértice de um grafo exatamente uma vez.

## Visão Geral do Código

O algoritmo implementa uma solução baseada em backtracking, que explora sistematicamente todas as possibilidades até encontrar uma solução válida ou esgotar todas as possibilidades.

```python
def is_safe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return True
    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            # backtrack
            path[pos] = -1
    return False

def hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_util(graph, path, 1):
        print("Não existe Caminho Hamiltoniano")
        return False
    print("Caminho Hamiltoniano encontrado:")
    print(path)
    return True
```

## Explicação Detalhada das Funções

### Função `is_safe(v, pos, path, graph)`

Esta função verifica se é seguro adicionar o vértice `v` na posição `pos` do caminho:

```python
def is_safe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True
```

**Explicação linha a linha:**

1. `if graph[path[pos - 1]][v] == 0:` - Verifica se existe uma aresta entre o último vértice adicionado (`path[pos - 1]`) e o vértice candidato `v`. Se o valor na matriz de adjacência for 0, significa que não existe conexão, então retorna False.
   
2. `if v in path:` - Verifica se o vértice `v` já está presente no caminho. Como um Caminho Hamiltoniano exige que cada vértice seja visitado exatamente uma vez, se o vértice já estiver no caminho, retorna False.

3. `return True` - Se o vértice passar pelas duas verificações anteriores, é seguro adicioná-lo ao caminho.

### Função `hamiltonian_util(graph, path, pos)`

Esta é a função recursiva principal que implementa o algoritmo de backtracking:

```python
def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return True
    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            # backtrack
            path[pos] = -1
    return False
```

**Explicação linha a linha:**

1. `if pos == len(graph):` - Condição de término da recursão. Se já preenchemos todas as posições do caminho (ou seja, visitamos todos os vértices), encontramos um Caminho Hamiltoniano válido.

2. `for v in range(1, len(graph)):` - Itera por todos os vértices do grafo, exceto o vértice 0 (que já é definido como o ponto de partida).

3. `if is_safe(v, pos, path, graph):` - Verifica se é seguro adicionar o vértice `v` na posição atual do caminho.

4. `path[pos] = v` - Se for seguro, adiciona o vértice `v` ao caminho na posição `pos`.

5. `if hamiltonian_util(graph, path, pos + 1):` - Chamada recursiva para preencher o resto do caminho, avançando para a próxima posição.

6. Se a chamada recursiva retornar True, significa que encontramos um caminho válido, então também retornamos True para propagar o sucesso.

7. `path[pos] = -1` - Backtracking: se a tentativa atual falhar (o caminho não leva a uma solução), remove o vértice do caminho e tenta a próxima possibilidade.

8. `return False` - Se todas as possibilidades de vértices forem esgotadas sem encontrar um caminho válido, retorna False.

### Função `hamiltonian_path(graph)`

Esta função inicializa e gerencia o processo de busca:

```python
def hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_util(graph, path, 1):
        print("Não existe Caminho Hamiltoniano")
        return False
    print("Caminho Hamiltoniano encontrado:")
    print(path)
    return True
```

**Explicação linha a linha:**

1. `path = [-1] * len(graph)` - Cria um vetor para armazenar o caminho, inicializado com -1 em todas as posições, indicando que nenhum vértice foi visitado ainda.

2. `path[0] = 0` - Define o primeiro vértice do caminho como 0, estabelecendo o ponto de partida.

3. `if not hamiltonian_util(graph, path, 1):` - Chama a função recursiva para encontrar um caminho, começando da posição 1 (já que a posição 0 está ocupada pelo vértice inicial).

4. Se a função `hamiltonian_util` retornar False, imprime uma mensagem informando que não existe Caminho Hamiltoniano e retorna False.

5. Se um caminho for encontrado, imprime o caminho e retorna True.

### Bloco Principal do Programa

```python
if __name__ == "__main__":
    # Exemplo 1: Grafo que possui Caminho Hamiltoniano
    graph_hamiltoniano = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    
    # Exemplo 2: Grafo que NÃO possui Caminho Hamiltoniano
    graph_nao_hamiltoniano = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    
    print("Grafo Hamiltoniano:")
    path1 = hamiltonian_path(graph_hamiltoniano)
    if path1:
        print("Caminho encontrado:", path1)
    else:
        print("Não existe Caminho Hamiltoniano.")
        
    print("\nGrafo NÃO Hamiltoniano:")
    path2 = hamiltonian_path(graph_nao_hamiltoniano)
    if path2:
        print("Caminho encontrado:", path2)
    else:
        print("Não existe Caminho Hamiltoniano.")
```

### Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/Gaburieru35/trabalho_individual_3_FPAA.git
```

2. Navegue até o diretório:
```bash
cd trabalho_individual_3_FPAA
```

3.Execute o arquivo:
```bash
python main.py
```

## Relatório Técnico

### Classes de Complexidade: P, NP, NP-Completo, NP-Difícil

- O **Problema do Caminho Hamiltoniano** pertence à classe **NP-Completo**.

#### Justificativa
- **Verificação em tempo polinomial:** Dado um caminho, podemos verificar se ele é Hamiltoniano em tempo polinomial, apenas checando se todos os vértices foram visitados uma vez.
- **Sem algoritmo polinomial conhecido:** Não existe um algoritmo conhecido que resolva o problema em tempo polinomial para grafos gerais.
- **Redução de problemas:** O problema do Caminho Hamiltoniano é redutível ao Problema do Caixeiro Viajante (TSP), que é **NP-Completo**.

Portanto, o Caminho Hamiltoniano é um problema **NP-Completo**.

---

### Análise da Complexidade Assintótica de Tempo

- A complexidade temporal do algoritmo implementado é **O(N!)**, onde **N** é o número de vértices do grafo.

#### Método de Determinação
- O algoritmo tenta todas as possíveis permutações de vértices para encontrar um caminho válido.
- Cada vértice pode levar a várias tentativas de caminho, resultando em uma explosão fatorial no número de chamadas recursivas.
- A contagem de operações indica que o crescimento é **fatorial** (N!).
  
**Resumo:**  
- Complexidade de tempo: **O(N!)**
- Complexidade de espaço: **O(N)** (devido à lista `path` que armazena o caminho atual).

---

### Aplicação do Teorema Mestre

- **O Teorema Mestre não pode ser aplicado neste caso.**

#### Justificativa
- O Teorema Mestre se aplica a **algoritmos recursivos** que se dividem em subproblemas de tamanhos menores com recorrência da forma:
T(n) = a * T(n/b) + f(n)


- O algoritmo de Backtracking para Caminho Hamiltoniano não se encaixa nesse padrão.
- A cada passo, o problema não é simplesmente dividido, mas sim **explodido** em múltiplas possibilidades (sem divisão proporcional).

Por isso, **não é possível aplicar o Teorema Mestre**.

---

### Análise dos Casos de Complexidade

| Caso            | Descrição | Complexidade | Impacto |
|-----------------|-----------|--------------|---------|
| **Melhor caso** | O caminho Hamiltoniano é encontrado rapidamente, sem muitas chamadas recursivas. | **O(N²)** aproximadamente | Raro na prática, mas acontece em grafos muito conectados. |
| **Caso médio**  | Algumas tentativas e retrocessos (backtracks) são necessárias. | **O(N!)** | Ocorre em grafos com conexões moderadas. |
| **Pior caso**   | Todas as combinações possíveis são tentadas sem sucesso ou só a última é válida. | **O(N!)** | Típico em grafos muito desconexos ou complexos. |

#### Considerações
- O **pior caso** domina a análise assintótica.
- **Backtracking** é intrinsecamente **exponencial** para esse problema.

---


