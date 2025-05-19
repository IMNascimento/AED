#include <iostream>
#include <list>

int main() {
    std::list<int> lst;
    // Inserção no início e fim
    lst.push_back(10);
    lst.push_front(20);
    lst.push_back(30);

    // Impressão para frente
    for (int v : lst) std::cout << v << " <-> ";
    std::cout << "NULL
";

    // Impressão para trás
    for (auto it = lst.rbegin(); it != lst.rend(); ++it)
        std::cout << *it << " <-> ";
    std::cout << "NULL
";

    // Remover elemento do meio (por iterator)
    auto it = lst.begin();
    std::advance(it, 1); // aponta para o segundo elemento
    lst.erase(it);

    // Imprime após remoção
    for (int v : lst) std::cout << v << " <-> ";
    std::cout << "NULL
";

    return 0;
}