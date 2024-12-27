/*#include <iostream>
#include <chrono>
#include <random>

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

// Функция для создания массива и заполнения его случайными числами
void createAndFillArray(int* arr, int size) {
    //default_random_engine generator;
    //uniform_int_distribution<int> distribution(1, 10);

    for (int i = 0; i < size; ++i) {
        arr[i] = (rand() % 100);
    }
}
// Функция для освобождения памяти массива
void freeArray(int* arr, int size) {
    delete[] arr;
}
// Функция вывода массива
void printArray(const int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
//Функция сортировки массива
void sortArray(int* arr, int size) {
    sort(arr, arr + size);
}
int main() {
    setlocale(LC_ALL, "RUS");

    const int MAX_SIZE = 1000; // Максимальный размер массива
    int* arr = nullptr;
    int size = 0;

    
    cin >> size;
    if (size >= 0 && size <= MAX_SIZE) {
        arr = new int[size];
        createAndFillArray(arr, size);


    // Передача данных в структуру
    AWC array1 = { arr, size, 0 };

    // Искомые элементы
    int key1 = 3;

    // Вызов функции последовательного поиска
    AWC result1 = sequentialSearch(array1, key1);
    printArray(arr, size);
    // вывод результата
    cout << "Кол-во сравнений для первого ключа: " << result1.comparisons << std::endl;
    // Сортировка массива

    sortArray(arr, size);
    int n = size;
    ABS abs(arr, n);
    int target1 = 7;
    int index1 = abs.binarySearch(target1);

    if (index1 != -1) {
        cout << "Элемент " << target1 << " Найден под номером " << index1 << " с " << abs.comparisons << " раза" << std::endl;
    }
    else {
        cout << "Элемент " << target1 << " Не найден" << std::endl;
    }
    // Вывод массива
    printArray(arr, size);
    freeArray(arr, size);
    }
    else {
        cerr << "Неверный размер массива." << endl;
    }
    cout << "Размер массива" << " | " << "Практическая сложность последовательного поиска" << " | " << "Практическая сложность двоичного поиска" << endl;
    

    return 0;
}
*/
#include <iostream>
#include <chrono>
#include <iomanip>  // Для форматированного вывода времени
#include <cstdlib>  // Для rand и srand
#include <ctime>    // Для инициализации генератора случайных чисел

using namespace std;
using namespace chrono;  // Для удобного использования std::chrono

// Функция для сортировки пузырьком
void bubbleSort(int* arr, int size) {
    for (int i = 0; i < size - 1; ++i) {
        for (int j = 0; j < size - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

// Функция для сортировки вставками
void insertionSort(int* arr, int size) {
    for (int i = 1; i < size; ++i) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

// Функция для заполнения массива случайными числами
void fillArray(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        arr[i] = rand() % 100;  // Заполнение случайными числами от 0 до 99
    }
}

// Функция для форматирования времени в виде HH:MM:SS:μμμμμμ
string formatTime(microseconds duration) {
    auto totalSeconds = duration.count() / 1'000'000;
    auto hours = totalSeconds / 3600;
    auto minutes = (totalSeconds % 3600) / 60;
    auto seconds = totalSeconds % 60;
    auto microseconds = duration.count() % 1'000'000;

    stringstream ss;
    ss << setfill('0') << setw(2) << hours << ":"
        << setw(2) << minutes << ":"
        << setw(2) << seconds << ":"
        << setw(6) << microseconds;
    return ss.str();
}

// Функция для печати таблицы
void printTableHeader() {
    cout << left << setw(15) << "Размер"
        << setw(25) << "Время пузырька"
        << setw(25) << "Время вставок"
        << endl;
    cout << string(65, '-') << endl;
}

void printTableRow(int size, microseconds bubbleTime, microseconds insertionTime) {
    cout << left << setw(15) << size
        << setw(25) << formatTime(bubbleTime)
        << setw(25) << formatTime(insertionTime)
        << endl;
}

int main() {
    setlocale(LC_ALL, "RUS");
    srand(time(nullptr));  // Инициализация генератора случайных чисел

    const int NUM_EXPERIMENTS = 5;  // Количество экспериментов
    const int STEP = 200;            // Шаг увеличения размера массива

    printTableHeader();  // Печать заголовка таблицы

    for (int experiment = 1; experiment <= NUM_EXPERIMENTS; ++experiment) {
        int size = experiment * STEP;  // Размер массива
        int* arr1 = new int[size];     // Массив для пузырьковой сортировки
        int* arr2 = new int[size];     // Массив для сортировки вставками

        fillArray(arr1, size);  // Заполнение массива случайными числами
        copy(arr1, arr1 + size, arr2);  // Копирование массива для другой сортировки

        // Засекаем время пузырьковой сортировки
        auto startBubble = high_resolution_clock::now();
        bubbleSort(arr1, size);
        auto endBubble = high_resolution_clock::now();
        auto bubbleDuration = duration_cast<microseconds>(endBubble - startBubble);

        // Засекаем время сортировки вставками
        auto startInsertion = high_resolution_clock::now();
        insertionSort(arr2, size);
        auto endInsertion = high_resolution_clock::now();
        auto insertionDuration = duration_cast<microseconds>(endInsertion - startInsertion);

        // Печать строки таблицы с результатами
        printTableRow(size, bubbleDuration, insertionDuration);

        // Освобождение памяти
        delete[] arr1;
        delete[] arr2;
    }

    return 0;
}
