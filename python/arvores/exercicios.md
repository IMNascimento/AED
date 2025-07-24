1) Faça uma função recursiva para verificar se uma chave s[n] está contifa na trie
Struct No Patricia{
    int desvio: No patricia * filho[m]
    string chave: T * informação;
}

2) Escreva uma função recursiva e determine a altura de uma arvore avl visitando o menor m possivel de nós e 
considerando que cada nó guarda seu fator de balanceamento

3) Seja uma arvore AVL T. Considere a inserção de um no q em T que tornu T desregulada. Se p o nó desregulado mais
proximo das folhas. Seja he(p) a altura da SAE de p e h1(p) a altura da SAD de p

a) Qual o valor exato de he(p)-hd(p)?
b) Supondo hd(p) > he(p) então exista um filho direito u de p prove que necessariamente temos hd(u)-he(u)=1 e este
não pode ser 2 ou 0

c) De acordo com (b), quando hd(p)>he(p) existem dois subcasos:
(1)he(u)=hd(u)+1 ou (2)hd(u)=he(u)+1
para cada um dos subcasos mostre qual operações regula p

4) Provar ou dar contra exemplo: sejam H1 e H2 dois heap biomiais contendo k1 e k2 arvores binomiais,
respectivamente. Seja H o heap binomial resultanteda união de H1 e H2, o qual contém k arvore binomial então k<= k1 + k2.

5) Supondo um maxheap biario com M valores, crie um algoritmo recursivo para retornar a quantidade de valores maiores que x dentro dessa arvore contigua acessando o minimo


