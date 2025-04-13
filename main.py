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