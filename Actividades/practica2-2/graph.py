import pandas as pd

class Node(object):
    def __init__(self, id, name, page_rank = 0):
        self.id = id
        self.name = name
        self.level = 0
        self.adjacency = {}
        self.adjacencyInverse={}
        self.connected = 0
        self.page_rank = page_rank

    def add_connection(self, node, cost):
        self.adjacency[node.id] = [cost, node]
        node.adjacencyInverse[self.id] = self
        self.connected += 1
    
    def update_page_rank(self, d = 0.85):
        acumulado = 0
        for node in self.adjacencyInverse.values():
            acumulado += node.page_rank / node.connected
        self.page_rank = (1-d) + (d) * acumulado
        

    def toString(self):
        string = str(self.id) + ", " + self.name + ":"
        for i in self.adjacency.values():
            string += "\n\t(" + str(i[1].id) + ", " + i[1].name + ")"
        return string


class Graph (object):
    def __init__(self, name="Vox Graph"):
        self.name = name
        self.size = 0
        self.nodes = {}

    def insert_node(self, node):
        self.nodes[node.id] = node
        self.size += 1

    def page_rank(self, iteraciones = 0):
        keys = self.nodes.keys()
        for _ in range(iteraciones):
            for key in keys:
                self.nodes[key].update_page_rank(d=0.85)
        page_rank_d={}
        for key in keys:
            page_rank_d[self.nodes[key].name] = self.nodes[key].page_rank
        key_value = zip(page_rank_d.keys(), page_rank_d.values())
        return dict(sorted(key_value, key=lambda x: x[1], reverse=True))

    def toString(self):
        string = ""
        for i in self.nodes.values():
            string += "\n" + i.toString()
        return self.name + " of size: " + str(self.size) + " with Nodes: " + string

    def read_csv(self, nodesFile, edgesFile):
        fileNodes = pd.read_csv(nodesFile)
        for i, row in fileNodes.iterrows():
            self.insert_node(Node(row['Id'], row['Label']))
        fileEdges = pd.read_csv(edgesFile)
        for i, row in fileEdges.iterrows():
            self.nodes[row['Source']].add_connection(self.nodes[row['Target']], 1)
