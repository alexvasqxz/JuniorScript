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

    def quads_len(self):
        return len(self.quadruplos)

    def modificar_quad(self, index, lista_cambios):
        old_quad = self.quadruplos[index]
        new_quad = []
        if isinstance(lista_cambios, list):
            for i, cambio in enumerate(lista_cambios):
                if cambio != None:
                    new_quad.append(cambio)
                else:
                    new_quad.append(old_quad[i])

            new_quad = tuple(new_quad)
            self.quadruplos[index] = new_quad
        else:
            raise Exception(f"ERROR: El parametro '{lista_cambios}' debe de ser una lista")
