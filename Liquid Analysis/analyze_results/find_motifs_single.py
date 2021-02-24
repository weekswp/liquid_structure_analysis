import os
from shutil import copy
import sys
import numpy as np
from path import Path
# This file finds the motifs from the HDBSCAN groups for a given split set (replicate). 
# Parameters:
# replicate: The split group that we want the motifs for
# motif_dir: The location where we want to store the found motifs.
# affinity_dir: The location of the "affinities" files
# refined_dir: The location where the refined indices for the HDBSCAN groups were stored.
# cluster_dir: The cluster directory location for the replicate of interest.
replicate = int(sys.argv[1])
motif_dir = Path('../data/split/'+replicate+'/motifs')
affinity_dir = Path('../data/split/'+replicate+'/affinities')
refined_dir = Path('../data/split/'+replicate+'/affinities/refined_indices')
cluster_dir = Path('../data/split/'+replicate+'/clusters')

#Load the affinity file for given subset
def load_affinities():
    os.chdir(affinity_dir)
    affinities = np.load("combined_affinity.npy")
    return affinities

#Find motifs for groups of given replicate
def main():
    affinities = load_affinities()
    os.chdir(refined_dir)
    for file in os.listdir(refined_dir):
        os.chdir(refined_dir)
        group_list = []
        group_number = str(file).split(".")[0]
        with open(file,"r") as current_group:
            current_group.readline()
            line = current_group.readline()
            while line != "":
                group_list.append(int(line))
                line = current_group.readline()
            current_group.close()
        os.chdir(motif_dir)
        minimum = 1000
        pointer = 0
        for i in range (0,len(group_list)):
            local_diss = 0.0
            local_count = 0
            for j in range(0,len(group_list)):
                if i != j:
                    local_diss += float(affinities[group_list[i]][group_list[j]])
                    local_count += 1
            average = round(float(local_diss/local_count),4)
            if average < minimum:
                print("Found new minimum: "+str(group_list[i]))
                minimum = average
                pointer = i
        motif = group_list[pointer]
        source = str(cluster_dir)+"/"+str(motif)+".xyz"
        destination = str(motif_dir)+"/"+group_number+".xyz"
        copy(source,destination)
    os.chdir(refined_dir)

if __name__=='__main__':
    main()


