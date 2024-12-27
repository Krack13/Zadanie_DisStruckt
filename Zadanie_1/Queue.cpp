#include <iostream>
using namespace std;

struct qeueue {
    int Data[10];
    int check = 0;   //Индекс крайнего элемента.

    void push(int x) {check++;Data[check] = x;}

    int remove() {
        if (check != 0) {for (int i = 0; i < check; i++) {Data[i] = Data[i + 1];}check--;return Data[check];}
        else {cout << "Ошибка, очередь пуста" << endl;}
    }

    bool is_empty() {
        if (check == 0) {return true;}
        else {return false;}
    }

    int last() {
        if (is_empty() == 1) { cout << "Очередь пуста!" << endl;return -1;}
        else {return Data[check - 0];}
    }

    void print() {
        for (int i = check; i >= 1; i--) {cout << Data[i] << " ";}
    }
};
int main() {
    setlocale(LC_ALL, "rus");
    qeueue s;
    // Проверка is_empty()
    if (s.is_empty() > 0) {cout << "Очередь пуста" << endl;}
    else {cout << "В очереди присутствуют элементы" << endl;}

    // Проверка push()
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    cout << "Очередь состоит из : " << endl;
    // Проверка print()
    s.print();
    cout << endl;
    
    // Проверка pop()
    s.remove();
    cout << "Очередь состоит из : " << endl;
    // Проверка удалился ли элемент
    s.print();
    cout << endl;

    // Проверка is_empty() когда в очереди есть элементы
    if (s.is_empty() > 0) {cout << "Очередь пуста" << endl;}
    else {cout << "В очереди присутствуют элементы" << endl;}
    // Проверка last()
    cout << s.last();
    return 0;

}

