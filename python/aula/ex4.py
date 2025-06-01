#Problema 
# VocÊ precisa buscar documentos em uma coleção usando palavras chave. Para isso você pensa em criar 
#uma estrutura de dados que armazene as palavras de um documento possui a frequencia com que ela ocorre no documentoe quantos docs possui esta palavra:
#projete a estrutura 
# implemente com lista encadeada sendo uma lista para palavra e a outra lista documentos

#solução
# class WordNode:
#     def __init__(self, word):
#         self.word = word
#         self.frequency = 0
#         self.documents = None  # Lista encadeada de documentos
#         self.next = None

# class DocumentNode:
#     def __init__(self, doc):
#         self.doc = doc
#         self.next = None

# class WordList:
#     def __init__(self):
#         self.head = None

#     def add_word(self, word, doc):
#         """Adiciona uma palavra e o documento associado à lista de palavras."""
#         current = self.head
#         while current:
#             if current.word == word:
#                 current.frequency += 1
#                 self.add_document(current, doc)
#                 return
#             current = current.next
        
#         # Se a palavra não existe, cria um novo nó
#         new_word_node = WordNode(word)
#         new_word_node.frequency = 1
#         new_word_node.documents = DocumentNode(doc)
#         new_word_node.next = self.head
#         self.head = new_word_node

#     def add_document(self, word_node, doc):
#         """Adiciona um documento à lista de documentos de uma palavra."""
#         current_doc = word_node.documents
#         while current_doc:
#             if current_doc.doc == doc:
#                 return  # Documento já existe
#             if not current_doc.next:
#                 break
#             current_doc = current_doc.next
        
#         # Adiciona novo documento ao final da lista
#         new_doc_node = DocumentNode(doc)
#         if not word_node.documents:
#             word_node.documents = new_doc_node
#         else:
#             current_doc.next = new_doc_node

#     def print_words(self):
#         """Imprime todas as palavras e seus documentos associados."""
#         current = self.head
#         while current:
#             print(f"Word: {current.word}, Frequency: {current.frequency}, Documents: ", end="")
#             doc_current = current.documents
#             while doc_current:
#                 print(doc_current.doc_id, end=" ")
#                 doc_current = doc_current.next
#             print()  # Nova linha para separar as saídas
#             current = current.next
    
# # Exemplo de uso
# word_list = WordList()
# word_list.add_word("python, python", "doc1")
# word_list.add_word("python", "doc2")
# word_list.add_word("java", "doc1")

# word_list.print_words()
# Saída esperada:

class Node:
    def __init__(self, doc_node, word, next= None, frequency=1):
        self.doc_node = doc_node
        self.word = word
        self.next = next
        self.frequency = frequency

class DocNode:
    def __init__(self, content):
        self.content = content
        self.next = None

class DocumentRepo:
    def __init__(self):
        self.head = None

    def add_document(self, doc_content):
        # pega as palavras no doc_content, procura se já existe, se não existir cria um novo nó, adiciona o documento e incrementa a frequência
        words = doc_content.split()
        sla = {}
        for w in words:

            if w in sla:
                sla[w] += 1
            else:
                sla[w] = 1
        for word, freq in sla.items():
            new_doc_node = DocNode(doc_content)
            current = self.head
            if self.head is None:
                self.head = Node(new_doc_node, word, frequency=freq)
            else:
                while current:
                    if current.word == word:
                        new_doc_node.next = current.doc_node
                        current.doc_node = new_doc_node
                        current.frequency += freq
                        break
                    current = current.next
                if current is None:
                    new_node = Node(new_doc_node, word, frequency=freq)
                    new_node.next = self.head
                    self.head = new_node

    def get_docs_with_word(self, word):
        """Retorna uma lista de documentos que contêm a palavra especificada."""
        docs = []
        current = self.head
        while current:
            if current.word == word:
                doc_node = current.doc_node
                while doc_node:
                    docs.append(doc_node.content)
                    doc_node = doc_node.next
                break
            current = current.next
            
        return docs


    def get_frequency(self, word):
        """Retorna a frequência da palavra especificada."""
        current = self.head
        while current:
            if current.word == word:
                return current.frequency
            current = current.next
        return 0

repo = DocumentRepo()
repo.add_document("python python")
repo.add_document("python")
repo.add_document("java java")
print(repo.get_docs_with_word("java"))
print(repo.get_frequency("java"))
print(repo.get_docs_with_word("python"))
# Saída esperada: ["python python"]

print(repo.get_frequency("python"))
# Saída esperada: 2