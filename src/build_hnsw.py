import hnswlib
import numpy as np

dim = 2000
num_elements = 1000

data = np.loadtxt("../mfcc_extract/other_mfcc.txt", dtype=float)
data_labels = np.arange(len(data))
data_titles = [ t.strip()[:-8] if t.strip()[-8:] == '_320kbps' else t.strip() for t in open("../mfcc_extract/titles.txt", "r")]

p = hnswlib.Index(space = 'cosine', dim = dim)
p.init_index(max_elements = num_elements, ef_construction = 200, M = 16)
p.add_items(data, data_labels)
p.set_ef(50) # ef should always be > k

labels, distances = p.knn_query(data[:10], k=5)
for i, nn in enumerate(labels):
    print(f"{data_titles[i]} : ")
    for n in nn: print(data_titles[n])

index_path='other_hnsw.bin'
print("Saving index to '%s'" % index_path)
p.save_index(index_path)
del p


