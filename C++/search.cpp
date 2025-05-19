#include <iostream>
#include <vector>

int busca(const std::vector<int>& v, int chave) {
    for (size_t i = 0; i < v.size(); ++i) {
        if (v[i] == chave)
            return (int)i;
    }
    return -1;
}

int main() {
    std::vector<int> v = { 10, 20, 30, 40, 50 };
    int pos = busca(v, 30);
    if (pos >= 0)
        std::cout << "Encontrado na posição " << pos << "\n";
    else
        std::cout << "Não encontrado\n";
    return 0;
}