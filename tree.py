from graphviz import Digraph

class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.hijos = []

class GameTree:
    def __init__(self, turnos):
        self.raiz = Nodo("Partida")
        self.construir(turnos)

    def construir(self, turnos):
        for numero, blanca, negra in turnos:
            nodo_turno = Nodo(f"Turno {numero}")
            nodo_blanca = Nodo(f"{numero}. {blanca}")
            nodo_turno.hijos.append(nodo_blanca)

            if negra:
                nodo_negra = Nodo(f"{numero}... {negra}")
                nodo_turno.hijos.append(nodo_negra)

            self.raiz.hijos.append(nodo_turno)

    def visualizar(self):
        dot = Digraph(format='png')
        dot.attr(rankdir='TB', size='10', dpi='100')

        self._agregar_nodos(dot, self.raiz)
        dot.render('arbol_partida', cleanup=True)
        print("\nÁrbol generado como 'arbol_partida.png'.")

    def _agregar_nodos(self, dot, nodo):
        if nodo:
            dot.node(str(id(nodo)), nodo.etiqueta)
            for hijo in nodo.hijos:
                dot.edge(str(id(nodo)), str(id(hijo)))
                self._agregar_nodos(dot, hijo)

