import random
import math
import matplotlib.pyplot as plt


class Triangulation(object):
    def __init__(self, n, V=None, D=None, coords=None):
        """A triangulation is defined by a list of vertices and a list of diagonals.
        It uses a variable for the size when creating a new triangulation, and coordinates 
        to print the triangulation. Diagonals are a tuple of sorted vertices."""
        self.n = n

        if V == None:
            self.V = list(range(n))
        else:
            self.V = V

        if D == None:
            self.D = self.__random_diagonals()
        else:
            self.D = D

        if coords == None:
            self.coords = {i: (math.cos(math.pi/2 + i*2*math.pi/self.n), 
                          math.sin(math.pi/2 + i*2*math.pi/self.n)) for i in range(self.n)}
        else:
            self.coords = coords

    def __random_noncons_vertices(self):
        """Selects two random non-consecutive vertices from the set of vertices of the polygon.
        It returns them sorted to convert them easily to a diagonal."""
        v1 = random.choice(self.V)
        v2 = random.choice([i for i in self.V if 
             abs(self.V.index(v1) - self.V.index(i))%(self.n - 1) > 1])

        return tuple(sorted((v1, v2)))

    def __split_vertices(self, d):
        """Splits the vertices along a selected diagonal d into two lists."""
        iv1, iv2 = sorted((self.V.index(d[0]), self.V.index(d[1])))
        V1 = sorted([self.V[i] for i in range(self.n) if 
             (i - iv1)%self.n <= (iv2 - iv1)%self.n])
        V2 = sorted([self.V[i] for i in range(self.n) if
             (i - iv1)%self.n >= (iv2 - iv1)%self.n or i == iv1])

        return V1, V2

    def __random_diagonals(self):
        """Initializes the diagonals of a polygon randomly. It does so by creating a diagonal,
        dividing the vertices along that diagonal and creating a new triangulation for each 
        new sets of vertices, so it can apply the procedure recursisvely."""
        if self.n <= 3:
            return set()

        d = self.__random_noncons_vertices()
        V1, V2 = self.__split_vertices(d)
        t1, t2 = Triangulation(len(V1), V=V1), Triangulation(len(V2), V=V2)

        return {d}.union(t1.D).union(t2.D)

    def common_diagonals(self, T):
        """Returns common diagonals with another triangulation T"""
        return self.D.intersection(T.D)

    def divide(self, d):
        """Divides the triangulation along some diagonal d into two different triangulations. 
        It splits the vertices into two lists with split_vertices and then copies the correspondent 
        diagonals and coordinates."""
        V1, V2 = self.__split_vertices(d)

        D1 = {d for d in self.D if d[0] in V1 and d[1] in V1}
        D2 = {d for d in self.D if d[0] in V2 and d[1] in V2}
        D1.remove(d)
        D2.remove(d)

        coords1 = {i: coord for i, coord in self.coords.items() if i in V1}
        coords2 = {i: coord for i, coord in self.coords.items() if i in V2}
        
        t1 = Triangulation(len(V1), V=V1, D=D1, coords=coords1)
        t2 = Triangulation(len(V2), V=V2, D=D2, coords=coords2)

        return t1, t2

    def multi_divide(self, D):
        """Divides the triangulation along a set of diagonals into len(D) + 1 triangulations.
        It does so by dividing the triangulation along some random diagonal and applying the
        procedure recursively, dividing each triangulation along their correspondent diagonals."""
        if not D:
            return [self]

        t1, t2 = self.divide(D[0])
        return t1.multi_divide([d for d in D if d in t1.D]) + t2.multi_divide([d for d in D if d in t2.D])

    def flip(self, d):
        """Flips a diagonal of the triangulation. The two other vertices of the quadrilateral
        are found based on that they must be the end point of edges of both v1 and v2 (with d=(v1,v2))."""
        edges = self.D.union(
                {tuple(sorted((i, j))) for i, j in zip(self.V, self.V[1:] + self.V[0:1])})
        v = [v for v in self.V if 
            (tuple(sorted((d[0], v))) in edges and tuple(sorted((d[1], v))) in edges)]
        self.D.remove(d)
        self.D.add(tuple(sorted(v)))

        return v

    def random_flips(self, k):
        """Peforms k flips at random in the triangulation"""
        for _ in range(k):
            d = random.choice(list(self.D))
            self.flip(d)

    def show(self):
        """Shows a picture of the triangulation using the coordinates attribute."""
        vertices = [[[self.coords[i][0], self.coords[j][0]], 
                   [self.coords[i][1], self.coords[j][1]]] 
                   for i, j in zip(self.V, self.V[1:] + self.V[0:1])]
        diagonals = [[[self.coords[d[0]][0], self.coords[d[1]][0]],
                    [self.coords[d[0]][1], self.coords[d[1]][1]]] for d in self.D]

        for vertex in vertices:
            plt.plot(*vertex, 'blue')
        for diagonal in diagonals:
            plt.plot(*diagonal, 'blue')

        plt.axis([-1.1, 1.1, -1.1, 1.1])
        plt.show()
