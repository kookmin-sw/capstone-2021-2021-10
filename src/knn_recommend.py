from re import S
import hnswlib
import numpy as np
import mfcc_ext

def get_recommend(session, query, name, titles):
    
    dim = 2000
    max_elements = 1000
    # Re-initializing, loading the index
    p = hnswlib.Index(space='cosine', dim=dim)  
    print(f"{session}: Loading index")
    p.load_index(f"./{session}_hnsw.bin", max_elements = max_elements)

    
    #data_labels = np.arange(len(titles))
    labels, distances = p.knn_query(query, k=5)
    labels = labels.reshape(-1)
    result =[ titles[i] for i in labels]
    
    print(labels)
    print(distances)
    print(result)
    
    # p.add_items(query, len(titles))
    # index_path=f'{session}_hnsw.bin'
    # print(f"{session}: Saving index to {index_path}\n")
    # p.save_index(index_path)
    # del p
    
    return result

if __name__ == '__main__':
    titles = [ t.strip() for t in open("titles.txt", "r")]
    get_recommend('drums', mfcc_ext.extract("../seperated_audio/drums.wav") ,'test', titles)