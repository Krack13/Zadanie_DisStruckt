class PriorityQueueHeap:
    def __init__(self):
        self.heap = []

    def __repr__(self):
        return str(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def add(self, edge):
        """Добавление ребра в пирамиду."""
        self.heap.append(edge)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """Удаление и возврат ребра с минимальным весом."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0 and self.heap[index][2] < self.heap[self.parent(index)][2]:
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left][2] < self.heap[smallest][2]:
            smallest = left
        if right < len(self.heap) and self.heap[right][2] < self.heap[smallest][2]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


class DSU:
    def __init__(self, n):
        """Инициализация системы непересекающихся множеств (DSU)."""
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        """Находит представителя множества для элемента u."""
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Сжатие пути
        return self.parent[u]

    def union(self, u, v):
        """Объединяет два множества."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_mst(edges, num_vertices):
    """Алгоритм Крускала для построения MST."""
    pq = PriorityQueueHeap()
    dsu = DSU(num_vertices)

    # Добавление всех рёбер в пирамиду
    for edge in edges:
        pq.add(edge)

    mst = []  # Список для хранения рёбер минимального остовного дерева
    while len(mst) < num_vertices - 1 and len(pq.heap) > 0:
        u, v, weight = pq.extract_min()  # Извлекаем ребро с минимальным весом
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, weight))

    return mst


# Пример использования
# Ребра графа с весами
edges = [
    (0, 1, 4),  # a-b
    (0, 7, 8),  # a-h
    (1, 2, 8),  # b-c
    (1, 7, 11), # b-h
    (2, 3, 7),  # c-d
    (2, 8, 2),  # c-i
    (2, 5, 4),  # c-f
    (3, 4, 9),  # d-e
    (3, 5, 14), # d-f
    (4, 5, 10), # e-f
    (5, 6, 2),  # f-g
    (6, 7, 1),  # g-h
    (6, 8, 6),  # g-i
    (7, 8, 7),  # h-i
]

num_vertices = 9  # Количество вершин

# Запускаем алгоритм Крускала
mst = kruskal_mst(edges, num_vertices)
print("Рёбра минимального остовного дерева:", mst)

