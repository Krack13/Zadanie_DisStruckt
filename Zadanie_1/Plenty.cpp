#include <iostream>
using namespace std;

struct Plenty {

    int Data[10];
    int check = 0;   //Индекс крайнего элемента.
    bool exists[10];
    void init() {
        for (int i = 0; i < 10; i++) {exists[i] = false;}}

    int getEmptyPosition() {
        for (int i = 0; i < 10; i++) {if (!exists[i]) {return i;}}
        return -1;
    }

    void add(int x) {
        int pos = getEmptyPosition();
        if (pos != -1) {Data[pos] = x;exists[pos] = true;check++;}
        else {cout << "Мест нет!"<<endl;}
    }

    void print() {
        for (int i = 0; i < 10; i++) {if (exists[i]) {cout << Data[i] << " ";}}
        cout << endl;
    }

    bool contains(int x) {
        for (int i = 0; i < 10; i++) {if (exists[i] && Data[i] == x) {return true;}}
        return false;
    }
    void delet(int x) {
        int pos = contains(x);
        if (pos != -1) {exists[pos] = false;check--;}
        else {cout << "Такого элемента нет";}
    }

    bool is_empty() {
        if (check == 0) {return true;}
        else {return false;}
    }
};
int main() {
    setlocale(LC_ALL, "rus");
    Plenty s;
    s.init();
    // Проверка add()
    s.add(1);
    s.add(7);
    s.add(3);
    s.add(4);
    s.add(5);
    // Проверка print()
    cout << "Список состоит из : " << endl;
    s.print();
    cout << endl;
    // Проверка contains(x)
    if (s.contains(7) == 1) {
        cout << "Искомый элемент есть в множестве" << endl;
    }
    else { cout << "Искомый элемент не найден в множестве" << endl; }
    // Проверка delet()
    s.delet(7);
    cout << "Список состоит из : " << endl;
    // Проверка удалился ли элемент
    s.print();
    // Проверка is_empty()
    if (s.is_empty() == 0) { cout << "В множестве что-то есть" << endl; }
    else { cout << "В множестве нет элементов" << endl; };
    return 0;
}