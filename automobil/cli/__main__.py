import sys
from automobil.cli.commands import start_mcp, populate

def main():
    if len(sys.argv) < 2:
        print("Erro: Nenhum comando foi fornecido.", file=sys.stderr)
        print("Uso: python -m automobil.cli [populate|start-mcp]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "start-mcp":
        start_mcp()
    elif command == "populate":
        populate()
    else:
        print(f"Erro: Comando desconhecido '{command}'", file=sys.stderr)
        print("Comandos disponíveis: populate, start-mcp", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
