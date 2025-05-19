from graphviz import Digraph

class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.izquierda = None
        self.derecha = None

class GameTree:
    def __init__(self, turnos):
        self.raiz = Nodo("Partida")
        self.construir(turnos)

    def construir(self, turnos):
        actual = self.raiz
        for numero, blanca, negra in turnos:
            nodo_blanca = Nodo(f"{numero}. {blanca}")
            actual.izquierda = nodo_blanca

            if negra:
                nodo_negra = Nodo(f"{numero}... {negra}")
                actual.derecha = nodo_negra
                actual = nodo_negra
            else:
                actual = nodo_blanca

    def visualizar(self):
        dot = Digraph()
        self._agregar_nodos(dot, self.raiz)
        dot.render('arbol_partida', format='png', cleanup=True)
        print("\nÁrbol generado como 'arbol_partida.png'.")

    def _agregar_nodos(self, dot, nodo):
        if nodo:
            dot.node(str(id(nodo)), nodo.etiqueta)
            if nodo.izquierda:
                dot.edge(str(id(nodo)), str(id(nodo.izquierda)), label="Blancas")
                self._agregar_nodos(dot, nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(id(nodo)), str(id(nodo.derecha)), label="Negras")
                self._agregar_nodos(dot, nodo.derecha)
