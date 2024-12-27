from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)  # Массив для отслеживания посещённых вершин
    queue = deque([start])          # Очередь для вершин, которые нужно посетить
    visited[start] = True           # Отмечаем начальную вершину как посещённую
    order = []                      # Список для записи порядка обхода

    while queue:
        vertex = queue.popleft()    # Извлекаем вершину из очереди
        order.append(vertex)        # Добавляем её в порядок обхода

        # Выводим текущее состояние очереди перед добавлением новых вершин
        print("Обработана вершина:", vertex)
        print("Текущее состояние очереди:", list(queue))

        # Проверяем всех соседей текущей вершины
        for neighbor, connected in enumerate(graph[vertex]):
            if connected and not visited[neighbor]:  # Если есть связь и сосед не посещен
                queue.append(neighbor)               # Добавляем соседа в очередь
                visited[neighbor] = True             # Помечаем его как посещённого

        # Выводим состояние очереди после добавления новых вершин
        print("Очередь после добавления новых вершин:", list(queue))
        print("-" * 30)

    return order

# Пример графа
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

# Запуск BFS, начиная с вершины 0
start_vertex = 2
order = bfs(graph, start_vertex)
print("Порядок обхода в ширину:", order)
