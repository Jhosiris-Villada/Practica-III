from parser import ChessParser
from tree import GameTree

def main():
    print("=== Analizador Sintáctico de Ajedrez ===\n")
    partida = input("Ingresa la partida en notación SAN (toda en una línea):\n")

    parser = ChessParser()
    try:
        turnos = parser.analizar_partida(partida)
        print("\nPartida válida sintácticamente.")
        tree = GameTree(turnos)
        tree.visualizar()
    except ValueError as e:
        print(f"\nError de sintaxis: {e}")

if __name__ == "__main__":
    main()
