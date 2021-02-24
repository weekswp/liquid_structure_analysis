import os
import sys
from path import Path
cwd = os.getcwd()
original_cluster_dir = Path('../data/original_clusters/clusters')
split_size = 1000
def main():
    length = int(os.listdir(original_cluster_dir))
    limit = (length/split_size)+1
    data = ""
    for i in range(1,limit):
        data += "python find_motifs_single.py "+str(i)
    with open('motif_determination.sh','w') as out_file:
        out_file.write(data)
        out_file.close()

if __name__=='__main__':
    main()

