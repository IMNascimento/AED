import os
from skiplist import SkipList

TXT_DIR = os.path.join("result", "txt")
DATA_FILE = os.path.join(TXT_DIR, "skiplist_data_streamlit.txt")

def ensure_dirs():
    os.makedirs(TXT_DIR, exist_ok=True)

def load_values():
    ensure_dirs()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            items = []
            for line in f:
                if line.strip():
                    parts = line.strip().split(":")
                    value = int(parts[0])
                    level = int(parts[1])
                    items.append((value, level))
            return items
    return []

def save_values(items):
    ensure_dirs()
    with open(DATA_FILE, "w") as f:
        for value, level in items:
            f.write(f"{value}:{level}\n")

def run_streamlit():
    import streamlit as st

    st.title("SkipList Interativa (Persistente em TXT, com alturas)")

    if "items" not in st.session_state:
        st.session_state["items"] = load_values()

    skip = SkipList(max_level=8, p=0.5)
    for value, level in st.session_state["items"]:
        skip.insert(value, level=level)

    st.code(skip.print_skiplist_ascii())

    with st.form("form1"):
        val = st.number_input("Valor", min_value=0, value=1)
        col1, col2, col3 = st.columns(3)
        with col1:
            inserir = st.form_submit_button("Inserir")
        with col2:
            remover = st.form_submit_button("Remover")
        with col3:
            buscar = st.form_submit_button("Buscar")

    feedback = ""
    if inserir:
        exists = any(val == v for v, _ in st.session_state["items"])
        if not exists:
            skip.insert(val)
            # Descobre o nível do nó inserido
            current_level = 0
            node = skip.header.forward[0]
            while node:
                if node.value == val:
                    current_level = len(node.forward) - 1
                    break
                node = node.forward[0]
            st.session_state["items"].append((val, current_level))
            save_values(st.session_state["items"])
            feedback = f"Inserido: {val} com nível {current_level}"
        else:
            feedback = "Já existe!"
    elif remover:
        exists = False
        for idx, (v, l) in enumerate(st.session_state["items"]):
            if v == val:
                exists = True
                break
        if exists:
            skip.delete(val)
            st.session_state["items"] = [(v, l) for v, l in st.session_state["items"] if v != val]
            save_values(st.session_state["items"])
            feedback = f"Removido: {val}"
        else:
            feedback = "Não existe!"
    elif buscar:
        node = skip.search(val)
        feedback = f"Busca {val}: {'ENCONTRADO' if node else 'NÃO encontrado'}"

    if feedback:
        st.success(feedback)

    if st.button("Limpar tudo"):
        st.session_state["items"] = []
        save_values([])
        st.experimental_rerun()

if __name__ == "__main__":
    run_streamlit()
