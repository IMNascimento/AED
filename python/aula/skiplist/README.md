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

> Igor Nascimento - Desenvolvedor Principal - [GitHub](https://github.com/IMNascimento)

---
