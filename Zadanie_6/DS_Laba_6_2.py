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

    def add(self, key):
        """Добавление элемента в пирамиду."""
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """Удаление и возврат максимального элемента."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def _heapify_down(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)


def heap_sort(arr):
    """Функция для выполнения пирамидальной сортировки."""
    # Создаём пирамиду
    heap = PriorityQueueHeap()

    # Добавляем все элементы массива в пирамиду
    for el in arr:
        heap.add(el)

    # Извлекаем элементы из пирамиды в отсортированном порядке
    sorted_arr = []
    while len(heap.heap) > 0:
        sorted_arr.append(heap.extract_max())

    # Возвращаем массив в обратном порядке для сортировки по возрастанию
    return sorted_arr[::-1]


# Пример использования
arr = [10, 3, 15, 7, 8, 23, 1]
print("Исходный массив:", arr)

sorted_array = heap_sort(arr)
print("Отсортированный массив:", sorted_array)
