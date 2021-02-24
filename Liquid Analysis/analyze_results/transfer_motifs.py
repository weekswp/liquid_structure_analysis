import os
from shutil import copy
import sys
import numpy as np
from path import Path
# This file finds the motifs from the HDBSCAN groups for a given split set (replicate). 
# Parameters:
# affinity_dir: The location of the "affinities" files
# refined_dir: The location where the refined indices for the HDBSCAN groups were stored.
# cluster_dir: The cluster directory location for the replicate of interest.
# recombined_cluster_dir: The new location of the "recombined" motifs.
# recombined_tracker_dir: The storage location for the "group trackers" that keep track of the atoms represented by each of the motifs.
recombined_cluster_dir = Path('../data/Recombined/clusters')
recombined_tracker_dir = Path('../data/Recombined/group_trackers')
split_size = 1000

#Transfer the motifs from a given subshell
def transfer_motifs_rep(rep):
    motif_dir = Path('../data/split/'+str(rep)+'/motifs')
    affinity_dir = Path('../data/split/'+str(rep)+'/affinities')
    refined_dir = Path('../data/split/'+str(rep)+'/affinities/refined_indices')
    cluster_dir = Path('../data/split/'+str(rep)+'/clusters')
    if os.path.isdir(motif_dir):
        tracker = int(os.listdir(recombined_cluster_dir))
        for file in os.listdir(motif_dir):
            os.chdir(motif_dir)
            atom_identifier = str(file).split(".")[0]
            source = motif_dir+"/"+str(file)
            destination = recombined_cluster_dir+"/"+str(tracker)+".xyz"
            copy(source,destination)
            os.chdir(refined_dir)
            data = "Group "+str(atom_identifier)+".txt from replicate "+str(rep)+"\n"
            name = str(atom_identifier)+".txt"
            with open (name,"r") as old_group:
                old_group.readline()
                line = old_group.readline()
                while line != "":
                    new_ref = int(int(line)+(split_size*(rep-1)))
                    data += str(new_ref)+"\n"
                    line = old_group.readline()
                old_group.close()
            os.chdir(recombined_tracker_dir)
            new_name = str(tracker)+".txt"
            with open(new_name,"w") as new_group:
                new_group.write(data)
                new_group.close()
            tracker += 1
    else:
        print(str(rep)+" FAILED!")

#Transfer files for all replicates
def main():
    original_cluster_dir = Path('../data/original_clusters/clusters')
    length = int(len(os.listdir(original_cluster_dir)))
    limit = int(length/split_size)+1
    for i in range(1,limit):
        transfer_motifs_rep(i)

if __name__=='__main__':
    main()
