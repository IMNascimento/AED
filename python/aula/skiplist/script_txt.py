import os
from skiplist import SkipList

TXT_DIR = os.path.join("result", "txt")
DATA_FILE = os.path.join(TXT_DIR, "skiplist_data.txt")

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

def main():
    skip = SkipList(max_level=8, p=0.5)
    items = load_values()
    for value, level in items:
        skip.insert(value, level=level)

    print("=== SkipList TXT ===")
    print("Comandos: insert VALOR | delete VALOR | search VALOR | show | exit")
    while True:
        cmd = input("> ").strip().split()
        if not cmd:
            continue
        op = cmd[0].lower()
        if op == "exit":
            break
        elif op == "insert" and len(cmd) > 1:
            val = int(cmd[1])
            exists = any(val == v for v, _ in items)
            if not exists:
                skip.insert(val)
                current_level = 0
                node = skip.header.forward[0]
                while node:
                    if node.value == val:
                        current_level = len(node.forward) - 1
                        break
                    node = node.forward[0]
                items.append((val, current_level))
                save_values(items)
                print(f"Inserido: {val} com nível {current_level}")
            else:
                print("Já existe!")
        elif op == "delete" and len(cmd) > 1:
            val = int(cmd[1])
            skip.delete(val)
            old_len = len(items)
            items = [(v, l) for v, l in items if v != val]
            if len(items) != old_len:
                save_values(items)
                print(f"Removido: {val}")
            else:
                print("Não existe!")
        elif op == "search" and len(cmd) > 1:
            val = int(cmd[1])
            node = skip.search(val)
            print(f"Busca {val}: {'ENCONTRADO' if node else 'NÃO encontrado'}")
        elif op == "show":
            print(skip.print_skiplist_ascii())
        else:
            print("Comando inválido.")

if __name__ == "__main__":
    main()
