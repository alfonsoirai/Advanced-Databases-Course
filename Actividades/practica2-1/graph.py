import pandas as pd

class Node(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.level = 0
        self.adjacency = {}

    def add_connection(self, node, cost):
        self.adjacency[node.id] = [cost, node]

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

    def bfs(self, firstID):
        firstNode = self.nodes[firstID]
        result = []
        resultString = []
        Q = []
        result.append(firstNode)
        Q.append(firstNode)
        firstNode.level = 0
        resultString.append(str(firstNode.level) + " " + firstNode.name)
        while Q:
            current = Q.pop(0)
            for i in current.adjacency.values():
                if i[1] not in result:
                    i[1].level = current.level + 1
                    result.append(i[1])
                    Q.append(i[1])
                    resultString.append(str(i[1].level) + " " + i[1].name)
        return result, resultString

    def dfs(self, firstID):
        firstNode = self.nodes[firstID]
        result = []
        resultString = []
        stack = []
        stack.append(firstNode)
        firstNode.level = 0
        while stack:
            current = stack.pop()
            if(current not in result):
                result.append(current)
                resultString.append(str(current.level) + " " + current.name)
            for i in current.adjacency.values():
                if i[1] not in result:
                    i[1].level = current.level + 1
                    stack.append(i[1])
        return result, resultString

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
