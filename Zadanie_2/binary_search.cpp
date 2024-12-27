#include <iostream>
using namespace std;
// Структура хранения массива, размер, кол-во сравнений
struct ABS {
    int* array;
    int size;
    int comparisons;
// Конструктор класса с размером и указателем
    ABS(int* arr, int n) {
        array = arr;
        size = n;
        comparisons = 0;
    }
// Функция бинарного поиска
    int binarySearch(int target) {
        int left = 0;
        int right = size - 1;

        while (left <= right) {
            comparisons++;

            int mid = left + (right - left) / 2;

            if (array[mid] == target) {
                return mid;
            }
            else if (array[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return -1;
    }
};

int main() {
    setlocale(LC_ALL, "RUS");
    // заранее отсортированный массив, потому что лень делать сортировку :(
    int arr[] = { 2, 2, 3, 4, 7, 9, 9, 10, 10, 10 };
    int n = sizeof(arr) / sizeof(arr[0]);
    // Создание экземпляра класса
    ABS abs(arr, n);
    // Искомый первый элемент 
    int target1 = 7;
    int index1 = abs.binarySearch(target1);

    if (index1 != -1) {
        cout << "Элемент " << target1 << " Найден под номером " << index1 << " с " << abs.comparisons << " раза" << std::endl;
    }
    else {
        cout << "Элемент " << target1 << " Не найден" << std::endl;
    }
    //Обнуление счетчика сравнений
    abs.comparisons = 0;
    // Поиск второго элемента
    int target2 = 8;
    int index2 = abs.binarySearch(target2);

    if (index2 != -1) {
        cout << "Элемент " << target2 << " Найден под номером " << index2 << " с " << abs.comparisons << " раза" << std::endl;
    }
    else {
        cout << "Элемент " << target2 << " Не найден" << std::endl;
    }

    return 0;
}
