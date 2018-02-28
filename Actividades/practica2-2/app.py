from graph import *

if __name__ == '__main__':
    voxGraph = Graph()
    voxGraph.read_csv('data/vox-nodes.csv',
                      'data/vox-edges.csv')

    print("\nPage Rank\n")
    page_rank = voxGraph.page_rank(50)
    for key, value in zip(page_rank.keys(), page_rank.values()):
        print(key + "\t\t\t"+ str(value))
