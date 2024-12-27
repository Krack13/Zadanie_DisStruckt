import random
import math
def make_spaces(spaces):
    print(" " * spaces, end="")



class PriorityQueueHeap:
    def __init__(self):
        # Внутренний массив для хранения элементов пирамиды
        self.heap = []

    def __repr__(self):
        # Вспомогательная функция для вывода пирамиды
        return str(self.heap)

    def parent(self, i):
        # Индекс родительского узла
        return (i - 1) // 2

    def left_child(self, i):
        # Индекс левого потомка
        return 2 * i + 1

    def right_child(self, i):
        # Индекс правого потомка
        return 2 * i + 2

    def add(self, key):
        """Добавление элемента в пирамиду."""
        self.heap.append(key)  # Добавляем элемент в конец массива
        self._heapify_up(len(self.heap) - 1)  # Восстанавливаем свойство пирамиды

    def peek_max(self):
        """Возвращает максимальный элемент (в корне)."""
        if self.heap:
            return self.heap[0]
        return None

    def extract_max(self):
        """Удаляет и возвращает максимальный элемент."""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Единственный элемент

        root = self.heap[0]
        # Перемещаем последний элемент в корень
        self.heap[0] = self.heap.pop()
        # Восстанавливаем свойство пирамиды
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """Восстанавливает свойство пирамиды снизу вверх."""
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            # Меняем местами текущий элемент с родительским
            self.heap[index], self.heap[self.parent(index)] = (
                self.heap[self.parent(index)],
                self.heap[index],
            )
            index = self.parent(index)

    def _heapify_down(self, index):
        """Восстанавливает свойство пирамиды сверху вниз."""
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Находим наибольший элемент среди текущего узла и его потомков
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        # Если наибольший элемент не текущий узел, меняем местами и продолжаем
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display_pyramid_tree(self):
        if not self.heap:
            print("\nПирамида пуста\n")
            return 0

        k = 1
        j = 0
        sp = 2 ** (math.floor(math.log2(len(self.heap))))

        for level in range(math.floor(math.log2(len(self.heap))) + 1):
            make_spaces(sp)
            for i in range(k):
                if j < len(self.heap):
                    print(f"{self.heap[j]:2}", end="")
                    make_spaces(sp * 2 - 1)
                    j += 1
            k *= 2
            sp //= 2
            print("\n")

# Пример использования
pq = PriorityQueueHeap()
for i in range(25):
    pq.add(random.randint(1,1000))


print("Пирамида:", pq)
print("Максимальный элемент:", pq.peek_max())
print("Удаление максимального элемента:", pq.extract_max())
print("Пирамида после удаления:", pq)
print(pq.display_pyramid_tree())