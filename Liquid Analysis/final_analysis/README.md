There are two main codes in this directory:

1.) `traceback_groups.py`: This code uses the `../data/Recombined/affinities/refined_indices` directory and the `../data/Recombined/group_trackers` directory to traceback each Recombined motif in each `refined_indices` file to the structures represented by that motif (`group_trackers/`). The code then transfers all represented structures to the `../data/Recombined/final_groups` directory where each file represents a single HDBSCAN group from the `../data/Recombined/affinities/refined_indices` directory.

2.) `forced_commonality.py`: This code uses the data in the `../data/Recombined/final_groups` directory and condenses it down into the final data set, saved in the `../data/Recombined/commonality_groups` directory. The first task of this code is to sort the final_groups files by size with the largest group first and the smallest last. Once we do this, we start to look at the structures in each of these final_group files starting with the largest. This code makes an important assumption: Each structure can only appear in one group and each structure should be left in the largest group to which it belongs. In other words, starting from the largest group, if we have already seen a particular structure, it is excluded from consideration in any subsequent groups in which it is found. The consequence of this is that there are fewer groups in the commonality_groups directory than the final_groups directory, as some of the smaller groups have no unique structures that haven't already been characterized by a larger group.