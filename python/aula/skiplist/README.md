# SkipList Interativa com Visualização

Implementação **profissional** de SkipList em Python, com persistência de estrutura (valores + alturas dos nós), visualização em ASCII, gráficos PNG e interface web interativa via Streamlit.  
Os dados e gráficos ficam organizados em subpastas para máxima organização!

![Exemplo de Skiplist](https://github.com/user-attachments/assets/4060e128-8115-4d0a-8482-af6860557bba)

---

## 📂 Estrutura de Pastas

```
result/
├── txt/          # Arquivos de dados persistentes da SkipList (valores e níveis)
└── grafico/      # Imagens PNG geradas dos estados da SkipList
```

---

## 🚀 Como executar o projeto

### 1. Clone o projeto

```bash
git clone https://github.com/IMNascimento/AED.git
cd AED/python/aula/skiplist
```

---

### 2. Crie um ambiente virtual (recomendado)

#### **No Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### **No Windows (CMD ou PowerShell):**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Se não existir o `requirements.txt`, instale manualmente:

```bash
pip install matplotlib streamlit
```

---

### 4. Execute cada funcionalidade

#### **A. Terminal Interativo com Persistência**

Manipule a SkipList por comandos no terminal, com estrutura salva/restaurada:

```bash
python script_txt.py
```
Comandos aceitos:
- `insert VALOR` — insere valor (altura sorteada)
- `delete VALOR` — remove valor
- `search VALOR` — busca valor
- `show` — mostra a estrutura em ASCII
- `exit` — sai do programa

---

#### **B. Gerar Gráfico PNG da SkipList**

Gera a visualização atual da SkipList em `result/grafico/skiplist_plot.png`:

```bash
python script_plot.py
```

---

#### **C. Interface Web Interativa com Streamlit**

Adicione, remova ou busque valores em tempo real no navegador:

```bash
streamlit run script_streamlit.py
```

Acesse no navegador pelo link exibido (ex: http://localhost:8501).

**Para rodar em outra porta:**
```bash
streamlit run script_streamlit.py --server.port 5050
```

### D. Usando o CLI via linha de comando

O arquivo `skiplist_cli.py` permite operar a SkipList rapidamente usando comandos diretos no terminal.

#### Exemplos de uso:

- **Inserir valores**
    ```bash
    python skiplist_cli.py insert 10 20 35
    ```
    *Insere os valores 10, 20 e 35 na SkipList.*

- **Deletar valores**
    ```bash
    python skiplist_cli.py delete 20
    ```
    *Remove o valor 20 da SkipList (se existir).*

- **Buscar valores**
    ```bash
    python skiplist_cli.py search 35 999
    ```
    *Busca pelos valores 35 e 999, exibindo se estão presentes ou não.*

- **Mostrar a SkipList**
    ```bash
    python skiplist_cli.py show
    ```
    *Mostra a estrutura da SkipList no formato ASCII.*

#### Parâmetros opcionais

Você pode ajustar a altura máxima e a probabilidade dos níveis:

```bash
python skiplist_cli.py --max-level 8 --p 0.3 insert 1 2 3 4
```

---

**Observações:**
- Por padrão, os dados não são persistidos entre execuções neste CLI (é uma SkipList temporária).  
  Para persistência real, use os scripts `script_txt.py` ou `script_streamlit.py`.
- Sempre será exibido o estado atual da SkipList ao final de cada comando.


---

## 📑 Observações

- **A estrutura da SkipList é persistida (valor + altura) em arquivos `.txt`**, então ao abrir em qualquer um dos scripts a visualização será sempre idêntica, independentemente do sistema operacional.
- **Os gráficos são salvos automaticamente na pasta correta**. Pode usar as imagens em artigos, apresentações, etc.
- **Tudo funciona igual em Windows, Linux e macOS.**

---

## 📷 Screenshots

> Adicione suas imagens de exemplo aqui, caso queira!

---

## 🛠️ Dicas e Troubleshooting

- **Ambiente virtual** é fortemente recomendado para evitar conflitos de dependências.
- Para adicionar grandes quantidades de dados, use o modo terminal e insira via comando ou adapte conforme sua necessidade.
- Não modifique manualmente os arquivos `.txt` das pastas, para garantir a consistência dos níveis dos nós.

---

## ✨ Autores

> Igor Nascimento - Desenvolvedor Principal - [GitHub](https://github.com/IMNascimento) - [LinkdIn](https://www.linkedin.com/in/igor-m-nascimento/) - [Um pouco mais](https://imnascimento.github.io/Portifolio/)

---
