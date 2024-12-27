def dfs_with_spanning_tree(graph, start):
    visited = [False] * len(graph)   # Массив для отслеживания посещённых вершин
    stack = [start]                  # Стек для вершин, которые нужно посетить
    spanning_tree_edges = []         # Список для хранения рёбер каркаса

    while stack:
        vertex = stack.pop()         # Извлекаем вершину из стека
        if not visited[vertex]:      # Проверяем, была ли вершина посещена
            visited[vertex] = True   # Отмечаем текущую вершину как посещённую
            print("Обработана вершина:", vertex)
            print("Текущее состояние стека:", list(stack))

            # Проверяем всех соседей текущей вершины
            for neighbor in range(len(graph[vertex]) - 1, -1, -1):  # Смотрим в обратном порядке
                if graph[vertex][neighbor] and not visited[neighbor]:
                    stack.append(neighbor)                      # Добавляем соседа в стек
                    spanning_tree_edges.append((vertex, neighbor))  # Добавляем ребро в каркас
                    print(f"Добавлено ребро в каркас: ({vertex}, {neighbor})")

            # Выводим состояние стека после добавления новых вершин
            print("Стек после добавления новых вершин:", list(stack))
            print("-" * 30)

    return spanning_tree_edges

# Пример графа
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

# Запуск DFS с построением каркаса графа, начиная с вершины 0
start_vertex = 0
spanning_tree_edges = dfs_with_spanning_tree(graph, start_vertex)
print("Рёбра каркаса графа:", spanning_tree_edges)
