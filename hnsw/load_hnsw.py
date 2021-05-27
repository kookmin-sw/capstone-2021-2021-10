import hnswlib
import numpy as np

def load(graph):

    dim = 2000
    max_elements = 1000

    # Re-initializing, loading the index
    p = hnswlib.Index(space='l2', dim=dim)  
    print(f"\nLoading index from {graph} \n")
    p.load_index(graph, max_elements = max_elements)




