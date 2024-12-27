class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _hash(self,key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Key '{key}' already exists. Value updated to {value}.")
                return
        self.table[index].append([key, value])
        print(f"Key '{key}' inserted with value {value}.")

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Пример использования
hash_table = HashTable(10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("apple", 3)

print(hash_table.search("apple"))  # Вывод: 1
print(hash_table.search("banana"))  # Вывод: 2
hash_table.delete("apple")
print(hash_table.search("apple"))  # Вывод: None