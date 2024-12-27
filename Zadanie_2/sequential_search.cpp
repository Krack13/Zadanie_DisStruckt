#include <iostream>
using namespace std;
// Структура для хранения массива, размера, кол-ва стравнений
struct AWC {
    int* arr;
    int size;
    int comparisons;
};
// Функция поиска элемента в массиве 
AWC sequentialSearch(AWC array, int key) {
    AWC result = { array.arr, array.size, 0 };

    for (int i = 0; i < array.size; i++) {
        result.comparisons++;
        if (array.arr[i] == key) {
            return result;
        }
    }

    return result;
}

int main() {
    setlocale(LC_ALL, "RUS");
    // Созданние массивов
    int arr1[] = { 1, 2, 3, 4, 5 };
    int arr2[] = { 3, 6, 9, 12, 15, 18 };
    int arr3[] = { 7, 14, 21, 28, 35, 42, 49 };
    int arr4[] = { 7, 20, 56, 59, 83, 0, 97, 18, 83, 63, 5, 67, 94, 81, 78, 41, 13, 24, 60, 44, 59, 41, 79, 100, 2, 38, 97, 47, 53, 20, 32, 77, 29, 0, 12, 86, 35, 85, 17, 86, 37, 11, 3, 5, 4, 43, 12, 51, 62, 86, 64, 17, 95, 78, 47, 14, 45, 57, 68, 0, 89, 5, 64, 21, 73, 35, 32, 2, 68, 46, 24, 73, 75, 91, 22, 37, 44, 93, 74, 73, 37, 22, 27, 72, 24, 27, 28, 10, 30, 89, 37, 25, 29, 66, 50, 79, 67, 82, 31, 79 };
    // Передача данных в структуру
    AWC array1 = { arr1, 5, 0 };
    AWC array2 = { arr2, 6, 0 };
    AWC array3 = { arr3, 7, 0 };
    AWC array4 = { arr4, 100, 0 };
    // Искомые элементы
    int key1 = 3;
    int key2 = 12;
    int key3 = 49;
    int key4 = 31;
    // Вызов функции последовательного поиска
    AWC result1 = sequentialSearch(array1, key1);
    AWC result2 = sequentialSearch(array2, key2);
    AWC result3 = sequentialSearch(array3, key3);
    AWC result4 = sequentialSearch(array4, key4);
    // вывод результата
    cout << "Кол-во сравнений для первого ключа: " << result1.comparisons << std::endl;
    cout << "Кол-во сравнений для второго ключа: " << result2.comparisons << std::endl;
    cout << "Кол-во сравнений для третьего ключа: " << result3.comparisons << std::endl;
    cout << "Кол-во сравнений для четвертого ключа: " << result4.comparisons << std::endl;

    return 0;
}
