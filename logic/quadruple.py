class Quadruple:
    def __init__(self):
        self.quadruplos = []

    def agregar(self, operator, left, right, result):
        self.agregar_quadruplo((operator, left, right, result))

    def agregar_quadruplo(self, quad):
        if isinstance(quad, tuple) and len(quad) == 4:
            self.quadruplos.append(quad)
        else:
            raise Exception(f"ERROR: '{quad}' solamente se pueden agregar quadruplos a la lista")

    def obtener_quadruplos(self):
        return self.quadruplos