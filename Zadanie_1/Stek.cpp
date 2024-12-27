#include <iostream>
using namespace std;
struct stack {
    int Data[10];
    int check = 0;   //Индекс крайнего элемента.

    void push(int x) { if (check <= 10) { check++; Data[check] = x; } else { cout << "error"; } }

    int pop() {
        if (check != 0) {check--;return Data[check + 1];}
        else {cout << "Ошибка" << endl;}
    }

    bool is_empty() {
        if (check == 0) {return true;}
        else {return false;}
    }

    int last() {
        if (is_empty() == 1) {cout << "Стек пуст!" << endl;return -1;}
        else {return Data[check - 0];}
    }

    void print() {
        for (int i = check ; i >= 1; i--) {cout << Data[i] << " ";}
    }
    };

    int main() {
        setlocale(LC_ALL, "rus");
        stack s;

        // Проверка is_empty()
        if (s.is_empty() > 0) {cout << "Стек пуст" << endl;}
        else {cout << "В стеке присутствуют элементы" << endl;}

        // Проверка push()
        s.push(1);
        s.push(2);
        s.push(3);
        s.push(4);
        s.push(5);
        s.push(2);
 
        cout <<"Cтек состоит из : " << endl;
        s.print();
        cout << endl;

        // Проверка pop()
        s.pop();
        cout << "Cтек состоит из : " << endl;
        // Проверка удалился ли элемент
        s.print();
        cout << endl;
        
        // Проверка is_empty()
        if (s.is_empty() > 0){cout << "Стек пуст" << endl;}
        else {cout << "В стеке присутствуют элементы" << endl;}
        cout << s.last();
        return 0;
    }
