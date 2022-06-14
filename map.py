import time
import matplotlib.pyplot as plt
import numpy as np
import random

#clase nodo
class Node:
    posx = 0
    posy = 0
    name = ""
    def __init__(self, posx, posy, name):
        self.posx = posx
        self.posy = posy
        self.name = name
    
    #retorna las coordenadas en forma de una tupla
    def coords(self):
        return (self.posx, self.posy)

    #distancia entre este nodo y el nodo objetivo 
    def h(self, obj):
        distance = (float(self.posx - obj.posx)**2.0 + float(self.posy - obj.posy)**2.0)**0.5
        return distance


class Edge:
    node1 = Node(0,0,'')
    node2 = Node(0,0,'')
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
    def line(self):
        x, y = [self.node1.posx, self.node2.posx], [self.node1.posy, self.node2.posy]
        return x, y
#def go(, matrix):
#    x = [[1,2,3,4],[]]
#    return


class map:
    nodes = list()
    edges = list()
    matrix = list()
    def __init__(self, points, matrix):
        self.matrix = matrix
        fig, ax = plt.subplots()
        ax.set_aspect("equal", adjustable="datalim")
        ax.set_box_aspect(0.5)
        ax.autoscale()
        plt.title('Mapa')        
        for i in points:
            self.nodes.append(Node(i[0],i[1],i[2]))
        for i in self.nodes:
            ax.add_patch(plt.Circle(i.coords(), 0.1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    print(i, j)
                    edge = Edge(self.nodes[i], self.nodes[j])
                    self.edges.append(edge)
        for i in self.edges:
            x, y = i.line()
            plt.plot(x, y)
        plt.show()
    def _find(self):
        return False
    

    def find(self, a, b):
        fig, ax = plt.subplots()
        found = False
        while not found:
            if self.nodes[a].coords() == self.nodes[b].coords():
                found = True
            


        plt.show()


def run():
    points = [[1,2,'A'],[3,7,'B'],[6,2,'C'],[4,4,'D'],[7,3,'E']]
    matrix = [
    [0,1,1,0,0],
    [1,0,0,1,0],
    [1,0,0,0,1],
    [0,1,0,0,1],
    [0,0,1,1,0]
    ]
    new_map = map(points, matrix)
    #new_map.find(1, 2)
    print('ok') #bandera
    pass


if __name__ == '__main__':
    run()
