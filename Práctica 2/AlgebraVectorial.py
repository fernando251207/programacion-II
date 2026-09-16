import math

class AlgebraVectorial:
    @staticmethod
    def _magnitud(v):
        return math.sqrt(sum(x**2 for x in v))
    @staticmethod
    def _dot(a, b):
        return sum(x * y for x, y in zip(a, b))
    @staticmethod
    def _sub(a, b):
        return [x - y for x, y in zip(a, b)]
    @staticmethod
    def _add(a, b):
        return [x + y for x, y in zip(a, b)]
    @staticmethod
    def _cross_3d(a, b):
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]
    def perpendicular(self, a, b, criterio="diagonales"):
        if criterio == "diagonales":
            return math.isclose(self._magnitud(self._add(a, b)), self._magnitud(self._sub(a, b)))
        elif criterio == "simetria":
            return math.isclose(self._magnitud(self._sub(a, b)), self._magnitud(self._sub(b, a)))  
        elif criterio == "producto_punto":
            return math.isclose(self._dot(a, b), 0.0) 
        elif criterio == "pitagoras":
            lhs = self._magnitud(self._add(a, b))**2
            rhs = self._magnitud(a)**2 + self._magnitud(b)**2
            return math.isclose(lhs, rhs)
    def paralela(self, a, b, criterio="escalar"):
        if criterio == "escalar":
            ratios = [x / y for x, y in zip(a, b) if y != 0]
            return all(math.isclose(r, ratios[0]) for r in ratios)
        elif criterio == "producto_cruz":
            cruz = self._cross_3d(a, b)
            return all(math.isclose(x, 0.0) for x in cruz)
    def proyeccion_de_a_sobre_b(self, a, b):
        mag_b_sq = self._magnitud(b)**2
        factor = self._dot(a, b) / mag_b_sq
        return [factor * x for x in b]
    def componente_de_a_en_b(self, a, b):
        return self._dot(a, b) / self._magnitud(b)
if __name__ == "__main__":
    av = AlgebraVectorial()
    v1 = [1, 0, 0]
    v2 = [0, 1, 0]

    print("v1 y v2 ortogonales (producto punto):", av.perpendicular(v1, v2, "producto_punto"))
    print("Proyección v1 en v2:", av.proyeccion_de_a_sobre_b(v1, v2))