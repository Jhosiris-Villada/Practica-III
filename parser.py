import re

class ChessParser:
    def __init__(self):
        self.regex_turno = re.compile(r"(\d+)\.\s*([^\s]+)(?:\s+([^\s]+))?")

        self.regex_jugada = re.compile(r"""
            (O-O(-O)?)
            |([KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](=[QRBN])?[\+#]?)
            |([a-h]x[a-h][1-8](=[QRBN])?[\+#]?)
            |([a-h][1-8](=[QRBN])?[\+#]?)
        """, re.VERBOSE)

    def analizar_partida(self, texto):
        turnos = []
        for match in self.regex_turno.finditer(texto):
            numero = match.group(1)
            blanca = match.group(2)
            negra = match.group(3)

            if not self.es_jugada_valida(blanca):
                raise ValueError(f"Jugada blanca inválida en el turno {numero}: {blanca}")
            if negra and not self.es_jugada_valida(negra):
                raise ValueError(f"Jugada negra inválida en el turno {numero}: {negra}")

            turnos.append((numero, blanca, negra))
        if not turnos:
            raise ValueError("No se detectaron turnos válidos.")
        return turnos

    def es_jugada_valida(self, jugada):
        return bool(self.regex_jugada.fullmatch(jugada))
