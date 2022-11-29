# Markov Chain representation
import random


class Vertex(object):
    def __init__(self, value):   # value will be the word
        self.value = value
        self.adjacent = {}  # nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def __str__(self):
        return self.value + ' '.join([node.value for node in self.adjacent.keys()])

    def add_edge_to(self, vertex, weight=0):
        # adding an edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # this is incrementing the weight of an existing edge
        # if vertex is a key in adjacent hen get value of that vertex
        # else default to zero
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        # map each word to its probability and put them in separate lists
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select the next weight based on weight
        # random.choices() : chooses from a list based on a given list of weights
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph(object):
    def __init__(self):
        self.vertices = {}  # string to Vertex mapping

    def get_vertex_values(self):
        # return all possible vertices
        return set(self.vertices.keys())

    def add_vertex(self, value):
        # add a new word to graph
        # value is the word that the vertex represents
        self.vertices[value] = Vertex(value)  # Vertex object

    def get_vertex(self, value):
        # get the Vertex object that represents the word (value)
        if value not in self.vertices:
            self.add_vertex(value)  # if value is not in graph
        return self.vertices[value]  # get the Vertex object

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
