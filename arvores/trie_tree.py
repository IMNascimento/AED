class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário para armazenar os filhos
        self.is_end_of_word = False  # Indica se este nó é o fim de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Inicializa a raiz da Trie

    def insert(self, word):
        # Insere uma palavra na Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        # Busca uma palavra na Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        # Verifica se existe alguma palavra na Trie que começa com o prefixo
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Exemplo de uso
if __name__ == "__main__":
    trie = Trie()  # Cria uma instância da Trie

    # Insere palavras na Trie
    trie.insert("hello")
    trie.insert("world")
    trie.insert("hi")
    trie.insert("her")
    trie.insert("hero")
    trie.insert("heron")

    # Busca por palavras na Trie
    print(trie.search("hello"))  # True
    print(trie.search("hero"))  # True
    print(trie.search("heron"))  # True
    print(trie.search("her"))  # True
    print(trie.search("he"))  # False
    print(trie.search("hell"))  # False

    # Verifica prefixos na Trie
    print(trie.starts_with("he"))  # True
    print(trie.starts_with("wo"))  # True
    print(trie.starts_with("her"))  # True
    print(trie.starts_with("hi"))  # True
    print(trie.starts_with("ho"))  # False