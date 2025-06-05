import os
from skiplist import SkipList

TXT_DIR = os.path.join("result", "txt")
GRAF_DIR = os.path.join("result", "grafico")

def ensure_dirs():
    os.makedirs(TXT_DIR, exist_ok=True)
    os.makedirs(GRAF_DIR, exist_ok=True)

def load_values(filename=os.path.join(TXT_DIR, "skiplist_data.txt")):
    ensure_dirs()
    if os.path.exists(filename):
        with open(filename, "r") as f:
            items = []
            for line in f:
                if line.strip():
                    parts = line.strip().split(":")
                    value = int(parts[0])
                    level = int(parts[1])
                    items.append((value, level))
            return items
    return []

def plot_skiplist_ascii(skip):
    print("ASCII da SkipList:")
    print(skip.print_skiplist_ascii())

def plot_skiplist_matplotlib(skip, filename=os.path.join("result", "grafico", "skiplist_plot.png")):
    import matplotlib.pyplot as plt

    pasta = os.path.dirname(filename)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)

    # Mapear todos nós do nível 0
    nodes_lvl0 = []
    node = skip.header.forward[0]
    while node:
        nodes_lvl0.append(node)
        node = node.forward[0]
    x_map = {id(node): i for i, node in enumerate(nodes_lvl0)}
    x_map[id(skip.header)] = -1

    fig, ax = plt.subplots(figsize=(14, 2.5 + skip.level * 0.7))
    color = ["#1976D2", "#388E3C", "#D32F2F", "#0097A7", "#FBC02D", "#8E24AA", "#FF7043"]

    node_radius = 0.25  # Quanto maior, mais espaço para o número
    head_radius = 0.35

    # 1. Desenhar horizontal de cada nível e os nós
    for lvl in range(skip.level, -1, -1):
        y = lvl
        node = skip.header
        xs = []
        labels = []
        while node.forward[lvl]:
            x_start = x_map[id(node)]
            x_end = x_map[id(node.forward[lvl])]
            ax.plot([x_start, x_end], [y, y], color=color[lvl % len(color)], linewidth=2.5, alpha=0.6)
            xs.append(x_end)
            labels.append(str(node.forward[lvl].value))
            node = node.forward[lvl]
        # Desenha círculos maiores e centralizados
        for xi in xs:
            circle = plt.Circle((xi, y), node_radius, color=color[lvl % len(color)], ec="black", zorder=4)
            ax.add_patch(circle)
        for xi, label in zip(xs, labels):
            ax.text(xi, y, label, ha='center', va='center', fontsize=13, color='white', weight='bold', zorder=5)

    # 2. Conexões verticais
    for node in nodes_lvl0:
        x = x_map[id(node)]
        y1 = 0
        y2 = len(node.forward) - 1
        ax.plot([x, x], [y1, y2], color="#616161", linestyle=':', linewidth=1.6, zorder=2)

    # 3. Header: quadrado maior e texto centralizado, destacado
    head_x = -1
    head_y = skip.level
    header_box = plt.Rectangle(
        (head_x - head_radius, head_y - head_radius),
        2 * head_radius, 2 * head_radius,
        color="#444444", ec="black", zorder=6, lw=2, alpha=0.98
    )
    ax.add_patch(header_box)
    ax.text(head_x, head_y, "Header", ha='center', va='center', fontsize=14, color='white', weight='bold', zorder=7)

    ax.axis('off')
    ax.set_ylim(-0.5, skip.level + 1)
    ax.set_xlim(-2, len(nodes_lvl0) + 1)
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    print(f"Imagem da skiplist salva em: {filename}")

def main():
    skip = SkipList(max_level=8, p=0.5)
    items = load_values()
    for value, level in items:
        skip.insert(value, level=level)

    plot_skiplist_ascii(skip)
    plot_skiplist_matplotlib(skip)

if __name__ == "__main__":
    main()
