#include <iostream>
using namespace std;

struct list {
    int Data[10];
    int check = 0;   //Индекс крайнего элемента.

    void insert(double x, int pos) {
        if (check == 10) {cout << "Список полон!"<< endl;}
        else if (!(0 <= pos && pos <= check)) {cout << "Индекс элемента не входит в список"<< endl;}
        else {for (int i = check; i >= pos; i--) {Data[i + 1] = Data[i];}
            Data[pos+1] = x;
            check++;
        }
    }

    int indexOf(double x) {
        for (int i = 0; i < check; i++) {if (Data[i] == x) {return i;}}
        return -1;
    }

    void remove(int pos) {
        if (pos == -1) {cout << "No such element\n";}
        else {for (int i = pos; i < check; i++) {Data[i] = Data[i + 1];}
            check--;
        }
    }

    bool is_empty() {
        if (check == 0) {return true;}
        else {return false;}
    }

    int last() {
        if (is_empty() == 1) {cout << "Список пуст!" << endl;return -1;}
        else {return Data[check - 0];}
    }

    void print() {
        for (int i = check; i >= 1; i--) {cout << Data[i] << " ";}
    }
};
int main() {
    setlocale(LC_ALL, "rus");
    list s;

    // Проверка is_empty()
    if (s.is_empty() > 0) {cout << "Список пуст" << endl;}
    else {cout << "В списке присутствуют элементы" << endl;}

    // Проверка push()
    s.insert(1,0);
    s.insert(7,1);
    s.insert(3,2);
    s.insert(4,3);
    s.insert(5,2);

    // Проверка print()
    cout << "Список состоит из : " << endl;
    s.print();
    cout << endl;

    // Проверка remove()
    s.remove(2);
    cout << "Список состоит из : " << endl;

    // Проверка удалился ли элемент
    s.print();
    cout << endl;

    // Проверка indexOf()
    cout << "Индекс искомого значени:" << s.indexOf(5) << endl;

    // Проверка last()
    cout << "Последний элемент списка: " << s.last();
    return 0;

}

