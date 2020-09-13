import numpy as np

from margin import Graph, GraphCollection
from utils import *

if __name__ == '__main__':
    datasets = "mico-demo"
    graphs = []

    # graph_input = []
    # graph_input.append(np.array([[  1,  44,  44,  67,   0,   0,   0,   0],
    #        [ 44,   3,  17,  95,  13,  50, 105,  58],
    #        [ 44,  17,  28,   0,   0,   0,   0,   0],
    #        [ 67,  95,   0,  25,   0,   0,   0,   0],
    #        [  0,  13,   0,   0,  30,   0,  54,  98],
    #        [  0,  50,   0,   0,   0,  22,   0,   0],
    #        [  0, 105,   0,   0,  54,   0,  27,   0],
    #        [  0,  58,   0,   0,  98,   0,   0,  14]]))
    #
    # graph_input.append(np.array([[  3,  13,  17,  95,  50, 105,  44,  58],
    #        [ 13,  30,   0,   0,   0,  54,   0,  98],
    #        [ 17,   0,  28,   0,   0,   0,  44,   0],
    #        [ 95,   0,   0,  25,   0,   0,  67,   0],
    #        [ 50,   0,   0,   0,  22,   0,   0,   0],
    #        [105,  54,   0,   0,   0,  27,   0,   0],
    #        [ 44,   0,  44,  67,   0,   0,   1,   0],
    #        [ 58,  98,   0,   0,   0,   0,   0,  14]]))
    #
    # graph_input.append(np.array([[  3,  13,  95,  50, 105,  44,  58,  17],
    #        [ 13,  30,   0,   0,  54,   0,  98,   0],
    #        [ 95,   0,  25,   0,   0,  67,   0,   0],
    #        [ 50,   0,   0,  22,   0,   0,   0,   0],
    #        [105,  54,   0,   0,  27,   0,   0,   0],
    #        [ 44,   0,  67,   0,   0,   1,   0,  44],
    #        [ 58,  98,   0,   0,   0,   0,  14,   0],
    #        [ 17,   0,   0,   0,   0,  44,   0,  28]]))

    graph_input = readGraphs('{}.outx'.format(datasets))

    for i, graph_array in enumerate(graph_input):
        print("CONSTRUCTING LATTICE SEARCH SPACE... Graph %d" % i)
        graphs.append(Graph(graph_array))

    graphDB = GraphCollection(graphs, 1.0)
    MF = graphDB.margin()

    print(MF)
    for sg in MF["tree"]:
        plotGraph(sg, False)