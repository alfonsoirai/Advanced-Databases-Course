from graph import *

if __name__ == '__main__':
    voxGraph = Graph()
    voxGraph.read_csv('data/vox-nodes.csv',
                      'data/vox-edges.csv')

    print("\nBFS\n")
    bfsN, bfsS = voxGraph.bfs(223649167822693)

    for node, i in zip(bfsN, bfsS):
        x = "  " * node.level
        print(x + i)

    print("\nDFS\n")
    dfsN, dfsS = voxGraph.dfs(223649167822693)
    for node, i in zip(dfsN, dfsS):
        x = "  " * node.level
        print(x + i)
