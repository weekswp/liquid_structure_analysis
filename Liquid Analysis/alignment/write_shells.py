from path import Path
import os
alignment_dir = os.getcwd()
original_cluster_dir = Path('../data/original_clusters/clusters')
num_clusters = int(os.listdir(original_cluster_dir))
#Note that the split_size and cutoff parameters are going to be dependent on the application and the specific composition, respectively,
#where the cutoff is determined from the first valley in the pair distribution function of the original simulation cell.
split_size = 1000
cutoff = 3.7
num_splits = int(num_clusters/split_size)+1

def main():
    for i in range(1,num_splits+1):
        os.chdir(alignment_dir)
        local_data = "#!/bin/bash\n"
        for j in range(split_size):
            local_data += "python align_clusters.py "+str(j)+" "+str(i)+"\n"
        for j in range(split_size):
            local_data += "python extract_errors.py ../data/split/"+str(i)+"/results/"+str(j)+".xyz.json "+str(cutoff)+"\n"
        filename = "run_analysis_"+str(i)+".sh"
        with open(filename,'w') as out_file:
            out_file.write(local_data)
            out_file.close()

if __name__ == "__main__":
    main()
