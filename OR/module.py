# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout


class Drawing:
    # edges = []

    def __init__(self, G, n):
        self.n = n
        self.graph = G
        self.D = nx.DiGraph(G)
        for i in range(n):
            self.D.add_node(i)
        self.pos = graphviz_layout(self.D,
                                   prog="dot")  # Генерирует координаты узлов чтобы граф выглядел как дерево(dot)
        self.node_color = "#A0CBE2"
        self.edge_color = "#00a3ff"
        self.width = 2

    def set_width(self, new_width):
        self.width = new_width

    def set_edge_color(self, new_color):
        self.edge_color = new_color

    def set_node_color(self, new_color):
        self.node_color = new_color

    def draw_graph(self, pause=-1):

        # Функция рисует граф. pause - время на которое появляется окно.
        # Если pause <0 то окно блокирует поток

        options = {
            "node_color": self.node_color,
            "edge_color": self.edge_color,
            "width": self.width,
            "node_size": 500,
            "font_weight": "bold",
            "with_labels": True
        }

        nx.draw(self.D, self.pos, **options)

        if pause > 0:
            plt.pause(pause)
        else:
            plt.show()

    def close(self):
        plt.close()
        self.node_color = "#A0CBE2"
        self.edge_color = "#00a3ff"
        self.width = 2


class Graph:
    def __init__(self, a=1, b=1, c=1, d=1):
        self.a, self.b, self.c, self.d = a, b, c, d

        self.pos = None
        if d % 3 == 0:
            self.n = 10
        elif d % 3 == 1:
            self.n = 11
        else:
            self.n = 12

        self.G = self.__fill_graph()
        self.G_matrix = self.__represent_to_adjacency_matrix()
        self.G_list = self.__represent_to_adjacency_list()
        self.drawing = Drawing(self.G, self.n)
        self.stop = False

    def __str__(self):
        return str(self.G)

    def set_abcd(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def set_stop(self):
        self.stop = True

    def __fill_graph(self):
        # Функция заполняет переменную G ребрами в соответсвии с условием задания

        G = []
        for i in range(0, self.n):
            for j in range(0, self.n):
                if (self.a * i + self.b * j) / self.c % self.d <= 1:
                    G.append((i, j))

        return G

    def print_edge_list(self):
        # Печать списка ребер
        for k in self.G:
            print(k)

    def test_fill(self):

        # Функция для тестового заполнения графа

        self.G = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 6), (3, 7), (3, 8), (6, 7), (9, 10)]
        self.n = 11
        self.G_list = self.__represent_to_adjacency_list()
        self.G_matrix = self.__represent_to_adjacency_matrix()
        self.drawing = Drawing(self.G, len(self.G))

    def __represent_to_adjacency_matrix(self):

        # Преобразует список ребер в матрицу смежности графа

        matrix = []
        for i in range(self.n + 1):
            line = []
            for j in range(self.n + 1):
                if (i, j) in self.G:
                    line.append(1)
                else:
                    line.append(0)
            matrix.append(line)
        return matrix

    def print_adjacency_matrix(self):

        # Печатает матрицу смежности графа

        print("{0:5}".format(""), end="")
        for i in range(self.n):
            print("{0:5}".format(i), end="")
        print()
        for i in range(self.n):
            print("{0:5}".format(i), end="")
            for j in range(self.n):
                print("{0:5}".format(self.G_matrix[i][j]), end="")
            print()

    def __represent_to_adjacency_list(self):

        # Преобразует список ребер в список смежности графа

        G2 = defaultdict(list)
        for k, v in self.G:
            G2[k].append(v)
        return dict(G2)

    def print_adjacency_list(self):
        # Печатает список смежности
        for i in self.G_list:
            print(f"{i} => {self.G_list[i]}")

    def node_colors_reshape(self, colors):
        # Преобразование цветов узлов из функции depth_first_search
        # в виде пригодном для передачи в класс Drawing

        hex_dict = {"Black": "#2f3c42",
                    "Grey": "#65808f",
                    "White": "#A0CBE2"}

        new_colors = list(map(lambda x: hex_dict[x], colors))  # список цветов в другом виде
        sort_colors = list(map(lambda i: new_colors[i],
                               self.drawing.D.nodes))  # этот же список но в порядке,необходимом для закрашивания узлов
        return sort_colors

    def edge_colors_reshape(self, edges):
        # Преобразование цветов ребер из функции depth_first_search
        # в виде пригодном для передачи в класс Drawing

        # Порядок вершин в объекте drawing остается тот же
        # Ребра по которым проходим становятся другого цвета
        new_edges = list(map(lambda x: "#000000" if x in edges else "#00a3ff", self.drawing.D.edges))
        return new_edges

    def width_reshape(self, edges):
        # Создание списка с разной шириной для ребер
        # Ребра по которым проходим становятся больше
        width_list = list(map(lambda x: 4 if x in edges else 2, self.drawing.D.edges))
        return width_list

    def set_color_node(self, color):
        self.drawing.set_node_color(self.node_colors_reshape(color))

    def set_width(self, edge_set):
        self.drawing.set_width(self.width_reshape(edge_set))

    def set_color_edge(self, edge_set):
        self.drawing.set_edge_color(self.edge_colors_reshape(edge_set))

    def draw(self, time=-1):
        self.drawing.draw_graph(time)

    def error_function(self):
        raise SyntaxError

    def depth_first_search(self, s=0, draw_mode=False, pause_set=-1):
        pred = [-1] * self.n  # родительские узлы
        color = ["White"] * self.n  # цвет узлов
        edge_set = set()  # множество хранящее ребра по которым уже прошли

        def dfs_visit(v):

            color[v] = "Grey"

            if draw_mode:
                self.set_color_node(color)
                self.draw(pause_set)

            neighbors = self.G_list.get(v)
            if neighbors:
                for neighbor in neighbors:

                    if draw_mode:
                        edge_set.add((v, neighbor))
                        self.set_color_edge(edge_set)
                        self.set_width(edge_set)
                        self.draw(pause_set)

                    if color[neighbor] == "White":
                        pred[neighbor] = v
                        dfs_visit(neighbor)
            color[v] = "Black"

            if draw_mode:
                self.set_color_node(color)
                self.draw(pause_set)

        dfs_visit(s)

        if draw_mode:
            self.set_color_node(color)
            self.draw(-1)

# if __name__ == "__main__":
#     # a, b, c, d = int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: ")), int(input("Enter d: "))
#     a, b, c, d = 43, 32, 12, 54
#     g = Graph(a, b, c, d)
#     # print(g.drawing.D.nodes)
#     g.test_fill()
#
#     # print(g.drawing.draw_animation())
#     g.print_adjacency_list()
#     g.depth_first_search(1,draw_mode=True, pause_set=1)
#     # g.drawing.draw_graph()
#     # g.drawing.draw_graph()
