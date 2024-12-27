def dfs(graph, start):
    visited = [False] * len(graph)  # Массив для отслеживания посещённых вершин
    stack = [start]                 # Стек для вершин, которые нужно посетить
    order = []                      # Список для записи порядка обхода

    while stack:
        vertex = stack.pop()        # Извлекаем вершину из стека
        if not visited[vertex]:     # Проверяем, была ли вершина посещена
            visited[vertex] = True  # Отмечаем текущую вершину как посещённую
            order.append(vertex)    # Добавляем её в порядок обхода

            # Выводим состояние стека после обработки вершины
            print("Обработана вершина:", vertex)
            print("Текущее состояние стека:", list(stack))

            # Добавляем в стек всех соседей текущей вершины, которые не были посещены
            for neighbor in range(len(graph[vertex]) - 1, -1, -1):  # Смотрим в обратном порядке
                if graph[vertex][neighbor] and not visited[neighbor]:
                    stack.append(neighbor)

            # Выводим состояние стека после добавления новых вершин
            print("Стек после добавления новых вершин:", list(stack))
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

# Запуск DFS, начиная с вершины 0
start_vertex = 0
order = dfs(graph, start_vertex)
print("Порядок обхода в глубину:", order)
