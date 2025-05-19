#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    // Inserção
    v.push_back(10);
    v.push_back(20);

    // Remoção
    int valor = v.back();
    v.pop_back();
    std::cout << "Removido: " << valor << "\n";

    return 0;
}