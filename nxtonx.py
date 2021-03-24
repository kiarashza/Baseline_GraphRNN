import  pickle
import networkx as nx
def load_and_convert_graph_list(fname,is_real=True):
    with open(fname, "rb") as f:
        graph_list = pickle.load(f)
    nx2 = []
    for G in graph_list:
        nx2.append([G.nodes(data=True), G.edges(data=True)])
    pickle.dump(nx2, open( "nx2_"+fname, "wb" ))

load_and_convert_graph_list(fname = "C:/git/Graph-Generative-Models/results/GRAPHRNN/GraphRNN_MLP_grid_4_128_pred_3000_1.dat")