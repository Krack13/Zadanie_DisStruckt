from collections import deque

def bfs_with_spanning_tree(graph, start):
    visited = [False] * len(graph)  # Массив для отслеживания посещённых вершин
    queue = deque([start])          # Очередь для вершин, которые нужно посетить
    visited[start] = True           # Отмечаем начальную вершину как посещённую
    spanning_tree_edges = []        # Список для хранения рёбер каркаса

    while queue:
        vertex = queue.popleft()    # Извлекаем вершину из очереди

        # Выводим текущее состояние очереди перед обработкой вершины
        print("Обработана вершина:", vertex)
        print("Текущее состояние очереди:", list(queue))

        # Проверяем всех соседей текущей вершины
        for neighbor, connected in enumerate(graph[vertex]):
            if connected and not visited[neighbor]:  # Если есть связь и сосед не посещен
                queue.append(neighbor)               # Добавляем соседа в очередь
                visited[neighbor] = True             # Помечаем его как посещённого
                spanning_tree_edges.append((vertex, neighbor))  # Добавляем ребро в каркас

        # Выводим состояние очереди после добавления новых вершин
        print("Очередь после добавления новых вершин:", list(queue))
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

# Запуск BFS с построением каркаса графа, начиная с вершины 0
start_vertex = 0
spanning_tree_edges = bfs_with_spanning_tree(graph, start_vertex)
print("Рёбра каркаса графа:", spanning_tree_edges)
