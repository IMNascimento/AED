import argparse
from skiplist import SkipList

def main():
    parser = argparse.ArgumentParser(description="SkipList CLI")
    parser.add_argument('--max-level', type=int, default=4, help="Altura máxima da SkipList (default: 4)")
    parser.add_argument('--p', type=float, default=0.5, help="Probabilidade dos níveis (default: 0.5)")
    parser.add_argument('command', choices=['insert', 'delete', 'search', 'show'], help="Operação a ser realizada")
    parser.add_argument('values', nargs='*', help="Valores para operar (inteiros separados por espaço)")

    args = parser.parse_args()
    skip = SkipList(max_level=args.max_level, p=args.p)

    # Para persistir o estado entre comandos, você pode salvar/carregar a lista de valores em arquivo.
    # Para simplificação, vamos usar uma lista temporária.
    if args.command != "show":
        # Se quiser manter os valores entre execuções, leia um arquivo ou inicialize como preferir.
        initial_values = []
        for v in initial_values:
            skip.insert(v)

    if args.command == "insert":
        for val in args.values:
            skip.insert(int(val))
            print(f"Inserido: {val}")

    elif args.command == "delete":
        for val in args.values:
            skip.delete(int(val))
            print(f"Removido: {val}")

    elif args.command == "search":
        for val in args.values:
            node = skip.search(int(val))
            print(f"Busca {val}: {'ENCONTRADO' if node else 'NÃO encontrado'}")

    elif args.command == "show":
        print("SkipList atual:")
        print(skip.print_skiplist_ascii())

    # Sempre mostra a lista ao final
    print("Estado atual da SkipList:")
    print(skip.print_skiplist_ascii())

if __name__ == "__main__":
    main()
